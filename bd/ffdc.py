import matplotlib.pyplot as plt

# Data
districts = ['Noakhali', 'Cumilla', 'Feni', 'Chattogram', 'Lakshmipur', 'Moulvibazar',
             'Brahmanbaria', 'Habiganj', 'Kishoreganj', 'Cox’s Bazar', 'Sylhet']
losses = [4192, 3390, 2683, 1677, 1404, 506, 144, 144, 127, 102, 21]

# Plot
plt.figure(figsize=(10, 6))
bars = plt.bar(districts, losses, color='orange')
plt.title('District-Wise Flood Losses (2024)', fontsize=14, fontweight='bold')
plt.ylabel('Losses (crore taka)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 100, f'{yval}', ha='center', fontsize=9)

plt.tight_layout()
plt.show()
