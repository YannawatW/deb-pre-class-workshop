# ใช้ pandas (เครื่องมือจริงของ Data Engineer)
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/zkan/data-engineering-bootcamp/refs/heads/main/dataset/greenery/promos.csv")
print(df.head())
print(df.describe())

df_filtered = df[df["status"] == "inactive"]
print(df_filtered)
