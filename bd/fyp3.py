import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')


# Your existing DataFrame setup (only the % values)
data = {
    "Year": [
        1954, 1955, 1956, 1960, 1961, 1962, 1963, 1964, 1965, 1966,
        1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976,
        1977, 1978, 1980, 1982, 1983, 1984, 1985, 1986, 1987, 1988,
        1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1998, 1999,
        2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
        2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019,
        2020, 2021
    ],
    "Flood_Affected_Percent": [
        25, 34, 24, 19, 20, 25, 29, 21, 19, 23,
        17, 25, 28, 29, 25, 14, 20, 36, 11, 19,
        8, 7, 22, 2, 7.5, 19, 8, 4, 39, 61,
        4, 2.4, 19, 1.4, 20, 0.2, 22, 24, 68, 22,
        24, 2.8, 10, 14, 38, 12, 11, 42, 23, 19,
        18, 20, 12, 10.6, 25, 32, 33, 42, 23, 31,
        40, 33
    ]
}

df = pd.DataFrame(data)

# Stats
avg = df['Flood_Affected_Percent'].mean()

# Plot
plt.figure(figsize=(16, 6))
sns.set_style('whitegrid')


# Bar chart
plt.bar(df['Year'], df['Flood_Affected_Percent'], color='skyblue', edgecolor='black', label='Flood Affected (%)')

# Line chart over bars
plt.plot(df['Year'], df['Flood_Affected_Percent'], color='darkblue', linewidth=2.5, marker='o', label='Trend Line')

# Average line
plt.axhline(y=avg, color='red', linestyle='--', linewidth=1.5, label=f'Average ({avg:.1f}%)')

# Title and labels
plt.title("Flood Affected Area in Bangladesh (1954–2021)", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Flood Affected Area (%)", fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Save and show
plt.savefig("flood_combined_graph.png", dpi=300)
plt.show()
