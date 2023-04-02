import csv
import pandas as pd
import plotly.express as px
import numpy as np

"""with open('coffee vs sleep.csv','r', encoding='utf-8') as f:
    frame2 = csv.DictReader(f)
    scatter2 = px.scatter(frame2, x='Coffee in ml', y='sleep in hours')
    #scatter2.show()"""

#print(frame)

def get_data_source(data):
    percentage = []
    daysPresent = []

    with open(data) as f:
        frame = csv.DictReader(f)
        for row in frame:
            percentage.append(float(row['Marks In Percentage']))
            daysPresent.append(float(row['Days Present']))

    return {'x':percentage, 'y':daysPresent}

def findCorelation(data):
    corelation = np.corrcoef(data['x'],data['y'])
    print("The corelation between student marks vs days present is",corelation[0,1])

def plotGraph(data):
    with open(data,'r',encoding='utf-8') as f:
        frame = csv.DictReader(f)
        scatter = px.scatter(frame,x='Marks In Percentage',y='Days Present')
        scatter.show()

temp_frame = 'Student Marks vs Days Present.csv'
data = get_data_source(temp_frame)
findCorelation(data)
plotGraph(temp_frame)

#print(data)