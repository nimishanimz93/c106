from collections import Counter

data = [1,1,1,1,1,1,1]
numbers = [1,7,3,4,5,6,7,8,4,5,6,7,8]

x = Counter(numbers)

max=0
pos=0

for i in x:
    if(x[i]>max):
        max=x[i]
        pos=i
print(pos)



