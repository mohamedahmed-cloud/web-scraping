userName = []
const = "https://github.com/"

def finalResult(userAccount):
    global const
    for i in userAccount:
        user = ""
        for j in i[len(const):]:
            if j !="/":
                user += j
            else:break
        userName.append(user)

    return userName

# print(finalResult(["https://github.com/mohamedahmed-cloud","https://github.com/abdabdii"]))