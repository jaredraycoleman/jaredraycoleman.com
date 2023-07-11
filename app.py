from flask import Flask, render_template
from flask_talisman import Talisman
import os
from data import pubs, projects as projs, websites

app = Flask(__name__)

if os.getenv('FLASK_ENV') == 'production':
    Talisman(app, content_security_policy=None)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/publications')
def publications():
    return render_template('publications.html', publications=pubs, websites=websites)

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=projs)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
