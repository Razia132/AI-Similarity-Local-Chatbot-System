# Task 1: Name Similarity Matching System

## 📌 Objective
The objective of this task is to build a name-matching system that identifies the most similar person names from a predefined dataset when a user inputs a name.

This task simulates real-world scenarios where exact name matching may fail due to spelling variations or phonetic differences.

---

## 🧠 Approach
- A dataset of person names is stored externally in a text file (`names.txt`).
- The dataset is loaded dynamically at runtime.
- String similarity is calculated using a similarity scoring algorithm.
- The system ranks matches and displays the closest match along with alternative suggestions.

---

## 📂 Dataset
- File: `names.txt`
- Format: One name per line
- Contains 30+ person names with spelling and phonetic variations
- Dataset can be extended without changing code

---

## 🔍 How It Works
1. User enters a name via the command line.
2. The system compares the input with all names in the dataset.
3. Similarity scores are computed and ranked.
4. The best match and other close matches are displayed with scores.

---

## ▶️ How to Run
```bash
pip install -r requirements.txt
python name_matcher.py

Enter a name: Razi

Best Match:
Razia (Similarity Score: 0.89)

Other Similar Matches:
Nazia - 0.67


🛠️ Technologies Used
Python

RapidFuzz (string similarity)

