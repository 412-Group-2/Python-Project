'''
Created by Group 2

This program will fetch a specific http log file from the specified address.
Using this log file, it will be parsed to show the total number of logs in the past 6 months, and all time logs.
'''

retrieved == False 

if retrieved == False: # conditional statement so the program will be able to determine if it needs to fetch the file or not. 

  import requests #necessary module

  url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
  r = requests.get(url, allow_redirects = True) # This is the object that the fecth is associted

  f = open('name', 'r').write(r.content)
  print(f.read)
