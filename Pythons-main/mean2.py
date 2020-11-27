import csv
from collections import Counter

with open("marks.csv", newline='') as f:
    reader = csv.reader(f)
    dataList = list(reader)

dataList.pop(0)

total=0

marks = []

for i in dataList:
    # print(i[1])
    marks.append(int(i[1]))
    total= total + int(i[1])

print("MEAN",total/len(dataList))

marks.sort()

n = len(marks)

if n%2 == 0:
    print(marks[int(n/2 -1)])
else:
    print(marks[int(n/2)])





