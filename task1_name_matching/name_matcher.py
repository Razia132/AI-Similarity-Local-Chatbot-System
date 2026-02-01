from rapidfuzz import process, fuzz

# Loading names from dataset file
with open("task1_name_matching/names.txt", "r") as file:
    names = [line.strip() for line in file if line.strip()]


# Taking input from user
user_name = input("Enter a name: ")

# Finding similarity scores
matches = process.extract(
    user_name,
    names,
    scorer=fuzz.ratio,
    limit=5
)

# Displaying results
print("\nBest Match:")
print(f"{matches[0][0]} (Similarity Score: {matches[0][1] / 100:.2f})")

print("\nOther Similar Matches:")
for name, score, _ in matches[1:]:
    print(f"{name} - {score / 100:.2f}")
