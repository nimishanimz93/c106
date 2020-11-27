import os
import shutil

path = "/SourceFolder/"
dpath = "/DestFolder/"
if(os.path.exists(path)):
    # print("Exists!!!")
    files = os.listdir(path)
    # print(files)
    for file in files:
        splitArray = os.path.splitext(file)
        print(splitArray[1])
        if(splitArray[1]==".jpeg"):
            shutil.move(path+ splitArray[0]+splitArray[1],dpath+ splitArray[0]+splitArray[1])
else:
    print("Not Exists!!!")