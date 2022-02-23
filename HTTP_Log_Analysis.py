'''
Created by Group 2

This program will fetch a specific http log file from the specified address.
Using this log file, it will be parsed to show the total number of logs in the past 6 months, and all time logs.
'''

import requests #necessary module
import os # necessary module
from os.path import exists #neccesary module
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

'''
with open('http_access_log.txt') as f: 
    for line in f:
        print(line.rstrip()) # re-opening file and then iterating through each line 1 time. 
#Ben got rid of this and replaced it with a counter for all GET occurances in file.
# IDK what "in the six months" means in the instructions but we'll cross that bridge tomorrow.

'''
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





# Opens file (seems redundant but it was the only way I could get it to work)

    # Do for each line in file


'''
    for line in file:
        # Check if the line has brackets
        if "[" in line:
            # Use regex to find the date of the log line
            temp = re.search(r"\[(.*?)\]", line)
            # important: temp.group(0) is the regex'd info, .strip removes the brackets from that
            # format is DD/MMM/YYYY:HH:MM:SS -Timezone (I think?)
            # print(temp.group(0).strip("[]")) (I AM FOR TESTING)
            # you might be able to convert to datetime and work from there
            # reads to data (put in another nested if statement?)
            # compare the data in temp to see if it is within 6 months from oct 11 1995
            count = count + 1
    
            
print ('TOTAL REQUESTS OVER LAST SIX MONTHS FROM 11 OCT 1995 :', count)

#11/Apr/1995

with open('http_access_logs.txt') as file:
    for line in file:
        print(line.rstrip())
        
#this change prints the requests line by line. Becasue the file is large this is better than printing a single object (list) with all the info. 

'''

