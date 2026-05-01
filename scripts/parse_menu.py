import json
import os
import pandas as pd

menu_folder = "menus"

rows = []

for file in os.listdir(menu_folder):

    if file.endswith(".json"):

        path = os.path.join(menu_folder, file)

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        try:
            cards = data["data"]["cards"]

            for card in cards:

                if "groupedCard" in card:

                    groups = card["groupedCard"]["cardGroupMap"]["REGULAR"]["cards"]

                    for g in groups:

                        if "itemCards" in g["card"]["card"]:

                            items = g["card"]["card"]["itemCards"]

                            for item in items:

                                info = item["card"]["info"]

                                rows.append({
                                    "restaurant": file.replace(".json", " "),
                                    "dish": info.get("name"),
                                    "price": info.get("price",0)/100,
                                    "rating": info.get("ratings",{}).get("aggregatedRating",{}).get("rating"),
                                    "veg": info.get("isVeg")
                                })

        except:
            pass


df = pd.DataFrame(rows)

print(df.head())

df.to_csv("data/swiggy_dataset.csv", index=False)

print("Dataset created!")