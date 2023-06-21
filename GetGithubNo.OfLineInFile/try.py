from get_All_Folder_File_in_Directory import getValue
from PrepareHtmlContent import data
from WriteInHtml import writeInHtml
from RenderHtmlFile import render

arr = [{'Mohamed Yousef': [['.gitignore', 9], ['README.md', 6], ['Task-7/K%20Closest%20Points%20to%20Origin.cpp', 23], ['Task-7/Last%20Stone%20Weight.cpp', 26], ['Task-7/Library%20Fine.cpp', 30], ['Task-7/Lights%20Out.cpp', 35], ['Task-7/Merge%20Two%20Sorted%20Lists.cpp', 63], ['Task-7/Modified%20Kaprekar%20Numbers.cpp', 54], ['Task-7/Nested%20Lists.py', 20], ['Task-6/ACM%20ICPC%20Team.cpp', 41]]}
       , {'MuhammadSawalhy': [['.gitignore', 9], ['README.md', 6], ['Task-7/K%20Closest%20Points%20to%20Origin.cpp', 23], ['Task-7/Last%20Stone%20Weight.cpp', 26], ['Task-7/Library%20Fine.cpp', 30], ['Task-7/Lights%20Out.cpp', 35], ['Task-7/Merge%20Two%20Sorted%20Lists.cpp', 63], ['Task-7/Modified%20Kaprekar%20Numbers.cpp', 54], ['Task-7/Nested%20Lists.py', 20], ['Task-6/ACM%20ICPC%20Team.cpp', 41]]}]
print(arr)

htmlPage = data(arr)
# print(htmlPage)
writeInHtml(htmlPage)
render()