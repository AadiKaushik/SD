from typing import Mapping
import csv 

with open('C:/Users/aadi_/Desktop/coding/python/dataVisulation/data5.csv',newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)

data = fileData[0]

def mean(data):
    total = 0
    n = len(data)

    for x in data:
         total  += int(x)


    mean = total/n

    return(mean)

squaredList = []

for number in data :
    a = int(number) - mean(data)
    a= a**2
    squaredList.append(a)

sum = 0 

for i in squaredList:
    sum = sum + i

result = sum  / (len(data)-1)

import math 
SD = math.sqrt(result)
print(SD)

