import requests
from datetime import datetime, timedelta
from pprint import pprint

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "<hidden>"

api_headers = {"apikey": TEQUILA_API_KEY}

today = datetime.now()
days_to_search = 6 * 30
search_till = today + timedelta(days_to_search)
return_from = today + timedelta(7)
return_to = search_till + timedelta(7)
today_date = today.strftime('%d/%m/%Y')
search_till_date = search_till.strftime('%d/%m/%Y')
return_from_date = return_from.strftime('%d/%m/%Y')
return_to_date = return_to.strftime('%d/%m/%Y')


class FlightSearch:
    def get_destination_code(self, city_name):
        api_params = {
            "term": city_name,
            "location_types": "city",
        }
        response = requests.get(f"{TEQUILA_ENDPOINT}/locations/query", params=api_params, headers=api_headers)
        result = response.json()['locations']
        code = result[0]['code']
        # print(code)
        return code

    def search_fare(self, from_city, to_city):
        api_params = {
            "fly_from": from_city,
            "fly_to": to_city,
            "date_from": today_date,
            "date_to": search_till_date,
            "return_from": return_from_date,
            "return_to": return_to_date,
            "sort": "price",
            "curr": "USD",
            "limit": 1
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=api_params, headers=api_headers)
        results = response.json()['data']
        # pprint(results)
        for result in results:
            print(f"{to_city}, $ {result['price']}")
            return result['price']

