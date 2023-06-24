from GetUrl import getUrl
url = getUrl()

data = {}
key = "fms"
def sendData(i):
    data["long_url"] = url[i]
    return data

# sendData()
# print(data)