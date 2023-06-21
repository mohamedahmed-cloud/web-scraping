from ReadUserNameLineFromCSV import ReadUserName
import requests

userName = ReadUserName()


all_user_repos = {}
def Info():
    global all_user_repos

    for i in userName:
        ourApi = f"https://api.github.com/users/{i}/repos"
        constant = len(f"https://github.com/{i}/")
        response = requests.get(ourApi)
        if response.status_code == 200:
            data = response.json()
            all_user_repos[i]={}
            count = 0
            for cnt in data:
                all_user_repos[i][count]=cnt["svn_url"][constant:]
                count += 1 

        else:
            print(f"{response.status_code}")

    return all_user_repos

    