import json
import os
from rapidfuzz import process, fuzz

# Get base directory of this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to recipes dataset
DATA_PATH = os.path.join(BASE_DIR, "data", "recipes.json")

# Load recipes from JSON file
def load_recipes():
    with open(DATA_PATH, "r") as file:
        return json.load(file)

# Get recipe suggestion based on ingredients
def get_recipe(user_ingredients: str):
    recipes = load_recipes()

    # Prepare list for matching
    ingredient_list = [item["ingredients"] for item in recipes]

    # Find best match
    match = process.extractOne(
        user_ingredients,
        ingredient_list,
        scorer=fuzz.token_sort_ratio
    )

    if match and match[1] >= 60:
        matched_ingredients = match[0]
        for item in recipes:
            if item["ingredients"] == matched_ingredients:
                return item["recipe"]

    return "Sorry, no suitable recipe found for the given ingredients."
