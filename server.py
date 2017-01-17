import serial
import time
import urllib, json

#WOEID, to find the WOEID for your city you should go to http://woeid.rosselliot.co.nz/lookup/leganes
WOEID = 765045

#Possible serial interfaces
interfaces = ['/dev/ttyACM0', '/dev/ttyACM1']

#Keep it running indefinitely
while 1:

	location_url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%3D" + str(WOEID) + "%20and%20u%3D'c'&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback="
	
	#Yahoo API is very unreliable, so we keep tryin until we get a good repsonse
	response = urllib.urlopen(location_url)
	data = json.loads(response.read())
	
	while data['query']['results'] == None:
		
		print "Retrying"
		time.sleep(5)
		response = urllib.urlopen(location_url)
		data = json.loads(response.read())
		
	#And finally we get the results
	current_forecast = data['query']['results']['channel']['item']['forecast'][0]
	code = current_forecast['code']
	high = current_forecast['high']
	low  = current_forecast['low']
	
	found = False

	#Connect to the arcade
	for interface in interfaces:

		try:
		    ser = serial.Serial(interface, 9600)
		    found = True
		    break

		except serial.SerialException:
		    print "No connection to the device could be established"

	if found:

		print "Your weather is served"
		ser.write(str(code) + "#" + str(high) + "#" + str(low) + "#")
		ser.close()

    #Retry in 5 minutes
	time.sleep(300)