# get the file path.
from get_Content_no_lines import getnoLine

def extract_file_path(filePath):
    constant = "https://api.github.com/repos/"
    filePath = ("/".join(filePath[len(constant):].split("/")[3:]).split("?"))[0]
    numberOfLine = getnoLine(filePath)
    # print(filePath)
    
    return [filePath,numberOfLine]
    
# print(extract_file_path("https://api.github.com/repos/mohamedahmed-cloud/Github-follower/contents/.gitignore?ref=main"))
