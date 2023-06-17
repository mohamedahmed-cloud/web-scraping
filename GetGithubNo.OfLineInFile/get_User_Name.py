
userAccount = []
userName = []
const = "https://github.com/"

with open("data.txt", 'r') as f:
    data = f.read()
    userAccount.append(data)

userAccount = userAccount[0].split("\n")

if not userAccount[-1]:
    userAccount = userAccount[:-1]

def finalResult():
    for i in userAccount:
        user = ""
        for j in i[len(const):]:
            if j !="/":
                user += j
            else:break
        userName.append(user)
    print(userName)
    return userName

# finalResult()