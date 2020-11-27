import random

num =random.randrange(1,9)
i=0
while(i<5):
    i=i+1
    guessNum = input("Guess a number between 1 and 9--")
    if(int(guessNum)==num):
        print("You won")
        break
print("Number is ")
print(num)
