from flask import Flask, jsonify, render_template, request, abort
import os
from flask_talisman import Talisman
import markdown
from bar import BarData, Cocktail, Ingredient, SAVEPATH
from data import pubs, websites

# Webhook + Git setup
import pathlib
import logging
import hmac
import hashlib
from git import Repo, GitCommandError
from dotenv import load_dotenv
from bar_build import build_bar

# --- Initialization ---
app = Flask(__name__)

if os.getenv('FLASK_ENV') == 'production':
    Talisman(app, content_security_policy=None)

load_dotenv()

# Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Git config
thisdir = pathlib.Path(__file__).parent.resolve()
STUDY_BREAK_DIR = thisdir / "study_break"
REMOTE_URL = os.getenv("STUDY_BREAK_REPO")
STUDY_BREAK_SECRET = os.getenv("STUDY_BREAK_SECRET", "").encode()

def clone_or_get_repo():
    if STUDY_BREAK_DIR.exists():
        try:
            return Repo(STUDY_BREAK_DIR)
        except Exception as e:
            logger.error(f"[webhook] Repo exists but invalid: {e}")
            raise RuntimeError("Invalid Git repo at study_break/")
    else:
        logger.info(f"[webhook] Cloning from {REMOTE_URL}")
        return Repo.clone_from(REMOTE_URL, STUDY_BREAK_DIR)

# Clone repo on startup
REPO = clone_or_get_repo()

# --- Web routes ---
@app.route('/')
def home():
    return render_template('index.html', publications=pubs, websites=websites)

@app.route('/get-email')
def get_email():
    return jsonify({'user': 'jared.coleman', 'domain': 'lmu.edu'})

@app.route('/studybreak')
def studybreak():
    bar = BarData.load()
    full_bar = bar.cocktails

    available_bar = {}
    unavailable_bar = {}
    shopping_list = set()

    for key, cocktail in full_bar.items():
        ingredients = cocktail.ingredients
        if all(i.in_stock for i in ingredients if i.in_stock is not None):
            available_bar[key] = cocktail
        else:
            unavailable_bar[key] = cocktail
            for i in ingredients:
                if i.in_stock is False:
                    shopping_list.add(i.name)

        if cocktail.source_text:
            cocktail.source_text = markdown.markdown(cocktail.source_text)

    return render_template(
        'studybreak.html',
        full_bar=full_bar,
        available_bar=available_bar,
        unavailable_bar=unavailable_bar,
        shopping_list=sorted(shopping_list)
    )

# --- GitHub webhook ---
@app.route('/api/studybreak-webhook', methods=['POST'])
def studybreak_webhook():
    if STUDY_BREAK_SECRET:
        signature = request.headers.get("X-Hub-Signature-256")
        if not signature:
            abort(400, "Missing signature")
        try:
            sha_name, sig = signature.split("=")
            mac = hmac.new(STUDY_BREAK_SECRET, msg=request.data, digestmod=hashlib.sha256)
            if not hmac.compare_digest(mac.hexdigest(), sig):
                abort(403, "Invalid signature")
        except Exception:
            abort(400, "Malformed signature header")

    try:
        REPO.remotes.origin.pull()
        build_bar()
        logger.info("[webhook] Successfully pulled and rebuilt bar.json")
        return "OK", 200
    except GitCommandError as e:
        logger.error(f"[webhook] Git pull failed: {e}")
        return "Git error", 500
    except Exception as e:
        logger.error(f"[webhook] Unhandled error: {e}")
        return "Internal error", 500

# --- Main ---
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
