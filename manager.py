import requests


SHEETY_PRICE_ENDPPOINT= "https://api.sheety.co/0a9f127e197081af144d45ebf7e54d3e/flightDeals/prices"


class DataManager:
    def __int__(self):
        self.destination_data={}

    def get_distination_data(self):
        #get all the data into the sheet using Sheety API
        response = requests.get(url=SHEETY_PRICE_ENDPPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data


    def update_destination_codes(self):
        for city in self.destination_data:
            new_data={
                "price":{
                    "iataCode":city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICE_ENDPPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)