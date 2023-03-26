import requests
import os 
headers = {
    "Content-Type": "application/json"
}
url = f"https://api.telegram.org/bot{os.getenv('TOKEN')}/sendMessage"
data = {
    "text": "WOOOOORK",
    "chat_id": 319466828
}

r = requests.post(url, json=data, headers=headers)
print(r.json())