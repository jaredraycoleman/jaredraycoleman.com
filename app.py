from flask import Flask, jsonify, render_template
import os
from flask_talisman import Talisman
import markdown
from bar import BarData, Cocktail, Ingredient
from data import pubs, websites

app = Flask(__name__)

if os.getenv('FLASK_ENV') == 'production':
    Talisman(app, content_security_policy=None)

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
        # If all ingredients are in stock (or None), it's available
        ingredients = cocktail.ingredients
        if all(i.in_stock for i in ingredients if i.in_stock is not None):
            available_bar[key] = cocktail
        else:
            unavailable_bar[key] = cocktail
            for i in ingredients:
                if i.in_stock is False:
                    shopping_list.add(i.name)

        # Render source_text markdown
        if cocktail.source_text:
            cocktail.source_text = markdown.markdown(cocktail.source_text)

    return render_template(
        'studybreak.html',
        full_bar=full_bar,
        available_bar=available_bar,
        unavailable_bar=unavailable_bar,
        shopping_list=sorted(shopping_list)
    )

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
