from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# sheet_data = [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}, {'city': 'Dallas', 'iataCode': 'DFW', 'id': 11}, {'city': 'Houston', 'iataCode': 'HOU', 'id': 12}, {'city': 'Austin', 'iataCode': 'AUS', 'id': 13}, {'city': 'Singapore', 'iataCode': 'SIN', 'id': 14}]
flight_search = FlightSearch()
ORIGIN_CITY_IATA = "LON"

# print(sheet_data)
# print(type(sheet_data))

if sheet_data[0]["IATA Code"] == "":
    for row in sheet_data:
        row["IATA Code"] = flight_search.get_destination_code(city_name=row["City"])

data_manager.destination_data = sheet_data
# print(sheet_data)
data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for row in sheet_data:
    flight = flight_search.check_flight(
        ORIGIN_CITY_IATA,
        row["IATA Code"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    # row["Lowest Price"] = flight_search.search_fare(from_city=from_city, to_city=row["IATA Code"])

# data_manager.destination_data = sheet_data
# data_manager.update_fair()

# flight_search.search_fare(from_city=from_city, to_city="LON")
