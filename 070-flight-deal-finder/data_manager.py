import requests
from pprint import pprint

SHEETY_END_POINT = "https://api.sheety.co/<hidden>/flightDeals/prices"
bearer_headers = {"Authorization": "Bearer <hidden>"}
from_city = "MAA"

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_END_POINT, headers=bearer_headers)
        data = response.json()["prices"]
        self.destination_data = data
        print(self.destination_data)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            iata_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_END_POINT}/{city['id']}", json=iata_data, headers=bearer_headers)
            # pprint(response.text)
