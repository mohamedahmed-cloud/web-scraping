from prepareForWrite import data

newData = data()

print(newData)
with open('result.txt', 'w') as file:
    for i in newData:
        file.write(f"{i}\n")