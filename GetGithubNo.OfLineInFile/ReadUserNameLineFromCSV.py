import csv
from collections import deque
from get_User_Name import finalResult
result = deque()
def ReadUserName():
    with open("user.csv",newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            result.append(row[0])
    return finalResult(result)
