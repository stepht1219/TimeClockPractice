# Weather Example                                                                                                                                                                   
# Processing json data from openweathermap.org                                                                                                                                      
# api.openweathermap.org                                                                                                                                                            
#                                                                                                                                                                                   
# Author: Stephanie Tattrie                                                                                                                                                         
# Date: 10/21/15                                                                                                                                                                    


import json
#import tabulate as tbl                                                                                                                                                             
import urllib.request
city = input("Enter a City: ")
metric = input("Enter a Metric: ")

#h = ["Date", "Weather", "Temp Kelvins", "Chosen Metric"]                                                                                                                           
def f_getForecast(city,metric):

    location = city
    weatherURL = "http://api.openweathermap.org/data/2.5/forecast/city?id=524901&APPID=f6a3c3006543a72a4db855d0fcf1f168&q=" + location

    json.input = urllib.request.urlopen(weatherURL).read()
    decoded = json.input.decode("utf-8")
    data = json.loads(decoded)


    wList = []
    x = 0
    while x < len(data['list'])- 1:
        dt = data['list'][x]['dt_txt']
        date, time = dt.split(" ")
        n = data['city']['name']
        c = data['city']['country']

        w = data['list'][x]['weather'][0]['description']

        t = data['list'][x]['main']['temp']


        x += 1
        if metric == "f":
            ntemp = t * 9/5 - 459.67
        elif metric == "c":
            ntemp = t - 273.15

        wList.append([date, w, t, ntemp])

    print("\nCity Name and Country:", n, c)
    print("\nDate \t\tWeather \tTemp \tTemp in requested metric")
#    print(tbl.tabulate(wList, h)                                                                                                                                                   
    s = 0
    for s in wList:
        print(s)


def main():
    f_getForecast(city,metric)

main()

