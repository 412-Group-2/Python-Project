'''
Created by Group 2

This program will fetch a specific http log file from the specified address.
Using this log file, it will be parsed to show the total number of logs in the past 6 months, and all time logs.
'''

import requests #necessary module
import os # necessary module
from os.path import exists #neccesary module

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

with open('http_access_log.txt') as f: 
    for line in f:
        print(line.rstrip()) # re-opening file and then iterating through each line 1 time. 
        
'''

From here I would figure out how to put each line item into a list. 

'''
