import pandas as pd
import matplotlib.pyplot as plt

# Sampled Data (extracted visually from the image)
data = {
    "Year": [1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
    "Class 1": [0, 1, 3, 7, 10, 4, 5, 6, 10, 12, 10, 14, 19],
    "Class 2": [0, 0, 1, 2, 3, 2, 3, 2, 3, 4, 3, 4, 5],
    "Class 3": [0, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 2, 3],
}

df = pd.DataFrame(data)
df["Total"] = df["Class 1"] + df["Class 2"] + df["Class 3"]

# Calculate 10-year running mean
df["10yr_mean"] = df["Total"].rolling(window=3, center=True).mean()

# Plotting
plt.figure(figsize=(12, 6))

# Bar plot (stacked)
plt.bar(df["Year"], df["Class 1"], label="Class 1 (Low)", color="white", edgecolor="black")
plt.bar(df["Year"], df["Class 2"], bottom=df["Class 1"], label="Class 2 (Intermediate)", color="gray")
plt.bar(df["Year"], df["Class 3"], bottom=df["Class 1"] + df["Class 2"], label="Class 3 (High)", color="black")

# Line plot for 10-year running mean
plt.plot(df["Year"], df["10yr_mean"], color="black", label="10 Year Running Mean", linewidth=2)

plt.xlabel("Year")
plt.ylabel("Reported Flood Events")
plt.title("Flood Events in the UK (Sampled Data)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

