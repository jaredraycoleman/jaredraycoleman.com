"""Main application file for the website."""
import os

from flask import Flask, render_template
from flask_talisman import Talisman

from data import pubs, websites

app = Flask(__name__)

if os.getenv('FLASK_ENV') == 'production':
    Talisman(app, content_security_policy=None)

@app.route('/')
def home():
    """Renders the home page."""
    return render_template('index.html', publications=pubs, websites=websites)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
