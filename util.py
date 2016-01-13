'''
Updates on reverse engineering the location search API:

y > latitude
x > longitude

I can use ArcGIS for Android https://developers.arcgis.com/android/
so that given a lat/lon and a distance and an angle, compute anothe set of lat/lon
this way I can construct the boundaries of the rectangle with which I can construct
a url. 
still not sure what look_maxdist is for.

This C# application http://kiwigis.blogspot.de/search/label/Projection%20Engine
which is also inside AS15716.zip has a method I need
As an alternative I can use http://williams.best.vwh.net/gccalc.htm [1]
which is using http://williams.best.vwh.net/avform.htm#LL
but my initial implementation failed. doesn't seem to be very trivial. however, since
ArcGIS is not totally free, getting the javascript code at [1] to work in android and python 
is the ultimate plan. 

Update! the code in [1] is actually using no external code other than some math functions in javascript,
converting it to android/python HAS to be easy.

source: https://gis.stackexchange.com/questions/5821/calculating-lat-lng-x-miles-from-point
'''

import numpy as np
from numpy import cos, sin, radians, degrees, mod, pi
from numpy import arcsin, arctan2

def getLoc(lat1, lon1, d, tc):
	lat, lon = None, None
	lat1, lon1 = radians(lat1), radians(lon1)
	tc = radians(tc)
	
	lat = arcsin(sin(lat1)*cos(d)+cos(lat1)*sin(d)*cos(tc))
	if cos(lat) == 0:
		lon = lon1 # endpoint is a pole
	else:
		lon = mod(lon1-arcsin(sin(tc)*sin(d)/cos(lat))+pi,2*pi)-pi
	
	lat = arcsin(sin(lat1)*cos(d)+cos(lat1)*sin(d)*cos(tc))
	dlon = arctan2(sin(tc)*sin(d)*cos(lat1),cos(d)-sin(lat1)*sin(lat))
	lon = mod(lon1-dlon+pi,2*pi)-pi

	return degrees(lat), degrees(lon)