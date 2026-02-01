from rapidfuzz import process, fuzz

# Loading names from dataset file
with open("task1_name_matching/names.txt", "r") as file:
    names = [line.strip() for line in file if line.strip()]


# Taking input from user
user_name = input("Enter a name: ").strip().title()


# Finding similarity scores
matches = process.extract(
    user_name,
    names,
    scorer=fuzz.ratio,
    limit=10
)

# Keep only good matches
matches = [m for m in matches if m[1] >= 60]

# Displaying results
if not matches:
    print("\nNo close matches found.")
else:
    print("\nBest Match:")
    print(f"• {matches[0][0]} (Similarity Score: {matches[0][1] / 100:.2f})")

    if len(matches) > 1:
        print("\nOther Similar Matches:")
        for name, score, _ in matches[1:]:
            print(f"• {name} - {score / 100:.2f}")

