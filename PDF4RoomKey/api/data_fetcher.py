import csv
import json
import requests
from PDF4RoomKey.settings import BASE_API_URL,CLIENT_ID,CLIENT_SECRET
from datetime import datetime

class DataFetcher:
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key
    

    def get_arrivals(self, date):
        arrivals = self.api_request_arrivals(date)

        stripped_arrivals = []
        for arrival in arrivals['reservations']:
            stripped_arrival = {
                "id": arrival["id"],
                "lastName": arrival["primaryGuest"]["lastName"],
                "firstName": arrival["primaryGuest"]["firstName"],
                "corporateCode": arrival.get("corporateCode", ""),
                "arrival": arrival["arrival"],
                "departure": arrival["departure"],
                # "breakfast_included": arrival["rate"]["breakfastIncluded"]
            }
            # print(json.dumps(stripped_arrival, indent=4))
            stripped_arrivals.append(stripped_arrival)

        return stripped_arrivals

        
    def api_request_arrivals(self, date):
        url = self.api_url + "/booking/v1/reservations"
        params = {
            "unitGroupTypes": "BedRoom",
            "dateFilter": "Arrival",
            "from": f"{date}T00:00:00Z",
            "to": f"{date}T23:59:59Z"
        }
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(url, params=params, headers=headers)
        print(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'API request failed with status {response.status_code}')


    def fetch_data(self,date):
        # return self.get_arrivals(date) # --> ln 17, TypeError: list indices must be integers or slices, not str
        return [{'key': 'value'}]
        
    def write_to_csv(self,data,path):
        with open(path, "w", newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow()
            
    def write_to_json(self,data,path):
        with open(path, "w") as file:
            json.dump(data,file,indent=4)

    def generate(self,date,file,type):
        dataFetcher = DataFetcher(None,None) # DataFetcher(BASE_API_URL,??) 
        if type == 'csv':
            dataFetcher.write_to_csv([{'key': 'value'}],file)
        else:
            dataFetcher.write_to_json([{'key': 'value'}],file)

    def check_name_length(self,full_name):
        if(not full_name or len(full_name) > 40 or len(full_name) <= 0):
            raise ValueError("Invalid Name!")
        return True
    
    def check_dates(self,arrival,departure):
        if len(arrival) == 0:
            raise ValueError("Invalid Arrival Date!")
        
        if len(departure) == 0:
            raise ValueError("Invalid Departure Date!")
        
        arrival_date = datetime.strptime(arrival, '%Y-%m-%d')
        departure_date = datetime.strptime(departure, '%Y-%m-%d')

        if departure_date < arrival_date:
            raise ValueError("Invalid Dates!")

        return True 



