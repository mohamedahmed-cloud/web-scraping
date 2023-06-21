from get_All_Folder_File_in_Directory import getValue
from PrepareHtmlContent import data
from WriteInHtml import writeInHtml
from RenderHtmlFile import render
from FilterUser import filterUser

arr = getValue(filterUser())
print(arr)
with open("marawany.txt", "w") as file:
    file.write(str(arr))
 
flag = 0

if arr == "Error 403":
    flag = 1

if not flag:
    print(arr)
    htmlPage = data(arr)
    writeInHtml(htmlPage)
    render()
else:
    print("Error 403")



