import pandas as pd
import plotly
import plotly.graph_objs as go


#Read cars data from csv
data = pd.read_csv("PISA2015-cleaned.csv")

#Set marker properties
markercolor = data['Proportion of ISCED Level 5a Teachers']


#Make Plotly figure
fig1 = go.Scatter3d(x=data['Math Score'],
                    y=data['Reading Score'],
                    z=data['Student-Teacher Ratio'],
                    marker=dict(color=markercolor,
                                opacity=1,
                                reversescale=True,
                                colorscale='Blues',
                                size=5, autocolorscale=True,
                                showscale=True),
                    line=dict (width=0.02),
                    mode='markers',
                    showlegend=True,
                    name="Proportion of ISCED Level 5a Teachers",
                    textposition="top right")

#Make Plot.ly Layout
mylayout = go.Layout(title="FACTORS INFLUENCING STUDENT SCORES", 
                    scene=dict(xaxis=dict(title="Math Score"),
                    yaxis=dict(title="Reading Score"),
                    zaxis=dict(title="Student-Teacher Ratio")))

#Plot and save html
plotly.offline.plot({"data": [fig1],
                     "layout": mylayout},
                     auto_open=True,
                     filename=("4DPlot.html"))