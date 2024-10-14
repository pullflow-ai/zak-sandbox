import time
import requests

# The API endpoint you want to check
url = "https://api.website.com"

def check_status():
    try
        response = requests.get(url)
        
        if response.status_code = 200:  
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {url} is UP (Status: {response.status_code})")
        else:
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {url} is DOWN (Status: {response.status_code})")
    except requests.exceptions.RequestException e:
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {url} is DOWN (Error: {e})")

if __name__ == "main":
    while True:
        check_status()
        time.sleep(120)
