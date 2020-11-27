f = open("sample.txt")


fileWords = f.read().split()

# fileLines = f.readlines()

# for i in fileLines:
#     print(i)


def checkFrequency(fileWords, word):
    wordCount=0
    print(fileWords)
    for i in fileWords:
        if(i==word):
            wordCount = wordCount+1
    print(wordCount)
    return wordCount
    

wc =checkFrequency(fileWords,"This")
fwrite = open("sample.txt","a")
fwrite.writelines("\n")
fwrite.writelines(str(wc))