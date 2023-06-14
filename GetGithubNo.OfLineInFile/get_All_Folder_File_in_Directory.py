import requests
import get_Access_Token
repo = "alx-low_level_programming"
user = "mohamedahmed-cloud"
github_link = f"https://api.github.com/repos/{user}/{repo}/contents"
#  https://api.github.com/repos/mohamedahmed-cloud/alx-low_level_programming/contents
accessToken = get_Access_Token.getAcessToken()
header = {"Authorization": accessToken}
# didn't complete yet

# dfs function
result = []
parentName = []
parentUrl = []
file = []
cnt = 0
def dfs(url):
    cnt1 = 0
    for data in url:
        temp = data['download_url']
        if not temp:
            cnt1 += 1
            parentName.append(data['name'])
            parentUrl.append(data['url'])
            result.append(data['name'])
        else:
            file.append(data['name'])
    if not cnt1:
        parentName.pop()
        parentUrl.pop()

    if not parentName:
        return

    while parentUrl[-1] == 'Accessed':
        parentUrl.pop()
        parentName.pop()
        
    url = requests.get(parentUrl[-1], headers = header)
    url = url.json()
    print("This is the parent Name",parentName[-1])
    parentUrl[-1] = "Accessed."
    print("This is the parent current Url",parentUrl[-1])
    print("This is the file",file)
    dfs(url)

    
    


    
response = requests.get(github_link, headers = header)
if response.status_code == 200:
    data = response.json()
    dfs(data)
    print(result)
    print(file)

else:
    print(f"Error {response.status_code}")



