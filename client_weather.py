#!/usr/bin/env python
from requests import get

lon="19.04"
lat="47.48"
APP_KEY="32e8867d11123e2b3d0f0b1b4f107a79"
WEATHERDATA = "http://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&APPID={2}".format(lat, lon, APP_KEY)

if __name__ == "__main__":
    try:
        data = get(WEATHERDATA)
        cur_temp =  int(data.json()['main']['temp'])-273.15
        print cur_temp
    except:
        print "Failed to get temperature!"
