import pandas as pd

df = pd.read_csv("merged_dataset.csv")

print("Before :", list(df.columns))

del df["name.1"]
del df["distance.1"]
del df["mass.1"]
del df["radius.1"]

df.dropna(axis="columns")

print("After:", list(df.columns))

df.to_csv("cleaned.csv")