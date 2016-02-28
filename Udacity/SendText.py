from twilio import rest

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACae36d77a0e942f6c40b3d1635507918d"
auth_token  = "1625a453610db2d71d75c769547830f3"
client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Hello, Friend?",
    to="+19729839981",    # Replace with your phone number
    from_="+14696191334") # Replace with your Twilio number
print message.sid