import requests
import json

def send_sms(number,message):
    url = "https://www.sms4india.com/api/v1/sendCampaign"
    parameters={
        'apikey':"",
        'secret':"",
        'usetype':"stage",
        'phone': number,
        'message':message,
        'senderid':"SMSIND"
    }
    response = requests.get(url,params=parameters)
    dic = response.json
    print(dic)
    
send_sms("","")
