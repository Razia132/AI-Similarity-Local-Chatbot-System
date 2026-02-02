from fastapi import FastAPI
from pydantic import BaseModel
from model import get_recipe

app = FastAPI(title="Recipe Recommendation Chatbot")

# Request body model
class RecipeRequest(BaseModel):
    ingredients: str

# Root endpoint (optional but nice)
@app.get("/")
def read_root():
    return {"message": "Recipe Chatbot API is running"}

# Chat endpoint
@app.post("/chat")
def chat(request: RecipeRequest):
    recipe = get_recipe(request.ingredients)
    return {"recipe": recipe}
