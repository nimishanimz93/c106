import os
import shutil

spath = "/SourceFolder/"
dpath = "/DestFolder/"

if(os.path.exists(spath)):
    files = os.listdir(spath)
    for file in files:
        splits = os.path.splitext(file)
        if (splits[1] == ".jpeg"):
            print(splits[0])
            shutil.move(spath+splits[0]+splits[1], dpath+splits[0]+splits[1])
else:
    print("no Exists!")


