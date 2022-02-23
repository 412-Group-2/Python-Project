'''
Created by Group 2

This program will fetch a specific http log file from the specified address.
Using this log file, it will be parsed to display various desired outputs.
'''

import requests
import os
from os.path import exists
from datetime import datetime
import re
import collections
import calendar

cwd = os.getcwd()
cwd += '\http_access_log.txt' # obtain file path 

file_exists = exists(cwd) # check if file exists


if file_exists == False: # conditional statement so the program will be able to determine if it needs to fetch the file or not. 

    url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    r = requests.get(url, allow_redirects = True) # create object to connect to and then fetch webpage information

    f = open('http_access_log.txt', 'wb')
    for chunk in r.iter_content(chunk_size = 8192):
        if chunk:
            f.write(chunk)
    f.close() # creation and closing of the file locally

regex = re.compile('([a-z]*?) - - \[(.*?):(.*?) -([0-9]*?)\] \"[A-Z]*? (.*?) .*? ([0-9]*?) [0-9]*?')
file = open('http_access_log.txt', 'r')

# Q1: How many requests were made on each day?
# A1: Count total number of requests, divide by number of days in file to average out.
# Note: This will probably need to be modified, I think he wants us to do it by day of the week (Monday, Tuesday etc.)

"""
file = open('http_access_log.txt', 'r') # counting every single request
data = file.read()
requests = data.count("GET") # This value is the total number of requests in the file
file.close()


file = open('http_access_log.txt', 'r') # Open new file object (have to do this or it won't let your readlines())

dayFirst = (file.readline())[11:22] #Puts the date (24/Oct/1994) as the valuable for this variable
dayFinal = (file.readlines()[-1])[11:22] #Puts the date (11/Oct/1995) as the valuable for this variable


date_first = datetime.strptime(dayFirst, '%d/%b/%Y') #turns dayFirst and dayFinal into datetime objects for NumDays calculation
date_final = datetime.strptime(dayFinal, '%d/%b/%Y')

NumDays = date_final - date_first 
print(NumDays)

Days_in_year = NumDays.days #converts timedelta object into integer for calculation

print( 'Avg requests per day:', round(requests/Days_in_year, 2)) #returns requests/day
#anything else needed here?
"""

# Q2: How many requests were made on a week-by-week basis? Per month?
# A2: Take previous total number of requests and divide by number of weeks, then months.
total_count = 0

days = {
  "Monday": 0,
  "Tuesday": 0, 
  "Wednesday": 0, 
  "Thursday": 0,
  "Friday": 0, 
  "Saturday": 0,
  "Sunday": 0
}

months = {
  1: 0,
  2: 0, 
  3: 0, 
  4: 0,
  5: 0, 
  6: 0,
  7: 0, 
  8: 0,
  9: 0, 
  10: 0, 
  11: 0,
  12: 0
}
month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

for line in file:
    total_count +=1 
    parts = regex.split(line)
    if len(parts) != 8:
        continue
    datestamp = datetime.strptime(parts[2], '%d/%b/%Y')
    days[str(calendar.day_name[datestamp.weekday()])] += 1
    months[datestamp.month] += 1

print("Requests by day of the week:")
for a, b in days.items():
    print(f'{a}: {b}')

print("\nRequests by month:")
for i in months:
    print("%s: %i" % (month_names[i-1], months[i]))

# Q3: What percentage of the requests were not successful (any 4xx status code)?
#([a-z]*?) - - \[(.*?):(.*?) -([0-9]*?)\] \"[A-Z]*? (.*?) .*? (4\d\d )
# A3: How many requests have a 4XX status code?

file = open('http_access_log.txt', 'r') 
data = file.read()
regex_q3 = re.compile('([a-z]*?) - - \[(.*?):(.*?) -([0-9]*?)\] \"[A-Z]*? (.*?) .*? (4\d\d )')
matches = re.findall(regex_q3, data)
request4XX = round(len(matches) / requests * 100, 2)
print("\nThe percent of requests that were not succesful (4XX) was {0}%".format(request4XX))
file.close()

# Q4: What percentage of the requests were redirected elsewhere (any 3xx codes)?
# A4: How many requests have a 3XX code? Divide this number by total requests for answer.

file = open('http_access_log.txt', 'r') 
data = file.read()
regex_q4 = re.compile('([a-z]*?) - - \[(.*?):(.*?) -([0-9]*?)\] \"[A-Z]*? (.*?) .*? (3\d\d )')
matches2 = re.findall(regex_q4, data)
request3XX = round(len(matches2) / requests * 100, 2)
print("\nThe percent of requests that were redirected elsewhere (3XX) was {0}%".format(request3XX))
file.close()

# Q5: What was the most-requested file?
# Q6: What was the least-requested file?
# Q5 & 6: def fileCount():
def fileCount():
	filelog = []
	least_common = []
	with open('http_access_log.txt') as logs:
		for line in logs:
			try:
				filelog.append(line[line.index("GET")+4:line.index("HTTP")])		#find all files between GET requests and HTTP protocol"
			except:
				pass
	counter = collections.Counter(filelog)
	for count in counter.most_common(1):														
		print("\nMost commonly requested file is: {} with {} requests.".format(str(count[0]), str(count[1])))
	for count in counter.most_common():					#checking for file requests that only occur once as they must be the least requested
		if str(count[1]) == '1':
			least_common.append(count[0])
	if least_common:										#many file requests that were only requested once 													
		response = input("There were {} file(s) that were requested once, do you want to see them all? (y/n)".format(len(least_common)))
		if response == 'y' or response == 'Y':
			for file in least_common:
				print(file)
fileCount() # probably should be moved to end because a response can be given to get more data

# Q7: Now every single month needs its own log file. 
# A7: We need to seperate the original file into 12 months and give each month its own new log file. Could use one function for each month's file to keep it clean. 

'''
BELOW IS ALL THE OF PART 1'S FILE PARSING THAT WE DID. WE DON'T NEED THIS EXACT CODE ANYMORE, BUT I LEFT IT DOWN HERE FOR REFERENCE ###

#count every valid request in the file
file = open('http_access_log.txt') 
data = file.read()
requests = data.count("GET")
print ('TOTAL REQUESTS IN LOG :', requests)


#make a new file and cut off all but the last six months of requests
with open('http_access_log.txt', 'r') as sixmon:
    lines = sixmon.readlines()

with open('six_months_access_log.txt', 'w') as sixmon2:
    for number, line in enumerate(lines):
        if number not in range(0, 166364):
            sixmon2.write(line)
#count the requests from the new file

file = open('six_months_access_log.txt') 
data = file.read()
lastsixrequests = data.count("GET")
print ('TOTAL REQUESTS OVER LAST SIX MONTHS FROM 11 OCT 1995 :', lastsixrequests)
'''
