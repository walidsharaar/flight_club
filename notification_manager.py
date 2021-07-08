from twilio.rest import Client
import smtplib

TWILIO_SID = "AC60595cef50f52688c7bdec2112342600"
TWILIO_AUTH_TOKEN = "27679bd08c4f419e5177c581afa8ad75"
TWILIO_VIRTUAL_NUMBER = "+15392860952"
TWILIO_VERIFIED_NUMBER = "Verified Number"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "mmytest779@gmail.com"
MY_PASSWORD = "1234567@abc%$"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8'))