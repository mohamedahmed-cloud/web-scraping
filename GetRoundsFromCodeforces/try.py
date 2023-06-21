# import requests

# year = 2022 # replace with the year you want to retrieve contests for
# header =
# header = {"Authorization":header}
# response = requests.get(url)
# data = response.json()

# if data.get('status') == 'OK':
#     contests = data['result']
#     for contest in contests:
#         if contest['phase'] == 'FINISHED' and contest['startTimeSeconds'] // 31536000 == year - 1970:
#             print(contest,f"https://codeforces.com/contest/{contest['id']}")
# else:
#     print(f"Error: {data.get('comment')}")