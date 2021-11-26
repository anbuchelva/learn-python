import requests
from flight_data import FlightData
from pprint import pprint

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "<hidden>"
API_HEADERS = {"apikey": TEQUILA_API_KEY}


class FlightSearch:
    def get_destination_code(self, city_name):
        api_params = {
            "term": city_name,
            "location_types": "city",
        }
        response = requests.get(f"{TEQUILA_ENDPOINT}/locations/query", params=api_params, headers=API_HEADERS)
        result = response.json()['locations']
        code = result[0]['code']
        # print(code)
        return code

    def check_flight_round_trip(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round", # round / oneway
            "one_for_city": 1,
            "max_stopovers": 1, # how many stops
            "curr": "USD",
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=query, headers=API_HEADERS)
        # pprint(response.json())
        try:
            results = response.json()["data"][0]
        except IndexError:
            pprint(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=results["price"],
            origin_city=results["cityFrom"],
            origin_airport=results["cityCodeFrom"],
            destination_city=results["cityTo"],
            destination_airport=results["cityCodeTo"],
            out_date=results["route"][0]["local_departure"].split("T")[0],
            return_date=results["route"][1]["local_departure"].split("T")[0],
            airlines=results["airlines"]
        )
        # print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data

    def check_flight_oneway_trip(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "flight_type": "oneway",
            "one_for_city": 1,
            "max_stopovers": 1, # how many stops
            "curr": "USD",
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=query, headers=API_HEADERS)
        # pprint(response.json())
        try:
            results = response.json()["data"][0]
        except IndexError:
            pprint(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=results["price"],
            origin_city=results["cityFrom"],
            origin_airport=results["cityCodeFrom"],
            destination_city=results["cityTo"],
            destination_airport=results["cityCodeTo"],
            out_date=results["route"][0]["local_departure"].split("T")[0],
            return_date="None",
            airlines=results["airlines"],
        )
        # print(f"{flight_data.destination_city}: ${flight_data.price}, Date:{flight_data.out_date}, Airlines:{flight_data.airlines}")
        return flight_data
