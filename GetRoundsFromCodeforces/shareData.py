def lvalues(x):return list(map(int, input(x).split()))

def EnterYear():
    try:
        years = lvalues("please Enter which Year you want : ")
        return years
    except:
        return "please Enter a Number."
