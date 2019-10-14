chars_togo = ["'", " "]

newlist = ['Time', 'Summary', 'Icon', 'Preciptation Intensity', 
	'Preciptation Probability', 'Temperature', 'Apparent Temperature', 'Dew Point', 
	'Humidity', 'Pressure', 'Wind Speed', 'Wind Gust', 'Wind Bearing', 'Cloud Cover', 
	'UV Index', 'Visibility']

newlist1 = ['Time', 'Summary', 'Icon', 'Sunrise Time', 'Sunset Time', 
	'Moon Phase', 'Precipitation Intensity Max', 'Precipitation Intensity Max Time', 
	'Precipitation Probability', 'Temperature High', 'Temperature High Time', 'Temperature Low',
	'Temperature Low Time', 'Apparent Temperature High', 'Apparent Temperature High Time',
	'Apparent Temperature Low', 'Apparent Temperature Low Time', 
	'Temperature Minimum', 'Temperature Minimum Time', 'Temperature Maximum', 'Temperature Maximum Time',
	'Apparent Temperature Minimum', 'Apparent Temperature Minimum Time', 'Apparent Temperature Maximum Time']



l = len(newlist)
l1 = len(newlist1)


for i in chars_togo:
	for j in range(l1):
		newlist1[j] = newlist1[j].replace(i, '_')

for i in range(l1):
	print(newlist1[i]+",", end=" ")
"""

# Python3 code to demonstrate 
# removal of bad_chars 
# using replace() 

# initializing bad_chars_list 
bad_chars = ["'"] 

# initializing test string 
test_string = "Ge''ek * s''fo ! r;Ge * e*k:s !"

# printing original string 
print ("Original String : " + test_string) 

# using replace() to 
# remove bad_chars 
for i in bad_chars : 
	test_string = test_string.replace(i, '') 

# printing resultant string 
print ("Resultant list is : " + str(test_string)) 
"""