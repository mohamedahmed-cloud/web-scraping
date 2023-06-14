import csv
from GetText import getText
from FetchData import fetchData
from getRows import getRows

# from fetch file - get the data
teamA, teamB, score = fetchData()

# convert html text to text
teamA = getText(teamA)
score = getText(score)
teamB = getText(teamB)

# get the list of teamA[i], teamB[i], score[i]
rows = getRows(teamA, score, teamB)
tableHead = ["الفريق الاول", "الفريق الثاني", "مي   عاد المبارة", "النتيجة"]

# write in the file.
with open('save.csv', 'w', newline = '',encoding = 'utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(tableHead)
    writer.writerows(rows)



