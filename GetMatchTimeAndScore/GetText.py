from collections import deque
def getText(arr):
    ans = deque()
    for i in arr:
        i = i.text.strip().replace('\n' , "%")
        temp = i.split("%")
        print(temp)
        for i in range(len(temp)):
            if i in [0,2] and temp[i] == "-":
                temp[i] = '0'
        ans.append(temp)
        

    return ans