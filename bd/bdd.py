import matplotlib.pyplot as plt
import pandas as pd

# === Data in BDT ===
bdt_budgets = {
    "Fiscal Year": ["2019–20", "2021–22", "2022–23", "2023–24", "2024–25"],
    "Operating Budget (BDT Billion)": [9872.00, 10123.55, 10763.97, 10588.70, 11002.97]
}

# Convert to DataFrame
df = pd.DataFrame(bdt_budgets)

# Convert BDT to USD
exchange_rate = 110  # BDT per USD
df["Operating Budget (USD Billion)"] = df["Operating Budget (BDT Billion)"] / exchange_rate

# === Plotting ===
plt.figure(figsize=(10, 6))
bars = plt.bar(df["Fiscal Year"], df["Operating Budget (USD Billion)"], color="#1f77b4")

# Add value labels
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval:.2f}', ha='center', va='bottom')

plt.title("Bangladesh Disaster Management Budget in USD (FY 2019–20 to 2024–25)")
plt.xlabel("Fiscal Year")
plt.ylabel("Operating Budget (Billion USD)")
plt.ylim(85, 105)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

import os
print("Current working directory:", os.getcwd())
