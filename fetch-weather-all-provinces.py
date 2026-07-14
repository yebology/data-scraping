"""
Fetch NASA POWER monthly weather data for all 34 Indonesian provinces.
Outputs: weather-all-provinces-2010-2024.csv

Parameters fetched:
- PRECTOTCORR: Curah hujan (mm/day)
- T2M: Suhu rata-rata (°C)
- T2M_MAX: Suhu maksimum (°C)
- T2M_MIN: Suhu minimum (°C)
- RH2M: Kelembapan relatif (%)
"""

import requests
import csv
import time
import sys

# 34 Provinces with capital city coordinates
PROVINCES = [
    {"province": "ACEH", "lat": 5.55, "lon": 95.32},
    {"province": "SUMATERA UTARA", "lat": 3.59, "lon": 98.67},
    {"province": "SUMATERA BARAT", "lat": -0.95, "lon": 100.35},
    {"province": "RIAU", "lat": 0.51, "lon": 101.45},
    {"province": "JAMBI", "lat": -1.61, "lon": 103.61},
    {"province": "SUMATERA SELATAN", "lat": -2.99, "lon": 104.76},
    {"province": "BENGKULU", "lat": -3.80, "lon": 102.26},
    {"province": "LAMPUNG", "lat": -5.45, "lon": 105.27},
    {"province": "KEPULAUAN BANGKA BELITUNG", "lat": -2.13, "lon": 106.14},
    {"province": "KEPULAUAN RIAU", "lat": 1.08, "lon": 104.03},
    {"province": "DKI JAKARTA", "lat": -6.21, "lon": 106.85},
    {"province": "JAWA BARAT", "lat": -6.91, "lon": 107.61},
    {"province": "JAWA TENGAH", "lat": -6.97, "lon": 110.42},
    {"province": "DI YOGYAKARTA", "lat": -7.80, "lon": 110.36},
    {"province": "JAWA TIMUR", "lat": -7.25, "lon": 112.75},
    {"province": "BANTEN", "lat": -6.12, "lon": 106.15},
    {"province": "BALI", "lat": -8.65, "lon": 115.22},
    {"province": "NUSA TENGGARA BARAT", "lat": -8.65, "lon": 116.32},
    {"province": "NUSA TENGGARA TIMUR", "lat": -10.18, "lon": 123.61},
    {"province": "KALIMANTAN BARAT", "lat": -0.03, "lon": 109.34},
    {"province": "KALIMANTAN TENGAH", "lat": -2.21, "lon": 113.92},
    {"province": "KALIMANTAN SELATAN", "lat": -3.32, "lon": 114.59},
    {"province": "KALIMANTAN TIMUR", "lat": -1.24, "lon": 116.83},
    {"province": "KALIMANTAN UTARA", "lat": 3.07, "lon": 116.04},
    {"province": "SULAWESI UTARA", "lat": 1.49, "lon": 124.84},
    {"province": "SULAWESI TENGAH", "lat": -0.90, "lon": 121.49},
    {"province": "SULAWESI SELATAN", "lat": -5.14, "lon": 119.42},
    {"province": "SULAWESI TENGGARA", "lat": -3.97, "lon": 122.51},
    {"province": "GORONTALO", "lat": 0.54, "lon": 123.06},
    {"province": "SULAWESI BARAT", "lat": -2.84, "lon": 119.23},
    {"province": "MALUKU", "lat": -3.66, "lon": 128.18},
    {"province": "MALUKU UTARA", "lat": 1.72, "lon": 127.81},
    {"province": "PAPUA", "lat": -2.54, "lon": 140.72},
    {"province": "PAPUA BARAT", "lat": -1.17, "lon": 134.09},
]

BASE_URL = "https://power.larc.nasa.gov/api/temporal/monthly/point"
PARAMETERS = "PRECTOTCORR,T2M,T2M_MAX,T2M_MIN,RH2M"
START_YEAR = 2010
END_YEAR = 2024

OUTPUT_FILE = "weather-all-provinces-2010-2024.csv"


def fetch_province_data(province_info):
    """Fetch monthly weather data for a single province."""
    params = {
        "parameters": PARAMETERS,
        "community": "AG",
        "longitude": province_info["lon"],
        "latitude": province_info["lat"],
        "start": START_YEAR,
        "end": END_YEAR,
        "format": "JSON",
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=60)
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        print(f"  ERROR fetching {province_info['province']}: {e}")
        return None


def parse_power_json(json_data, province_name):
    """Parse NASA POWER JSON response into rows."""
    rows = []
    parameters = json_data.get("properties", {}).get("parameter", {})

    months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",
              "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

    for param_name, yearly_data in parameters.items():
        for year_month_key, value in yearly_data.items():
            # Keys are like "202001" for Jan 2020, or "202013" for annual
            year = int(year_month_key[:4])
            month_num = int(year_month_key[4:])

            if month_num == 13:
                # Annual average, skip for now
                continue
            if month_num < 1 or month_num > 12:
                continue

            rows.append({
                "province": province_name,
                "year": year,
                "month": month_num,
                "month_name": months[month_num - 1],
                "parameter": param_name,
                "value": value if value != -999 else None,
            })

    return rows


def main():
    all_rows = []
    total = len(PROVINCES)

    print(f"Fetching weather data for {total} provinces (2010-2024)...")
    print(f"API: NASA POWER (power.larc.nasa.gov)")
    print("=" * 50)

    for i, prov in enumerate(PROVINCES, 1):
        print(f"[{i}/{total}] {prov['province']} (lat={prov['lat']}, lon={prov['lon']})...")
        data = fetch_province_data(prov)

        if data:
            rows = parse_power_json(data, prov["province"])
            all_rows.extend(rows)
            print(f"  -> {len(rows)} data points")
        else:
            print(f"  -> SKIPPED")

        # Rate limit: NASA POWER allows ~30 requests/minute
        if i < total:
            time.sleep(2)

    # Write CSV
    print("=" * 50)
    print(f"Writing {len(all_rows)} rows to {OUTPUT_FILE}...")

    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "province", "year", "month", "month_name", "parameter", "value"
        ])
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"Done! File saved: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
