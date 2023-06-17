import requests
import get_Access_Token
from get_File_Path import extract_file_path
from SharableData import repo, userName


github_link = f"https://api.github.com/repos/{userName}/{repo}/contents"
print(github_link)
# https://api.github.com/repos/mohamedahmed-cloud/Parking-system/contents
accessToken = get_Access_Token.getAcessToken()
header = {"Authorization": accessToken}

# Variable
result = []
parentName = []
parentUrl = []
file = []
cnt = 0
path = ""
# Logic
def dfs(url):
    global path
    cnt1 = 0

    for data in url:
        temp = data['download_url']
        if not temp:
            cnt1 = 1
            parentName.append(data['name'])
            parentUrl.append(data['url'])
            result.append(data['name'])
        else:
            file.append(extract_file_path(data['url']))

    if parentName and not cnt1:
            parentName.pop()
            parentUrl.pop()
      

    if not parentName:
        return file

    while parentUrl and parentUrl[-1] == 'Accessed.':
        parentUrl.pop()
        parentName.pop()
        
    url = requests.get(parentUrl[-1], headers = header)
    url = url.json()
    parentUrl[-1] = "Accessed."
    dfs(url)

    
    


    
response = requests.get(github_link, headers = header)
def getValue():
    if response.status_code == 200:
        data = response.json()
        dfs(data)
        return file

    else:
        return (f"Error {response.status_code}")



