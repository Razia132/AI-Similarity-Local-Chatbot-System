# Task 2: Local Recipe Recommendation Chatbot

## 📌 Objective
The objective of this task is to build a locally running AI chatbot that suggests recipes based on user-provided ingredients.

The chatbot is implemented using a lightweight approach and is exposed through a FastAPI-based API. The entire system runs locally without relying on any external or paid APIs.

---

## 🧠 Approach
- A small custom recipe dataset is used to guide the chatbot responses.
- User-provided ingredients are matched against the dataset using similarity-based logic.
- The chatbot logic is separated from the API layer for better modularity.
- FastAPI is used to expose the chatbot functionality through a REST API.
- The chatbot can be tested using FastAPI’s built-in Swagger UI.

---

## 📂 Project Structure

task2_recipe_chatbot/
│
├── app.py # FastAPI application
├── model.py # Recipe matching logic
├── data/
│ └── recipes.json # Recipe dataset
├── requirements.txt # Dependencies
└── README.md


---

## 📄 Dataset
- File: `data/recipes.json`
- Format: JSON
- Each entry contains:
  - `ingredients`: comma-separated ingredient list
  - `recipe`: suggested recipe text
- Dataset is lightweight and can be extended easily

---

## 🔄 How It Works
1. User sends ingredients to the API.
2. The API forwards the input to the recipe-matching logic.
3. The system finds the closest matching ingredients from the dataset.
4. A relevant recipe is returned as a JSON response.

---

## ▶️ How to Run

### Step 1: Install dependencies
Navigate to the Task 2 folder and run:
```bash
pip install -r requirements.txt
Step 2: Start the FastAPI server
python -m uvicorn app:app --reload
You should see:

Uvicorn running on http://127.0.0.1:8000
🌐 How to Use the Chatbot
Open your browser and go to:

http://127.0.0.1:8000/docs
Use the POST /chat endpoint.

Click Try it out.

Enter ingredients in JSON format.

Sample Request
{
  "ingredients": "egg, onion"
}
Sample Response
{
  "recipe": "You can prepare a simple egg omelette by beating eggs and cooking them with chopped onions."
}
🛠️ Technologies Used
Python

FastAPI

Uvicorn

RapidFuzz

🎯 Learning Outcome
This task demonstrates:

Local AI system design

Dataset-driven chatbot logic

REST API development using FastAPI

Clean project structuring and documentation