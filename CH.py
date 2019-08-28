#import module
import requests
import csv
import math

#create file
csvfile = open('file.csv', 'w')

#create csv writer
csvwriter = csv.writer(csvfile, delimiter = ',')
 
#write information
csvwriter.writerow(['Date', 'Temperature'])

# Import requests
import requests
import json

url = "https://maps.googleapis.com/maps/api/geocode/json"
key = 'AIzaSyAwPHH9ZDTZHdkXRAPp-CI59U23S9OhSPY'
address = input("Enter an address")
payload = {'key':'', 'address': address}

# Make a request
r = requests.get(url, params=payload)

#process data
data = r.json()

#print(data)
location = data['results'][0]
geometry = location['geometry']['location']

#print(location.keys())
print("You are at %s." % location['formatted_address'])
print("Your latitiude is %s and your longitude is %s." % (geometry['lat'], geometry['lng']))

lat = str(geometry['lat'])
lon = str(geometry['lng'])

#creating url for requests

endpoint = 'https://api.darksky.net/forecast/'
key1 = '251cb187f7056e08ba336253030a291a'
payload1 = {'units': 'us'}
YYYY = int(input("pick a year"))

#Creating lists for Months and Days
Months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

Days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28']

#For every day in every month in a specified year writes temperature to a csv file
for MM in Months:
    for DD in Days:
        time = str(YYYY) + "-" + str(MM) + "-" + str(DD) + "T24:00:00Z"
    
        # Assemble full url
        url1 = endpoint + key1 + '/' + lat + ',' + lon + ',' + time
    
        # Make a request
        r1 = requests.get(url1, params=payload1)
        #print(url1)

        # deal with the information
        weather = r1.json()
        #print(weather)
    
        # Writes every temperature for every hour in terms of UNIX time
        for x in range(0, 23):
            # writes hour
            hour = weather['hourly']['data'][x]['time']
            print(hour)
            #Writes temperature into csv file
            Temperature = weather['hourly']['data'][x]['temperature']
            csvwriter.writerow([hour, Temperature])
#close writer
csvfile.close()

#importing modules
import bokeh

import pandas as pd
import numpy as np

from bokeh.charts import Scatter, output_file, save
from bokeh.charts import HeatMap, output_file, save
from bokeh.layouts import gridplot
from bokeh.plotting import figure, save, output_file

#read file
df = pd.read_csv('file.csv')

#Plots a heatmap
p = HeatMap(df, x='Date', y='Temperature', values=None, stat='count', xgrid=False, ygrid=False, hover_tool=True, hover_text='Temperature', plot_width=2000, plot_height=1000)

output_file('HeatMap.html')

#Saves graph
save(p)

#box = BoxPlot(df, values='Temperature', label='Date', title="Temperature Date Box Plot", plot_width=400)

#Creates a Scatter Plot
v = Scatter(df, x='Date', y='Temperature', color='red', title="Date vs. Temperature", legend='top_right', xlabel="Date", ylabel="Temperature", plot_width=2000, plot_height=1000)

output_file('Scatter.html')

#Saves Graph as a html file
save(v)

#Creates array for Temperature
Temperatures = np.array(df['Temperature'])

#Creates array for Date
dates = df['Date']

#Creating Graph
p2 = figure(title="Temperature vs Date")
p2.grid.grid_line_alpha = 0
p2.xaxis.axis_label = 'Date'
p2.yaxis.axis_label = 'Temperature'
p2.ygrid.band_fill_color = "olive"
p2.ygrid.band_fill_alpha = 0.1

#Creating dots for data points
p2.circle(dates, Temperatures, size=4, legend='Individual Temperatures', color='darkgrey', alpha=0.2)

#Line for graph and define legend
p2.line(dates, Temperatures, legend='avg', color='navy')
p2.legend.location = "top_left"

output_file("Temp.html", title="Temp.py example")

#Saving graph with proper dimensions
save(gridplot([[p2]], plot_width=2000, plot_height=1000))