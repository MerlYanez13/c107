import pandas as pd
import csv
import plotly.graph_objects as go
df=pd.read_csv ("data.csv")
data=df.loc[df['student_id']=="TRL_987"]
print(data.groupby("level")["attempt"].mean())
fig=go.Figure(go.Bar(
    x=data.groupby("level")["attempt"].mean(), y=['level 1', 'Level 2', 'Level 3', 'Level 4'],orientation='h'
))
fig.show()