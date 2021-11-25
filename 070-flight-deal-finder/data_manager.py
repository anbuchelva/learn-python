import gspread
from gspread.models import Cell

# API Doc for Gspread: https://docs.gspread.org/en/latest/oauth2.html#enable-api-access-for-a-project
gc = gspread.service_account()
sh = gc.open("Flight Deals")
worksheet = sh.worksheet("prices")

from_city = "MAA"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        data = worksheet.get_all_records()
        self.destination_data = data
        # print(self.destination_data)
        return self.destination_data

    def update_destination_codes(self):
        iata_code = []
        i = 2
        for city in self.destination_data:
            value = city["IATA Code"]
            # print(value)
            iata_code.append(Cell(row=i, col=2, value=value))
            i += 1
            worksheet.update_cells(iata_code)

    def update_fair(self):
        fare = []
        i = 2
        for city in self.destination_data:
            value = city["Lowest Price"]
            print(value)
            fare.append(Cell(row=i, col=3, value=value))
            i += 1
            worksheet.update_cells(fare)
