import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("data/swiggy_dataset.csv")
# Clean data
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

st.title("🍔 AI Food Deal Finder")

st.write("Search the best food deals from your restaurant dataset")

dish_query = st.text_input("Search food")

max_price = st.slider("Maximum price", 0, 1000, 300)

veg_only = st.checkbox("Veg only")

if st.button("Find Deals"):

    results = df[df["dish"].str.contains(dish_query, case=False, na=False)]

    results = results[results["price"] <= max_price]

    if veg_only:
        results = results[results["veg"] == 1]

    results = results.sort_values(by="rating", ascending=False)

    st.write("Top results")

    st.dataframe(results[["dish", "restaurant", "price", "rating"]].head(20))