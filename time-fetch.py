import requests

url = 'http://worldtimeapi.org/api/timezone/Asia/Colombo'

x = requests.get(url)

print(x.json())