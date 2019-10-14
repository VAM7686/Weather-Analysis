#import module
import csv
import math

# Import requests
import requests
import json

from datetime import timedelta, date, datetime

def location_finder():
    url_map = "https://maps.googleapis.com/maps/api/geocode/json"
    key = 'AIzaSyDx9EfTE_4cPsE9ihJjmqR319U5LhzpvPk'
    address = input("Enter an address")
    print(address)
    payload = {'key': key, 'address': address}

    # Make a request
    r = requests.get(url_map, params=payload)

    #print(r)

    #process data
    data = r.json()

    #print(data)
    location = data['results'][0]
    geometry = location['geometry']['location']

    #print(location.keys())
    print("You are at %s." % location['formatted_address'])
    print("Your latitiude is %s and your longitude is %s." % (geometry['lat'], geometry['lng']))

    #Storing latitude and longitudes
    global lat
    global lon
    lat = str(geometry['lat'])
    lon = str(geometry['lng'])

location_finder()

#option to switch location
while True:
    retry = input("Would you like to pick another location? Enter y or n")
    
    if ((retry != 'y') and (retry != 'n') and (retry != 'Y') and (retry != 'N')):
        print("Invalid entry. Enter y or n")
        continue
    elif ((retry == 'y') or (retry == 'Y')):
        location_finder()
    else:
        break


#creating url for requests
endpoint = 'https://api.darksky.net/forecast/'
key1 = '251cb187f7056e08ba336253030a291a' 
payload1 = {'units': 'us'}

#Creating lists for Months and Days
Months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

Days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28']


today = date.today()
today_year = today.year
today_month = today.month
today_day = today.day

#Input for year and verifies if valid year
YYYY = int(input("pick a year"))
while True:
    if ((today_year < YYYY ) or (YYYY < 1971)):
        print("Enter a valid year before " + str(today_year) + ", and after 1971")
        YYYY = int(input("pick a year"))
    else:
        break

#creates date range function to calculate how many days are in range
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

#Creates files
csvfilehourly = open('hourly'+str(YYYY)+'.csv', 'w')
csvfiledaily = open('daily'+str(YYYY)+'.csv', 'w')


#create csv writers
csvwriterhourly = csv.writer(csvfilehourly, delimiter = ',')
csvwriterdaily = csv.writer(csvfiledaily, delimiter = ',')

 
#write information to files
csvwriterhourly.writerow(['Time', 'Summary', 'Icon', 'Precipitation Intensity', 
    'Precipitation Probability', 'Temperature', 'Apparent Temperature', 'Dew Point', 
    'Humidity', 'Pressure', 'Wind Speed', 'Wind Gust', 'Wind Bearing', 'Cloud Cover', 
    'UV Index', 'Visibility']) 
csvwriterdaily.writerow(['Time', 'Summary', 'Icon', 'Sunrise Time', 'Sunset Time', 
    'Moon Phase', 'Precipitation Intensity Max', 'Precipitation Intensity Max Time', 
    'Precipitation Probability', 'Temperature High', 'Temperature High Time', 'Temperature Low',
    'Temperature Low Time', 'Apparent Temperature High', 'Apparent Temperature High Time',
    'Apparent Temperature Low', 'Apparent Temperature Low Time', 
    'Temperature Minimum', 'Temperature Minimum Time', 'Temperature Maximum', 'Temperature Maximum Time',
    'Apparent Temperature Minimum', 'Apparent Temperature Minimum Time', 'Apparent Temperature Max', 'Apparent Temperature Maximum Time'])


#creates date range for entire year selected
start_date = date(YYYY, 1, 1)
end_date = date(YYYY, 12, 31)
for single_date in daterange(start_date, end_date):    
    time = single_date.strftime("%Y-%m-%d") + "T24:00:00Z"
    
    # Assemble full url
    url1 = endpoint + key1 + '/' + lat + ',' + lon + ',' + time

    # Make a request
    r1 = requests.get(url1, params=payload1)
    print(url1)

    # deal with the information
    weather = r1.json()
    
    # Writes weather information for everyday

    # Gets time
    s = weather['daily']['data'][0]['time']
    Time = datetime.fromtimestamp(int(s)).strftime('%m-%d-%Y')
    print(Time)

    # Gets summary
    Summary1 = weather['daily']['data'][0]['summary']

    # Gets summary
    Icon1 = weather['daily']['data'][0]['icon']

    # Gets sunriseTime
    s_t = weather['daily']['data'][0]['sunriseTime']
    Sunrise_Time = datetime.fromtimestamp(int(s_t)).strftime('%m-%d-%Y %H:%M:%S')

    # Gets sunsetTime
    s_t1 = weather['daily']['data'][0]['sunsetTime'] 
    Sunset_Time = datetime.fromtimestamp(int(s_t1)).strftime('%m-%d-%Y %H:%M:%S')

    # Gets moonPhase
    Moon_Phase = weather['daily']['data'][0]['moonPhase']

    # Gets precipIntensity
    z = weather['daily']['data'][0]

    Precipitation_Intensity_Max = z.get('precipIntensityMax', 0)


    if (Precipitation_Intensity_Max != 0):
        # Gets precipIntensityMaxTime
        p_i_m_t = weather['daily']['data'][0]['precipIntensityMaxTime']
        Precipitation_Intensity_Max_Time = datetime.fromtimestamp(int(p_i_m_t)).strftime('%m-%d-%Y %H:%M:%S')
    else:
        Precipitation_Intensity_Max_Time = 0
    

    # Gets Precipitation_Probability
    Precipitation_Probability = weather['daily']['data'][0]['precipProbability']

    # Gets precipProbability
    t_h_t = weather['daily']['data'][0]['temperatureHighTime']
    Temperature_High_Time = datetime.fromtimestamp(int(t_h_t)).strftime('%m-%d-%Y %H:%M:%S')

    # Gets temperatureHightemperatureHigh
    Temperature_High = weather['daily']['data'][0]['temperatureHigh']

    # Gets temperatureHighTime
    Temperature_Low = weather['daily']['data'][0]['temperatureLow']

    # Gets icon
    t_l_t = weather['daily']['data'][0]['temperatureLowTime']
    Temperature_Low_Time = datetime.fromtimestamp(int(t_l_t)).strftime('%m-%d-%Y %H:%M:%S')

    # Gets icon
    Apparent_Temperature_High = weather['daily']['data'][0]['apparentTemperatureHigh']

    # Gets icon
    a_t_h_t = weather['daily']['data'][0]['apparentTemperatureHighTime']
    Apparent_Temperature_High_Time = datetime.fromtimestamp(int(a_t_h_t)).strftime('%m-%d-%Y %H:%M:%S')

    # Gets icon
    Apparent_Temperature_Low = weather['daily']['data'][0]['apparentTemperatureLow']

    # Gets icon
    a_t_l_t = weather['daily']['data'][0]['apparentTemperatureLowTime']
    Apparent_Temperature_Low_Time = datetime.fromtimestamp(int(a_t_l_t)).strftime('%m-%d-%Y %H:%M:%S')

    # Gets icon
    Temperature_Minimum = weather['daily']['data'][0]['temperatureMin']

    # Gets icon
    t_m_t = weather['daily']['data'][0]['temperatureMinTime']
    Temperature_Minimum_Time = datetime.fromtimestamp(int(t_m_t)).strftime('%m-%d-%Y %H:%M:%S')

    # Gets icon
    Temperature_Maximum = weather['daily']['data'][0]['temperatureMax']

    # Gets temperatureMaxTime
    T_max_t = weather['daily']['data'][0]['temperatureMaxTime']
    Temperature_Maximum_Time = datetime.fromtimestamp(int(T_max_t)).strftime('%m-%d-%Y %H:%M:%S')

    # Gets apparentTemperatureMin
    Apparent_Temperature_Minimum = weather['daily']['data'][0]['apparentTemperatureMin']

    # Gets apparentTemperatureMinTime
    a_t_min_t = weather['daily']['data'][0]['apparentTemperatureMinTime']
    Apparent_Temperature_Minimum_Time = datetime.fromtimestamp(int(a_t_min_t)).strftime('%m-%d-%Y %H:%M:%S')

    # Gets apparentTemperatureMax
    apparentTemperatureMax = weather['daily']['data'][0]['apparentTemperatureMax']

    # Gets icon
    a_t_max_t = weather['daily']['data'][0]['apparentTemperatureMaxTime']
    Apparent_Temperature_Maximum_Time = datetime.fromtimestamp(int(a_t_max_t)).strftime('%m-%d-%Y %H:%M:%S')

    csvwriterdaily.writerow([Time, Summary1, Icon1, Sunrise_Time, Sunset_Time, Moon_Phase, Precipitation_Intensity_Max, Precipitation_Intensity_Max_Time, Precipitation_Probability, Temperature_High, Temperature_High_Time, Temperature_Low, Temperature_Low_Time, Apparent_Temperature_High, Apparent_Temperature_High_Time, Apparent_Temperature_Low, Apparent_Temperature_Low_Time, Temperature_Minimum, Temperature_Minimum_Time, Temperature_Maximum, Temperature_Maximum_Time, Apparent_Temperature_Minimum, Apparent_Temperature_Minimum_Time, apparentTemperatureMax, Apparent_Temperature_Maximum_Time])

    # Writes weather information for every hour of everyday
    for x in range(0, 23):
        # Gets time
        s = weather['hourly']['data'][x]['time']
        Time1 = datetime.fromtimestamp(int(s)).strftime('%m-%d-%Y %H:%M:%S')
        print(Time1)

        # Gets summary
        Summary = weather['hourly']['data'][x]['summary']

        # Gets icon
        Icon = weather['hourly']['data'][x]['icon']
        
        # Gets Precipitation Intensity
        Precipitation_Intensity = weather['hourly']['data'][x]['precipIntensity']

        # Gets Precipitation Probability
        Precipitation_Probability = weather['hourly']['data'][x]['precipProbability']

        # Gets Temperature
        Temperature = weather['hourly']['data'][x]['temperature']

        # Gets Apparent Temperature
        Apparent_Temperature = weather['hourly']['data'][x]['apparentTemperature']

        # Gets Dew Point
        Dew_Point = weather['hourly']['data'][x]['dewPoint']

        # Gets Humidity
        Humidity = weather['hourly']['data'][x]['humidity']

        # Gets Wind Speed
        Wind_Speed = weather['hourly']['data'][x]['windSpeed']

        # Gets Wind Gust
        qw = weather['hourly']['data'][x]
        Wind_Gust = qw.get('windGust', 0)

        # Gets Wind Bearing
        y = weather['hourly']['data'][x]

        Wind_Bearing = y.get('windBearing', 0)

        # Gets Cloud Cover
        Cloud_Cover = weather['hourly']['data'][x]['cloudCover']

        # Gets UV Index
        UV_Index = weather['hourly']['data'][x]['uvIndex']

        # Gets Pressure
        Pressure = weather['hourly']['data'][x]['pressure']

        # Gets visibility
        Visibility = weather['hourly']['data'][x]['visibility']

        #Writes temperature into csv file
        Temperature = weather['hourly']['data'][x]['temperature']
        csvwriterhourly.writerow([Time1, Summary, Icon, Precipitation_Intensity, Precipitation_Probability, Temperature, Apparent_Temperature, Dew_Point,  Humidity,  Pressure,  Wind_Speed,  Wind_Gust,  Wind_Bearing, Cloud_Cover, UV_Index, Visibility])


#close writer
csvfiledaily.close()
csvfilehourly.close()


"""
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
"""