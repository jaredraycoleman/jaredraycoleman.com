import os
from typing import Dict, List, Optional
import pathlib
import pydantic
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

thisdir = pathlib.Path(__file__).parent.resolve()
SAVEPATH = thisdir / "static" / "data" / "bar.json"

class Ingredient(pydantic.BaseModel):
    name: str
    category: Optional[str] = None
    in_stock: Optional[bool] = None
    description: Optional[str] = None

class Cocktail(pydantic.BaseModel):
    name: str
    description: Optional[str]
    ingredients: List[Ingredient]
    instructions: Optional[str] = None
    source_text: Optional[str] = None

class BarData(pydantic.BaseModel):
    cocktails: Dict[str, Cocktail]

    @property
    def ingredients(self) -> Dict[str, Ingredient]:
        """Returns a dictionary of all ingredients used in the cocktails."""
        ingredients = {}
        for cocktail in self.cocktails.values():
            for ingredient in cocktail.ingredients:
                if ingredient.name not in ingredients:
                    ingredients[ingredient.name] = ingredient
        return ingredients
    
    def save(self):
        """Saves the bar data to a JSON file."""
        SAVEPATH.parent.mkdir(parents=True, exist_ok=True)
        SAVEPATH.write_text(self.model_dump_json(indent=2), encoding='utf-8')
    
    @classmethod
    def load(cls) -> 'BarData':
        """Loads the bar data from a JSON file."""
        if not SAVEPATH.exists():
            return cls(cocktails={})
        return cls.model_validate_json(SAVEPATH.read_text(encoding='utf-8'))


