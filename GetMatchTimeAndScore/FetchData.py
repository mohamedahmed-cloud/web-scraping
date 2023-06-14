import requests
from bs4 import BeautifulSoup

header = {'Accept-Charset':'utf-8'}

response = requests.get("https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date=6/14/2023#days" ,
                        headers = header)
def fetchData():
    if response.status_code == 200:
        data = response.content.decode('utf-8')
        soup = BeautifulSoup(data, 'lxml', from_encoding='utf-8')
        teamA = soup.find_all("div", {"class" : "teams teamA"})
        teamB = soup.find_all("div", {"class": "teams teamB"})
        score = soup.find_all("div", {"class": "MResult"})
    return [teamA, teamB, score]