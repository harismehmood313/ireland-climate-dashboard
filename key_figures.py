"""Reproduces the headline numbers quoted in the README.
Usage: python key_figures.py ../data/OWID_CO2_GHG_Emissions_Dataset.xlsx
Data: Our World in Data CO2 & GHG dataset (CC BY 4.0), https://github.com/owid/co2-data
"""
import sys
import pandas as pd

df = pd.read_excel(sys.argv[1], sheet_name="Data")
df = df[(df.year >= 1990) & (df.year <= 2024)]
df["co2_pp"] = df.co2 * 1e6 / df.population  # tonnes per person (same formula as the Tableau calculated field)
ie = df[df.country == "Ireland"].set_index("year")
eu = df[df.country == "European Union (27)"].set_index("year")
peak_year = ie.co2_pp.idxmax()
print(f"Ireland CO2/person: 1990 {ie.co2_pp[1990]:.1f}t | peak {peak_year} {ie.co2_pp[peak_year]:.1f}t | 2024 {ie.co2_pp[2024]:.1f}t")
print(f"EU-27 CO2/person:   1990 {eu.co2_pp[1990]:.1f}t | 2024 {eu.co2_pp[2024]:.1f}t")
print(f"Change 1990-2024: Ireland {ie.co2_pp[2024]/ie.co2_pp[1990]-1:.0%} | EU-27 {eu.co2_pp[2024]/eu.co2_pp[1990]-1:.0%}")
print(f"Ireland total CO2 (Mt): 1990 {ie.co2[1990]:.1f} -> 2024 {ie.co2[2024]:.1f}; population {ie.population[1990]/1e6:.1f}M -> {ie.population[2024]/1e6:.1f}M")
for fuel in ["coal_co2", "oil_co2", "gas_co2"]:
    print(f"  {fuel}: {ie[fuel][1990]:.1f} -> {ie[fuel][2024]:.1f} Mt")
