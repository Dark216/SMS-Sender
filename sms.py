import requests
import json

def send_sms(number,message):
    url = "https://www.sms4india.com/api/v1/sendCampaign"
    parameters={
        'apikey':"YGMTHBTWODO1I1JASBXLVMA61BLVJAEW",
        'secret':"8PZAMP5V4T50ZIK3",
        'usetype':"stage",
        'phone': number,
        'message':message,
        'senderid':"SMSIND"
    }
    response = requests.get(url,params=parameters)
    dic = response.json
    print(dic)
    
send_sms("8895820008","Binayak Panda stay safe from corona virus,take preventive measures and obey lockdown. Stay safe and stay healthy")