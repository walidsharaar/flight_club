from manager import DataManager
from flight_search import  FlightSearch
from notification_manager import NotificationManager
from datetime import  datetime,timedelta

flight_search = FlightSearch()
data_manager= DataManager()
notification_manager = NotificationManager()
sheet_data = data_manager.get_distination_data()

ORIGIN_CITY_IATA = "BER"

# print(sheet_data)

#  5. In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the Flight Search API.
#  You should use the code you get back to update the sheet_data dictionary.+

if sheet_data[0]["iataCode"]=="":

    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data=sheet_data
    data_manager.update_destination_codes()
    # print(f"sheet_data:\n{sheet_data}")

tomorrow= datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now()+timedelta(days=(6*30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time = six_month_from_today
    )
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only{flight.price} to fly from"
                    f" {flight.origin_city}-{flight.origin_airport} to "
                    f"{flight.destination_city}-{flight.destination_airport}, "
                    f"from {flight.out_date} to {flight.return_date}.")

