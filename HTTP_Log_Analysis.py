'''
Created by Group 2

This program will fetch a specific http log file from the specified address.
Using this log file, it will be parsed to show the total number of logs in the past 6 months, and all time logs.
'''

import requests
import os
from os.path import exists

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
