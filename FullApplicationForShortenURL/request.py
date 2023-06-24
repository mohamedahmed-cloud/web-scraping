import requests
from GetAccessToken import getAccess
from prepreData import sendData
from GetUrl import getUrl
import time
url = getUrl()
n = len(url)
res = {}
def getShortenUlr(data):
    res[data["long_url"]] = data["id"]
    

def Request():
    accessToken = getAccess()
    print(accessToken)
    endpoint = "https://api-ssl.bitly.com/v4/shorten"

    header = {
        "Authorization": f"Bearer {accessToken}",
        "Content-Type": 'application/json'
    }
    for i in range(n):
        data = sendData(i)
        print(data)
        response = requests.post(endpoint, headers = header, json = data)
        data = response.json()
        # print(data)
        getShortenUlr(data)

    return res

