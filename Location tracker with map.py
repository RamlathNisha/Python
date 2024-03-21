import requests
import folium
import datetime
from selenium import webdriver
import time

ip_inp=input()
ip="https://ipinfo.io/"+ip_inp
response=requests.get(ip).json()
loc=response['loc'].split(',')
lat=loc[0]
lon=loc[1]
city=response['city']
region=response['region']
country=response['country']
print("IP address:",response['ip'])
print("Location:",city+','+region)

map=folium.Map(location=[lat,lon],zoom_start=12)
map.add_child(folium.Marker(location=[lat,lon],popup="Your Location:"+city,icon=folium.Icon(color='blue')))
file="E:/Nisha/Mine/Internship/Codealpha ( python )/Task 5/"+str(datetime.date.today())+".html"
map.save(file)

dr=webdriver.Chrome()
dr.get(file)
time.sleep(100)


#14.139.188.196 - Tirunelveli
# 198.35.26.96  - Sanfransico

