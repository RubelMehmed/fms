import pandas as pd
import matplotlib.pyplot as plt

# ==== Extracted data from chart ====
years = list(range(1960, 2011))

class_1 = [
    4, 4, 5, 4, 5, 4, 5, 6, 7, 6, 8, 7, 10, 8, 9, 11, 13, 12, 14, 13, 12,
    14, 13, 12, 14, 13, 15, 16, 18, 17, 19, 20, 21, 19, 22, 21, 23, 22,
    24, 23, 25, 30, 28, 31, 33, 29, 28, 30, 32, 34, 35
]

class_2 = [
    1, 1, 1, 1, 2, 1, 2, 1, 2, 2, 3, 2, 2, 2, 3, 2, 3, 3, 2, 3, 2,
    3, 2, 2, 3, 2, 3, 3, 2, 2, 3, 3, 4, 3, 4, 3, 4, 4, 4, 4, 4,
    4, 3, 3, 3, 4, 3, 4, 3, 3, 3
]

class_3 = [
    1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 2, 1, 1,
    1, 2, 1, 1, 1, 2, 2, 1, 2, 2, 1, 2, 1, 2, 2, 2, 2, 3, 3, 2,
    3, 2, 3, 3, 2, 2, 3, 3, 3, 3
]

# ==== Create DataFrame ====
df = pd.DataFrame({
    "Year": years,
    "Class 1": class_1,
    "Class 2": class_2,
    "Class 3": class_3
})
df["Total"] = df["Class 1"] + df["Class 2"] + df["Class 3"]
df["10yr_mean"] = df["Total"].rolling(window=10, center=True).mean()

# ==== Plotting ====
plt.figure(figsize=(14, 7))

# Stacked bars
plt.bar(df["Year"], df["Class 1"], label="Class 1 (Low Magnitude)", color="white", edgecolor="black")
plt.bar(df["Year"], df["Class 2"], bottom=df["Class 1"], label="Class 2 (Intermediate Magnitude)", color="gray")
plt.bar(df["Year"], df["Class 3"], bottom=df["Class 1"] + df["Class 2"], label="Class 3 (High Magnitude)", color="black")

# Line for 10-year running mean
plt.plot(df["Year"], df["10yr_mean"], label="10 Year Running Mean", color="black", linewidth=2)

# Labels & title
plt.xlabel("Year")
plt.ylabel("Reported Flood Events")
plt.title("Reported Flood Events in the UK (1960–2010)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
