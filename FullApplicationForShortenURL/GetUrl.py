import re
from Read import info
def getUrl():
    text = info()

    pattern = re.compile(r"https?://\S+")
    Url = re.findall(pattern, text)
    return Url


