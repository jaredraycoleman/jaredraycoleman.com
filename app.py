"""Main application file for the website."""
import os

from flask import Flask, render_template
from flask_talisman import Talisman

from data import projects as projs
from data import pubs, websites

app = Flask(__name__)

if os.getenv('FLASK_ENV') == 'production':
    Talisman(app, content_security_policy=None)

@app.route('/')
def home():
    """Renders the home page."""
    return render_template('index.html')

@app.route('/publications')
def publications():
    """Renders the publications page."""
    return render_template('publications.html', publications=pubs, websites=websites)

@app.route('/projects')
def projects():
    """Renders the projects page."""
    return render_template('projects.html', projects=projs)

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
