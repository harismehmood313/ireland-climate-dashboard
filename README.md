# Is Ireland Cutting Emissions as Fast as Europe? (1990–2024)

An interactive **Tableau** dashboard comparing Ireland's CO2 emissions with the EU-27, built for the MSc Data Analytics module *B9DA106 – Data Visualisation* at Dublin Business School.

![Dashboard preview](images/dashboard_preview.png)

## Key findings
| | Ireland | EU-27 |
|---|---|---|
| CO2 per person, 1990 | 9.4 t | 9.2 t |
| CO2 per person, 2024 | 6.3 t | 5.4 t |
| Change 1990 → 2024 | **-32%** | **-42%** |

- Ireland's CO2 per person **peaked at 12.3 t in 2001**, then fell sharply, but not as fast as the EU average.
- In 2024 Ireland ranks **6th highest of the 27 EU members** for CO2 per person.
- Total Irish CO2 is almost flat (32.9 → 33.3 Mt) while population grew from 3.5M to 5.3M.
- Coal fell from 14.7 to 1.9 Mt, while oil (12.3 → 18.7 Mt) and gas (4.4 → 10.3 Mt) rose.

## Dashboard features
- **4 linked sheets:** EU map, Top-N ranking, Ireland vs EU-27 trend line, fuel-mix area chart.
- **Parameters:** Select Country, Select Year, Select Metric (CO2 per person / GHG per person) and Top N.
- **Calculated fields:** per-person emissions (`SUM(co2) * 1,000,000 / SUM(population)`), metric switcher (`IF`), EU-27 labelling, selected-country highlight, year filter.
- **Dashboard actions:** click a country on the map or ranking to update the trend and fuel charts; hover highlight.
- Custom 1400 x 900 layout with clear titles, subtitles and sources.

## Data
Our World in Data – CO2 and Greenhouse Gas Emissions dataset (50,411 rows x 79 columns, 1750–2024), CC BY 4.0: https://github.com/owid/co2-data. Analysis uses 1990–2024. Regional aggregates (blank ISO code) are separate from countries; EU-27 is the benchmark.

## Repo contents
- `dashboard/Ireland_Climate_Dashboard.twbx` – packaged Tableau workbook
- `data/OWID_CO2_GHG_Emissions_Dataset.xlsx` – dataset used (unchanged)
- `analysis/key_figures.py` – reproduces the numbers above with pandas
- `images/dashboard_preview.png` – dashboard preview

## Tools
Tableau, Python (pandas), Excel.

*Author: Haris Mehmood – MSc Data Analytics, DBS Dublin.*
