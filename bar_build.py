from functools import lru_cache
import re
from typing import Dict
import obsidiantools.api as otools
import pathlib
import dotenv

from bar import Ingredient, Cocktail, BarData

# Load environment variables from .env file
dotenv.load_dotenv()

thisdir = pathlib.Path(__file__).parent.resolve()
bardir = thisdir / "study_break"
ingredientsdir = bardir / "Ingredients"
cocktailsdir = bardir / "Cocktails"

wikilink_pattern = re.compile(r"\[\[(?:.*?/)?([^|\]]+)(?:\|([^\]]+))?\]\]")
@lru_cache(maxsize=None)
def extract_display_name(s: str) -> str:
    """
    Extracts the display name from a wikilink or returns the raw name if it's not a link.
    """
    match = wikilink_pattern.match(s.strip())
    if match:
        return match.group(2) or match.group(1).split('/')[-1].strip()
    return s.strip()

@lru_cache(maxsize=None)
def load_ingredient(vault: otools.Vault, name: str) -> Ingredient:
    """Load an ingredient from the vault."""
    try:
        metadata = vault.get_front_matter(name)
        return Ingredient(
            name=name,
            category=metadata.get('category'),
            in_stock=metadata.get('in_stock', False),
            description=metadata.get('description')
        )
    except ValueError:
        return Ingredient(
            name=name,
            category=None,
            in_stock=False,
            description=None
        )

def load_cocktail(vault: otools.Vault, name: str) -> Cocktail:
    """Load a cocktail from the vault."""
    metadata = vault.get_front_matter(name)
    ingredients = [
        extract_display_name(ing.strip())
        for ing in metadata.get('ingredients', [])
        if ing.strip()
    ]
    source_text: str = vault.get_source_text(name)
    for link in wikilink_pattern.finditer(source_text):
        source_text = source_text.replace(
            link.group(0),
            extract_display_name(link.group(0))
        )

    return Cocktail(
        name=name,
        description=metadata.get('description'),
        ingredients=[load_ingredient(vault, ing) for ing in ingredients],
        instructions=metadata.get('instructions'),
        source_text=source_text
    )

def load_ingredients(vault: otools.Vault) -> Dict[str, Ingredient]:
    """Load all ingredients from the vault."""
    ingredients = {}
    for file in ingredientsdir.glob("*.md"):
        name = file.stem
        ingredients[name] = load_ingredient(vault, name)
    return ingredients

def load_cocktails(vault: otools.Vault) -> Dict[str, Cocktail]:
    """Load all cocktails from the vault."""
    cocktails = {}
    for file in cocktailsdir.glob("*.md"):
        name = file.stem
        cocktails[name] = load_cocktail(vault, name)
    return cocktails

def build_bar():
    vault = otools.Vault(bardir).connect().gather()
    cocktails = load_cocktails(vault)
    print(f"Loaded {len(cocktails)} cocktails.")
    bar_data = BarData(cocktails=cocktails)
    print(f"Bar data loaded with {len(bar_data.ingredients)} unique ingredients.")
    bar_data.save()

if __name__ == "__main__":
    build_bar()