import pandas as pd
import csv
import plotly.graph_objects as go
data=pd.read_csv ("data.csv")
print(data.groupby("level")["attempt"].mean())
fig=go.Figure(go.Bar(
    x=data.groupby("level")["attempt"].mean(), y=['level 1', 'Level 2', 'Level 3', 'Level 4'],orientation='h'
))
fig.show()