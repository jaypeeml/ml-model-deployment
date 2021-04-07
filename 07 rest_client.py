import json
import requests

url = 'http://127.0.0.1:8000/model'

request_data = json.dumps({'model':'knn supervised machine learning model'})
response = requests.post(url,request_data)
print (response.text)



