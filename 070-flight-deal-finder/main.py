from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()
ORIGIN_CITY_IATA = "MAA"

if sheet_data[0]["IATA Code"] == "":
    for row in sheet_data:
        row["IATA Code"] = flight_search.get_destination_code(city_name=row["City"])

data_manager.destination_data = sheet_data
# print(sheet_data)
data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for row in sheet_data:
    flight = flight_search.check_flight_round_trip(
        ORIGIN_CITY_IATA,
        row["IATA Code"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    # print(row["IATA Code"])
    # print(f"To: {flight.destination_city} for ${flight.price}")
    # print(f"City: {row['City']}, Lowest Price: {row['Lowest Price']}, Price: {flight.price}")
    if flight is not None:
        if flight.price < row["Lowest Price"]:
            message = f"*Low Price Alert!*\n" \
                      f"Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to " \
                      f"{flight.destination_city}-{flight.destination_airport} from {flight.out_date} to " \
                      f"{flight.return_date} in {flight.airlines} Airlines."
            # print(message)
            notification_manager.alert(message)
        else:
            print(f"City: {row['City']}, Lowest Price: {row['Lowest Price']}, Price: {flight.price}")
