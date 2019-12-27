from twilio.rest import Client

account_sid = 'AC9675774c558d61cc2e976a9b41774eab'
auth_token = 'b2a69d0fd224cc46483c23578d78d1b9'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+12186566664',
                     to='+16123239643'
                 )

print(message.sid)
