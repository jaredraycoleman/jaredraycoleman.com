import os
import time
import pathlib
from git import Repo, GitCommandError
from bar_build import build_bar
from bar import SAVEPATH
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Config
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# set log level to INFO
logger.setLevel(logging.INFO)

POLL_INTERVAL = 60  # seconds (1 minute)
thisdir = pathlib.Path(__file__).parent.resolve()
STUDY_BREAK_DIR = thisdir / "study_break"
REMOTE_URL = os.getenv("STUDY_BREAK_REPO")

def clone_or_get_repo():
    if STUDY_BREAK_DIR.exists():
        try:
            # Try to use it as an existing Git repo
            return Repo(STUDY_BREAK_DIR)
        except Exception as e:
            logger.error(f"Existing study_break/ is not a git repo: {e}")
            # Optional: clear and re-clone, or raise an error
            raise RuntimeError("study_break/ exists but is not a valid git repo.")
    else:
        logger.info(f"Cloning repo from {REMOTE_URL}...")
        return Repo.clone_from(REMOTE_URL, STUDY_BREAK_DIR)

def run_poller():
    repo = clone_or_get_repo()
    origin = repo.remotes.origin
    origin.fetch()

    # Automatically detect default branch (main or master)
    default_branch = None
    for ref in origin.refs:
        if ref.name.endswith("/main"):
            default_branch = ref
            break
        if ref.name.endswith("/master"):
            default_branch = ref

    if not default_branch:
        raise RuntimeError("Could not detect remote default branch (main/master)")

    last_commit = default_branch.commit.hexsha

    while True:
        try:
            origin.fetch()
            new_commit = default_branch.commit.hexsha
        except Exception as e:
            logger.error(f"[poller] Error fetching: {e}")
            time.sleep(POLL_INTERVAL)
            continue

        if new_commit != last_commit or not SAVEPATH.exists():
            logger.info(f"[poller] New commit detected: {new_commit}")
            try:
                origin.pull()
                build_bar()
                last_commit = new_commit
            except GitCommandError as e:
                logger.error(f"[poller] Error pulling repo: {e}")
        else:
            logger.info("[poller] No changes detected.")
        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    if REMOTE_URL is None:
        raise EnvironmentError("STUDY_BREAK_REPO environment variable is not set.")
    run_poller()
