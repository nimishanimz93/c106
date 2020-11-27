import plotly_express as pty
import csv
import numpy as np

path = "./data/cups of coffee vs hours of sleep.csv"
coffee = []
sleep = []
with open(path, newline='') as csvfile:
    rows = csv.DictReader(csvfile)

    #iterator
    for row in rows:   
        # print(row['Coffee in ml'])
        coffee.append(float(row['Coffee in ml']))
        # print(coffee)
        sleep.append(float(row['sleep in hours']))
        # print(sleep)
    
corr = np.corrcoef(coffee,sleep)
print(corr[0,1])

    
fig = pty.scatter(x=coffee, y=sleep)
fig.show()





















#     for row in rows:
#         coffee.append(float(row["Coffee in ml"]))
#         sleep.append(float(row["sleep in hours"]))

# corr = np.corrcoef(coffee,sleep)

# print(corr[0,1])

# fig = pty.scatter(x=coffee, y=sleep)
# fig.show()

