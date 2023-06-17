import requests
from SharableData import userName, repo

# https://api.github.com/repos/mohamedahmed-cloud/Github-follower/contents

api = f"https://raw.githubusercontent.com/{userName}/{repo}/main/"
def getnoLine(url):
    global api
    data1 = f"{api}{url}"
    print(data1)
    response = requests.get(data1)
    if response.status_code == 200:
        try:
            data = response.content.decode('utf-8')
            lines = len(data.split('\n'))
            return lines
        except:
            return "File didn't Open"
    else:
        return f"{response.status_code} Status Error"

