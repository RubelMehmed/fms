import matplotlib.pyplot as plt
import pandas as pd

# === Data ===
data = {
    "Year": [2014, 2015, 2016, 2017, 2018, 2019, 2020],
    "Fund_Million_USD": [8.6, 11.25, 9.41, 26.69, 0, 11.76, 36.49]
}

df = pd.DataFrame(data)

# === Plotting ===
plt.figure(figsize=(10, 6))
bars = plt.bar(df["Year"], df["Fund_Million_USD"], color="#1f77b4")

# Add value labels
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval:.2f}', ha='center', va='bottom')

plt.title("Bangladesh Disaster Management Funding (2014–2020)")
plt.xlabel("Year")
plt.ylabel("Fund Mobilised (Million USD)")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
