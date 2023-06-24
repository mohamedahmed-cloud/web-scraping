res = []
def info():
    with open("data.txt", 'r') as file:
        data = file.read()
        return str(data)
    
def infoForWrite():
    with open("data.txt", "r") as file:
        for line in file:
            res.append(line.strip())

        return res
    