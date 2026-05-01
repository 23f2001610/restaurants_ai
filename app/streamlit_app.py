import streamlit as st
import pandas as pd


df = pd.read_csv("data/swiggy_dataset.csv")


df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

df = df.dropna(subset=["price", "rating"])


df["deal_score"] = df["rating"] / df["price"]

st.title("AI Food Deal Finder")
st.write("Search the best food deals from your restaurant dataset")

dish_query = st.text_input("Search food")
max_price = st.slider("Maximum price", 0, 1000, 300)
veg_only = st.checkbox("Veg only")

if st.button("Find Deals"):

    results = df[df["dish"].str.contains(dish_query, case=False, na=False)]
    results = results[results["price"] <= max_price]

    if veg_only:
        results = results[results["veg"] == 1]

    results = results.sort_values(by="deal_score", ascending=False)

    if not results.empty:
        best = results.iloc[0]

        best_restaurant = best["restaurant"].replace(".json", " ")

        st.success(
            f"🔥 Best Deal: {best['dish']} from {best_restaurant} "
            f"at ₹{best['price']} ⭐ {best['rating']}"
        )

        st.write("Top results")

        st.dataframe(
            results[["restaurant", "dish", "price", "rating", "deal_score"]].head(20)
        )