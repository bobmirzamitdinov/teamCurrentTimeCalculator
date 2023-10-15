# datetime module is used to handle date and time
from datetime import datetime
# tabulate package is used to format and print tabular data
from tabulate import tabulate
# pytz module is used to work with time zones
import pytz

# get_current_time function takes in the city name, country name and the time zone of the city and returns current time for each city
def get_current_time(city_name, country_name, time_zone):
    current_time = datetime.now(pytz.timezone(time_zone))
    current_date = current_time.strftime('%Y-%m-%d')
    current_day = current_time.strftime('%A')
    current_time = current_time.strftime('%H:%M:%S')
    return [city_name, country_name, current_date, current_day, current_time]

# cities dictionary contains the cities as keys and a nested dictionary as their corresponding values
if __name__ == "__main__":
    cities = {
        "Seoul": {"country": "South Korea", "timezone": "Asia/Seoul"},
        "Angren": {"country": "Uzbekistan", "timezone": "Asia/Tashkent"},
        "Tashkent": {"country": "Uzbekistan", "timezone": "Asia/Tashkent"},
        "Montreal": {"country": "Canada", "timezone": "America/Toronto"},
        "Chicago": {"country": "USA", "timezone": "America/Chicago"}
    }

    # loop through dictionary, retrieve date and time for each city and append to the list
    table = []
    for city, info in cities.items():
        table.append(get_current_time(city, info["country"], info["timezone"]))

    # print results in tabular format
    headers = ["City", "Country", "Current Date","Day of the Week","Current Time"]
    print(tabulate(table, headers, tablefmt="grid"))

