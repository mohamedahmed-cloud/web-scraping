import get_User_Name 
import time
import requests
import get_Access_Token

# get the all repo from github
userName = get_User_Name.finalResult()
accessToken = get_Access_Token.getAcessToken()

header = {"Authorization": accessToken}

print(userName)
all_user_repos = {}
for i in userName:
    ourApi = f"https://api.github.com/users/{i}/repos"
    constant = len(f"https://github.com/{i}/")
    response = requests.get(ourApi, headers=header)
    
    if response.status_code == 200:
        data = response.json()
        all_user_repos[i]={}
        count = 0
        for cnt in data:
            all_user_repos[i][count]=cnt["svn_url"][constant:]
            count += 1 

        time.sleep(1)
    else:
        print("There is a response Error in the code.")
for i in all_user_repos:
    count = 1
    print(f"The Repos for the {i} is :")
    for j in all_user_repos[i].values():
        print("  ",count," => ", j)
        count += 1


    