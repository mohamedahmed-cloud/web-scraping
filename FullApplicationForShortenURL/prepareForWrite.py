from Read import infoForWrite
from request import Request
from collections import deque

oldData = infoForWrite()
oldList = deque()
link = Request()

for i in oldData:
    oldList.append(i)

n = len(oldList)
print(link)
def data():
    for key, value in link.items():
        for i in range(n):
            if oldList[i] == key:
                oldList[i] = value
    return oldList



