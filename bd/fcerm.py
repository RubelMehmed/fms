import pandas as pd
import matplotlib.pyplot as plt

# === Data ===
data = {
    "Year": [
        "2005/06", "2006/07", "2007/08", "2008/09", "2009/10", "2010/11", "2011/12",
        "2012/13", "2013/14", "2014/15", "2015/16", "2016/17", "2017/18",
        "2018/19", "2019/20", "2020/21", "2021/22"
    ],
    "Central Government": [
        508.7, 506.9, 499.8, 567.6, 633.1, 670.1, 572.9,
        576.3, 606.2, 802.6, 710.8, 794.9, 777.0,
        792.4, 866.7, 1063.2, 1100.6
    ],
    "EA Local Levy": [
        19.7, 26.1, 17.0, 33.2, 38.0, 30.9, 33.7,
        20.2, 29.1, 24.1, 18.2, 27.1, 29.3,
        35.5, 38.0, 26.6, 20.2
    ],
    "Other Sources": [
        41.6, 34.5, 25.8, 22.1, 18.5, 17.1, 16.9,
        27.2, 39.4, 42.9, 55.8, 55.0, 49.8,
        42.8, 38.0, 70.1, 51.7
    ]
}

df = pd.DataFrame(data)
df["Total"] = df["Central Government"] + df["EA Local Levy"] + df["Other Sources"]

# === Plotting ===
plt.figure(figsize=(14, 7))

# Stacked bars
plt.bar(df["Year"], df["Central Government"], label="Central Government", color="#1f77b4")
plt.bar(df["Year"], df["EA Local Levy"], bottom=df["Central Government"], label="EA Local Levy", color="#ff7f0e")
plt.bar(df["Year"], df["Other Sources"], 
        bottom=df["Central Government"] + df["EA Local Levy"], label="Other Sources", color="#2ca02c")

# Axis and title
plt.ylabel("Funding (£ million)")
plt.title("Flood and Coastal Erosion Risk Management (FCERM) Total Funding Breakdown (2005–2022)")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
