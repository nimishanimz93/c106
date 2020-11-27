import pandas as pd
import plotly.express as px


# data = [["x axis","y axis"],[1,2],[4,5],[1,5],[1,2],[3,4]]
# df = pd.DataFrame(data)

df = pd.read_csv("data.csv")

# print (df)

# fig = px.line(df, x="Year", y="Per capita income", color="Country",title="line graph")
# fig.show()

fig = px.scatter(df, x="Population",y="Per capita",size="Percentage",color="Country")
fig.show()