data = [6,4,3,7,2]
size = len(data) #6

# Median for even numbers

if (size %2 == 1):
    print(data[int(size/2)])
else:
    x= (data[int(size/2)] + data[int(size/2 -1)])/2
    print(x)



