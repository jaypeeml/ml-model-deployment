## First run colab_rest_api.ipynb on colab
# copy the new external url generated here

import json
import requests

url = 'http://c3e95414bddb.ngrok.io/predict'

request_data = json.dumps({'age':47,'salary':40000})
response = requests.post(url,request_data)
print (response.text)



