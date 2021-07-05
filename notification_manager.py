from twilio.rest import Client

TWILIO_SID = "AC60595cef50f52688c7bdec2112342600"
TWILIO_AUTH_TOKEN = "27679bd08c4f419e5177c581afa8ad75"
TWILIO_VIRTUAL_NUMBER = "+15392860952"
TWILIO_VERIFIED_NUMBER = "Verified Number"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)