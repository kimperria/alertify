from decouple import config
from twilio.rest import Client

account_sid = config("TWILIO_ACCOUNT_SID")
auth_token = config("TWILIO_AUTH_TOKEN")
phone_number = config("TWILLIO_PHONE_NUMBER")
client = Client(account_sid, auth_token)

body = "Ahoy Client! Your order has been successfully placed on Kimperria-Alertify services. Best: Admin, Kimperria"

message = client.messages.create(
    body=body, from_=phone_number, to="+254705651500"
)

print({"sid": message.sid, "status": message.status})
