import requests

BASE = "http://127.0.0.1:5000" 

# response = requests.post(BASE + "/video/1", {"name": "Pog Video", "views": 10000, "likes": 10})
# print(response.json())

# response = requests.post(BASE + "/video/2", {"name": "Basketball Video", "views": 10000000, "likes": 1000})
# print(response.json())

# response = requests.post(BASE + "/video/5", {"name": "Boxing Video", "views": 200, "likes": 32})
# print(response.json())

response = requests.get(BASE + "/video/2")
print(response.json())


