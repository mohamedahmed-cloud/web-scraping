# there are a problem in the page of the jobs details I didn't know why.
# the content in the page can't accessed by this way.
import requests
from bs4 import BeautifulSoup

url = "https://wuzzuf.net/jobs/p/PzqywNmk5NoT-Senior-Odoo-Python-Developer-Ulemt-Cairo-Egypt?o=1&l=sp&t=sj&a=python|search-v3|spbg"
response = requests.get(url)
data = response.content
soup = BeautifulSoup(data, 'lxml')
salary = soup.find("span", {"class" : "css-4xky9y"})
print(salary.text)
