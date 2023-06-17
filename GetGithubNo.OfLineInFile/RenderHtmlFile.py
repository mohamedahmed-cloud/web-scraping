import webbrowser as web
import sys
def render():
    firstPart = sys.argv[0].split("/")
    firstPart = "/".join(firstPart[:-1])
    fileName = f"{firstPart}/index.html"

    print(fileName)
    web.open(fileName)