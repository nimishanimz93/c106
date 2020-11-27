import pandas as pd
import plotly.express as px


df = pd.read_csv("marks.csv") # read csv using pandas

# print (df)

# fig = px.line(dataframe,x axis, y axis, divider,title="line graph")

fig = px.line(df, x="subject", y="marks",color="exam",title="line graph")
fig.show()

