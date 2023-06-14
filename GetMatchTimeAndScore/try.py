import requests
from bs4 import BeautifulSoup
import csv

# set the headers to indicate that we want to receive UTF-8 encoded content
headers = {'Accept-Charset': 'utf-8'}

# make the request and pass in the headers
response = requests.get("https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date=6/14/2023#days", headers=headers)

if response.status_code == 200:
    # decode the content using UTF-8 encoding
    data = response.content.decode('utf-8')
    soup = BeautifulSoup(data, 'lxml')
    teamA = soup.find_all("div", {"class" : "teams teamA"})
    teamB = soup.find_all("div", {"class": "teams teamB"})
    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        for i in range(len(teamA)):
            print(teamA[i].text.strip())
            print(teamB[i].text.strip())
            csvwriter.writerow([teamA[i].text.strip(), teamB[i].text.strip()])