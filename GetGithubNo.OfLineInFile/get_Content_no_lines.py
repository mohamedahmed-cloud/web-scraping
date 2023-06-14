import requests
# get number of line for specific file
repo = "Github-follower"
url = f"https://api.github.com/repos/mohamedahmed-cloud/{repo}/contents"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    data1 = data['download_url']
    print(data1)
    response = requests.get(data1)
    if response.status_code == 200:
        data = response.content.decode('utf-8')
        lines = len(data.split('\n'))
        print(f"Number of lines : {lines}" )
    else:
        print(f"Error : {response.status_code}")

else:
    print(f"Error : {response.status_code}")