import pandas as pd
import plotly.express as px


# data = [["x axis","y axis"],[1,2],[4,5],[1,5],[1,2],[3,4]]
# df = pd.DataFrame(data)

df = pd.read_csv("marks.csv")

print (df)
fig = px.line(df, x="exam", y="marks", color="subject",title="line graph")
fig.show()

fig1 = px.bar(df, x="subject", y="marks",title="bar graph")
fig1.show()

fig2 = px.scatter(df, x="exam",y="marks",color="subject")
fig2.show()