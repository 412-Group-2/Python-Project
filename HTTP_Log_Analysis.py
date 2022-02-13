'''
Created by Group 2

This program will fetch a specific http log file from the specified address.
Using this log file, it will be parsed to show the total number of logs in the past 6 months, and all time logs.
'''

import requests #necessary module
import os # necessary module
from os.path import exists #neccesary module

cwd = os.getcwd()
cwd += '\http_access_log.txt'

file_exists = exists(cwd)

if file_exists == False: # conditional statement so the program will be able to determine if it needs to fetch the file or not. 

    url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    r = requests.get(url, allow_redirects = True) 

    f = open('http_access_log.txt', 'wb')
    for chunk in r.iter_content(chunk_size = 8192):
        if chunk:
            f.write(chunk)
    f.close()

'''with open('http_access_log.txt', 'r') as f: 
    #print(f.read())'''
# The above is the part that makes my IDE freeze. Don't think it should be doing that. 
