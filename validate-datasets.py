import csv

print("=== RTFP DATASET ===")
provinces = set()
years = set()
markets = set()
sample_rows = []

with open("IDN_RTFP_mkt_2007_2026-07-06 2.csv", "r") as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        provinces.add(row.get("adm1_name", ""))
        years.add(row.get("year", ""))
        markets.add(row.get("mkt_name", ""))
        if i < 3:
            sample_rows.append({
                "province": row.get("adm1_name"),
                "market": row.get("mkt_name"),
                "date": row.get("price_date"),
                "rice_price": row.get("c_rice"),
            })

print(f"Provinces: {len(provinces)}")
print(f"Markets: {len(markets)}")
print(f"Years: {min(years)} - {max(years)}")
print("Sample:")
for s in sample_rows:
    print(f"  {s}")

print()
print("=== WEATHER DATASET ===")
weather_provinces = set()
weather_years = set()
with open("weather-all-provinces-2010-2024.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        weather_provinces.add(row["province"])
        weather_years.add(row["year"])
print(f"Provinces: {len(weather_provinces)}")
print(f"Years: {min(weather_years)} - {max(weather_years)}")
print(f"Sample: {sorted(list(weather_provinces))[:5]}")

print()
print("=== PROVINCE NAME MATCHING ===")
rtfp_upper = {p.upper().strip() for p in provinces if p}
weather_upper = {p.upper().strip() for p in weather_provinces}
matched = rtfp_upper & weather_upper
only_rtfp = rtfp_upper - weather_upper
only_weather = weather_upper - rtfp_upper
print(f"Matched: {len(matched)}/{len(rtfp_upper)} RTFP provinces")
if only_rtfp:
    print(f"Only in RTFP (no weather): {sorted(only_rtfp)}")
if only_weather:
    print(f"Only in Weather (no price): {sorted(only_weather)}")

print()
print("=== YEAR OVERLAP ===")
rtfp_years = {int(y) for y in years if y.isdigit()}
weather_years_int = {int(y) for y in weather_years}
overlap_years = sorted(rtfp_years & weather_years_int)
print(f"Overlapping years: {overlap_years[0]} - {overlap_years[-1]} ({len(overlap_years)} years)")

print()
print("=== CONCLUSION ===")
if len(matched) >= 20 and len(overlap_years) >= 10:
    print("VALID - Datasets can be joined!")
    print(f"  {len(matched)} provinces matched")
    print(f"  {len(overlap_years)} years overlap (2010-2024)")
    print("  Join key: province + year + month")
else:
    print("PROBLEM - Check mismatches above")
