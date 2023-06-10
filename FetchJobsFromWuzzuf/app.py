import requests
from bs4 import BeautifulSoup
import csv


# instead of print
import WriteInFile
jobTitleArr = []
companyNameArr = []
companyLocationsArr = []
jobSkillsArr = []
all = []    
links = []

response = requests.get("https://wuzzuf.net/search/jobs/?a=spbg&q=python")
data = response.content

soup = BeautifulSoup(data, 'lxml')

WriteInFile.writeInFile(str(soup))
# we need to find job title, job skills, company name, location name, responsibility

jobTitle  = soup.find_all("h2", {"class":"css-m604qf"})
companyName = soup.find_all("a", {'class': "css-17s97q8"})
companyLocations = soup.find_all("span", {"class": "css-5wys0k"})
jobSkills = soup.find_all("div", {"class": "css-y4udm8"})

# print(jobSkills)
def getText(mainResponse):
    arr = []
    for i in mainResponse:
        arr.append(i.text)
    return arr
def getLinks (mainResponse):
    arr = []
    for i in mainResponse:
        arr.append("https://wuzzuf.net"+i.find("a").attrs['href'])
    return arr

jobTitleArr = getText(jobTitle)
companyNameArr = getText(companyName)
companyLocationsArr = getText(companyLocations)
jobSkillsArr = getText(jobSkills)

links = getLinks(jobTitle)

# print("get Salaray ")





row = ["Job Title", "Company Name", "Company Location", "job Skills", 'links', ]



for i in range(len(jobSkillsArr)):
    all.append([jobTitleArr[i], companyNameArr[i], companyLocationsArr[i], jobSkillsArr[i],links[i]])




# write in to csv
with open('save.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(row)
    writer.writerows(all)

