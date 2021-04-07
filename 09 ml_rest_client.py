import json
import requests

url = 'http://127.0.0.1:8005/model'

request_data = json.dumps({'age':45,'salary':35000})
response = requests.post(url,request_data)
print (response.text)



