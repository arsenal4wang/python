# __author__ = 'Administrator'
# coding=utf-8
import urllib
import re
import datetime


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    page.close()
    return html


def getWeather(html):
    reg = '<a title=.*?>(.*?)</a>.*?<span>(.*?)</span>.*?<b>(.*?)</b>'
    # reg = '<div class="cname"><a title=.*?>(.*?)</a></div>'
    reg1 = '<a.*?>(.*?)</a>.*?<div class="weather">(.*?)</div>.*?<div class="temp">(.*?)</div>'
    # weatherList = re.compile(reg1).findall(html)
    # weatherList = re.compile(r'<a target="_blank" href=.*?>(.*?)</a>').findall(html)
    weatherList = re.compile(r'<a target="_blank" href=.*?>(.*?)</a>').findall(html)
    return weatherList

print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " 广东部分地区天气预报"
print "City" + "   " + "High" + "   " + "Low"
# weatherList = getWeather(getHtml('http://gd.weather.com.cn/index.shtml'))
weatherList = getWeather(getHtml('http://www.nmc.cn/publish/forecast/AHB.html'))
print weatherList

for weather in weatherList:
    print (str(weather[0]).decode('utf-8')), (' '), (str(weather[1]).decode('utf-8')), (' '), (
        str(weather[2]).decode('utf-8'))

