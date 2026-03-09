import pandas as pd

# Load dataset
df = pd.read_csv("../data/swiggy_dataset.csv")

# Clean data
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

df = df.dropna(subset=["dish", "price"])

print("Dataset loaded:", len(df), "dishes")

while True:

    print("\n--- Food Finder ---")

    dish_query = input("Enter dish name (or 'exit'): ")

    if dish_query == "exit":
        break

    max_price = int(input("Max price: "))

    results = df[
        df["dish"].str.contains(dish_query, case=False, na=False)
    ]

    results = results[results["price"] <= max_price]

    results = results.sort_values(by="rating", ascending=False)

    print("\nTop Results:\n")

    print(results[["dish", "restaurant", "price", "rating"]].head(10))