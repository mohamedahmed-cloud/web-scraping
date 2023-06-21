import requests
from getHeaders import getHeader
def request(years):
    header = getHeader()
    result = []
    url = "https://codeforces.com/api/contest.list?gym=false"
    response = requests.get(url ,headers = header)
    data = response.json()
    if data['status'] == "OK":
        contests = data['result']
        secondInYear = 365 * 24 * 60 * 60
        for contest in contests:
            if contest['phase'] == 'FINISHED' and (contest["startTimeSeconds"] // secondInYear) in years:
                result.append([f"({contest['name'].split('(')[-1]}", f"https://codeforces.com/contest/{contest['id']}"])

        return result
    
    else:

        data = response.json()

