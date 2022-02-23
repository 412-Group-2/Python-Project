'''
Created by Group 2

This program will fetch a specific http log file from the specified address.
Using this log file, it will be parsed to show the total number of logs in the past 6 months, and all time logs.
'''

import requests
import os
from os.path import exists
from datetime import datetime
import re

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


# Q1: How many requests were made on each day?
# A1: Count total number of requests, divide by number of days in file to average out.

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

# Q2: How many requests were made on a week-by-week basis? Per month?
# A2: Take previous total number of requests and divide by number of weeks, then months.

# Q3: What percentage of the requests were not successful (any 4xx status code)?
# A3: How many requests have a 4XX status code?

# Q4: What percentage of the requests were redirected elsewhere (any 3xx codes)?
# A4: How many requests have a 3XX code? Divide this number by total requests for answer.

# Q5: What was the most-requested file?
# Q5: 
    
# Q6: What was the least-requested file?
# Q6: 

# Q7: Now every single month needs its own log file. 
regex = re.comple('(.?) - - [(.?):(.) .] "[A-Z]{3,6} (.?) HTTP." (\d{3}) (.+)')
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
