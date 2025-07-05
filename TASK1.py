import requests
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

api_key = '30d4741c779ba94c470ca1f63045390a'

cities = []
invalid_cities = []
city_daily_avg = {}  

print("*Enter city names to get 5-day forecast.")
print("*Type 'done' when finished.\n")

while True:
    city = input("Enter city name (or type 'done'): ")
    if city.lower() == 'done':
        break
    cities.append(city)

for city in cities:
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if data.get('cod') == '404':
        print(f"❌ City '{city}' not found.")
        invalid_cities.append(city.title())
        continue

    forecast_list = data['list']
    temp_by_date = defaultdict(list)

    for entry in forecast_list:
        dt = entry['dt_txt']
        date_str = dt.split(" ")[0]  
        temp_by_date[date_str].append(entry["main"]["temp"])


    daily_avg = {date: round(sum(temps)/len(temps), 1) for date, temps in temp_by_date.items()}
    city_daily_avg[city.title()] = daily_avg


all_dates = sorted(set(date for city in city_daily_avg.values() for date in city))

if city_daily_avg:
    fig, ax = plt.subplots(figsize=(16, 6))

    x = np.arange(len(all_dates))  
    width = 0.8 / len(city_daily_avg)  

    for idx, (city, daily_data) in enumerate(city_daily_avg.items()):
        temps = [daily_data.get(date, 0) for date in all_dates]
        bar_positions = x + (idx * width)
        ax.bar(bar_positions, temps, width=width, label=city)

        
        for i, temp in enumerate(temps):
            ax.text(bar_positions[i], temp + 0.3, f"{temp}°C", ha='center', va='bottom', fontsize=8)

    ax.set_xticks(x + width * (len(city_daily_avg) - 1) / 2)
    ax.set_xticklabels(all_dates, rotation=45)
    ax.set_ylabel("Average Temperature (°C)")
    ax.set_title("5-Day Daily Avg Temperature per City")
    ax.legend(title="Cities")
    ax.grid(axis='y', linestyle='--', alpha=0.5)

    plt.tight_layout()

    
    plt.savefig("output.png")  
    plt.savefig("daily_avg_temp_grouped_bar_chart.png")  

    plt.show()

else:
    print("⚠️ No valid city data to display.")


if invalid_cities:
    print("\n🚫 These cities not found:")
    for c in invalid_cities:
        print(f" - {c}")
