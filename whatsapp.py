from twilio.rest import Client

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client()

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+12268993426'

with open('bee_movie_script.txt','r') as bee_movie:
    for line in bee_movie:
        for word in line.split():
           client.messages.create(body=word,
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
