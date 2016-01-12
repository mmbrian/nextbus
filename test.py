from __future__ import unicode_literals
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

import unirest as u
import json

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36';

ROOT_URL = 'http://www.saarfahrplan.de/'

HEADERS = {
	'User-Agent': USER_AGENT,
	'Accept': 'text/html'}


# SEARCH_REQUEST % name
SEARCH_REQUEST = 'http://www.saarfahrplan.de/cgi-bin/ajax-getstop.exe/dny?' + \
				 'start=1&tpl=suggest2json&REQ0JourneyStopsS0A=255&getstop=1&noSession=yes&REQ0JourneyStopsB=12&REQ0JourneyStopsS0G=%s?&js=true&'

LOCATE_REQUEST = 'http://www.saarfahrplan.de/cgi-bin/query.exe/eny?performLocating=2&tpl=stop2json&' + \
				 'look_maxno=150&look_nv=get_stopweight|yes|selectable|yes|&' + \
				 'look_maxdist=2088642&look_stopclass=2047&&' + \
				 'look_maxx=7038524&look_maxy=49250258.5&' + \
				 'look_minx=6996468&look_miny=49236248.5'
# TODO: study the javascript in info.html to find out how to convect from latitude and longitude to these
# values and finally generate such a request to get bus stations in an area


def test_1():
	response = u.get(ROOT_URL, 
		headers = HEADERS)
	return response

def search(name):
	'''
	Searches for a `name` string and returns all matching stations
	'''
	response = u.get(SEARCH_REQUEST % name, 
		headers = { 'User-Agent': USER_AGENT,
					'Accept': 'text/plain'})
	print response.code
	res = unicode(response.body, errors='ignore')
	# (original response is sth like: Sls.sls={...};Sls.method();)
	# Fetching everything before the largest {}
	res = res[res.index('{'):(len(res)-res[::-1].index('}'))]
	jdata = json.loads(res)
	return jdata['suggestions']
	# print res

def nearest():
	'''
	TODO: result is sth like 

	stops: [{
		x: "6996843",
		y: "49246180",
		name: "Paul-Lincke-Str., Saarbrcken Malstatt",
		urlname: "Paul-Lincke-Str.,%20Saarbr%FCcken%20Malstatt",
		extId: "11016",
		puic: "80",
		planId: "1452187787",
		stopweight: "365"
	}, {
		x: "6996924",
		y: "49244472",
		name: "Rodenhof Ausstieg, Saarbrcken",
		urlname: "Rodenhof%20Ausstieg,%20Saarbr%FCcken",
		extId: "10409",
		puic: "80",
		planId: "1452187787",
		stopweight: "359"
	}

	which sucks since this is not a proper json format as keys aren't strings
	idea: add double quotes to every key which ends with a ':'
	'''
	response = u.get(LOCATE_REQUEST, 
		headers = { 'User-Agent': USER_AGENT,
					'Accept': 'text/plain'})
	print response.code
	res = unicode(response.body, errors='ignore')
	# res = res[res.index('{'):(len(res)-res[::-1].index('}'))]
	# jdata = json.loads(res)
	# return jdata
	return res



def main():
	# return test_1()
	# return search('13123123')
	return nearest()
