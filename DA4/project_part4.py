##############################################
# Programmer: Jonathan Smoley
# Class: CPSC 222, Fall 2021
# Assignment: Data Assignment #4
# Date: 10/20/21
# Description: This file requests and parses
#   a response from an API then prints it out.
##############################################
import requests
import json
import pandas as pd

'''
This API generates a list of universities where each
university name contains a word passed as a parameter.
It is an open API, so I did not need to use a key to
gain access. Also, the response is in the form of a 
list of JSON objects.

Documentation: https://github.com/Hipo/university-domains-list-api/blob/master/README.md
'''

# reference basic url
api_url = "http://universities.hipolabs.com"

# choose an endpoint used for generating a response
endpoint = "/search"

# define which value to search for (name, location, etc.)
search_value = "?name=washington"

# combine the basic url with the separate endpoint
tot_url = api_url + endpoint + search_value

# send a request to the API
data_response = requests.get(tot_url)

# convert the response into JSON
universities = json.loads(data_response.text)

# fill a new DataFrame with the values
uni_df = pd.DataFrame()
for obj in universities:
    uni_df = uni_df.append(obj, ignore_index = True)

# output all data
print(uni_df)

# grab just the names of the universities
names = pd.Series(uni_df["name"])

# print parsed data
print(names)