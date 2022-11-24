import requests
import json
import time

#UhRsPIqpSid5KcWrt0lARg ( TEST KEY FOR NODE ) ID : 665
def make_node():
    url = 'https://api.basecampserver.tech/nodes'
    headers = {'Content-Type': 'application/json'}
    data = {
    "name": "BananapiTEST", 
    "description": "Bananapi's Node",
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.status_code)
    print(response.text)

make_node()

#Post sensor data to node 
def post_sensor_data():
    url = 'https://api.basecampserver.tech/sensors?key=bKkUQatjtDu7fIwiOpl8uA'
    headers = {'Content-Type': 'application/json'}
    data = {
    "timestamp": 1,
    "temperature": 1,
    "humidity": 1,
    "pressure": 1,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.status_code)
    print(response.text)

def get_sensor_data():
  url = 'https://api.basecampserver.tech/sensors?node_id=444'
  headers = {'Content-Type': 'application/json'}
  response = requests.get(url, headers=headers)
  data = response.json()
  return data