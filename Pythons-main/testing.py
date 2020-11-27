message = input("Enter message")
charCount=0
wordCount =1
for i in message:
    charCount=charCount+1
    print(i+str(charCount))
    if(i==" "):
        wordCount=wordCount+1
print("Word count" + str(wordCount))



