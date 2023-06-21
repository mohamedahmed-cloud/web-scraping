#!/usr/bin/python3
from shareData import EnterYear
from request import request
from allowedYears import allowedYears
import csv

year = EnterYear()
years = allowedYears(year)


data = request(years)

print("Number of contest is ",len(data))

with open("result.csv", "w") as file:
    write = csv.writer(file)
    write.writerow([ "عليه أفضل الصلاة والسلام",'صلى على أفضل خلق الله'])
    write.writerow(["No.Of Div", "Div Link"])
    write.writerows(data)

    