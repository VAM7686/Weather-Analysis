#import module
import csv
import math

# Import requests
import requests
import json

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

location_finder()

while True:
	retry = input("Would you like to pick another location? Enter y or n")
	
	if ((retry != 'y') and (retry != 'n') and (retry != 'Y') and (retry != 'N')):
		print("Invalid entry. Enter y or n")
		continue
	elif ((retry == 'y') or (retry == 'Y')):
		location_finder()
	else:
		break
