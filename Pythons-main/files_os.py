import os
import shutil
# print(os.system("time"))
# print(os.getpid())
path = "C:/Users/user/Downloads/tower-siege-1-main/tower-siege-1-main/ball.js"
if(os.path.exists(path)):
    print("Exists!")
    shutil.move(path,"C:/Users/user/Downloads/tower-siege-1-main/tower-siege-1-main/balldupe.js")
    # splits = os.path.splitext(path)
    # print(splits[0])
    # print(splits[1])
else:
    print("no Exists!")
