from collections import Counter
numbers = [1,2,3,4,5,6,7,8,4,5,6,7,8,6]

print(Counter(numbers))
z = Counter(numbers)

max = 0

for p in z:
    if z[p]> max:
        max = z[p]

for p in z:
    if z[p]== max:
        print(p)

