from get_All_Folder_File_in_Directory import getValue
from PrepareHtmlContent import data
from WriteInHtml import writeInHtml
from RenderHtmlFile import render
arr = getValue()
htmlPage = data(arr)
print(htmlPage)
writeInHtml(htmlPage)
render()




