import pandas as pd
import matplotlib.pyplot as plt
#py flood_per_year.py
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



plt.figure(figsize=(16, 6))
plt.bar(df['Year'], df['Flood_Affected_Percent'], color='cornflowerblue')
plt.title("Year-wise Flood Affected Area in Bangladesh (% of Total Area)", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Flood Affected Area (%)")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("flood_bar_chart.png", dpi=300)  # For research paper use
plt.show()

plt.figure(figsize=(16, 6))
plt.plot(df['Year'], df['Flood_Affected_Percent'], marker='o', color='darkgreen')
plt.title("Trend of Flood Affected Area in Bangladesh", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Flood Affected Area (%)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("flood_line_chart.png", dpi=300)
plt.show()
