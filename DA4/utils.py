##############################################
# Programmer: Jonathan Smoley
# Class: CPSC 222, Fall 2021
# Assignment: Data Assignment #4
# Date: 10/20/21
# Description: This file is a functions-specific
#   file for DA4's main.py file.
# Notes: I attempted the bonus!
##############################################
import requests
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def prompt_user():
    '''
    Ask user to enter a city to geolocate data for.
    Returns: city formatted for an api url parameter
    '''
    # promt user
    user_city = input("Enter the name of a large city: ")

    # replace any spaces with a '+'
    city = user_city.replace(" ", "+")

    return city, user_city

def map_quest_request(url, key, city):
    '''
    Make a request to the MapQuest API for data,
        then parse for the geolocated values for
        the city's latitude and longitude
    Returns: latitude and longitude for the city
    '''
    # add key and location parameters to url
    url += "?key=" + key
    url += "&location=" + city

    # send a request to MapQuest API for JSON data
    response = requests.get(url = url)

    # convert to json object
    json_data = json.loads(response.text)

    # parse for latitude and longitude
    return grab_lat_lon(json_data)

def grab_lat_lon(json_data):
    '''
    Parse through the JSON file for the city's 
        latitude and longitude.
    Returns: the latitude and longitude
    '''
    # parse into location of lat and lon
    results = json_data["results"]
    results_list = results[0]
    locations = results_list["locations"]
    locations_list = locations[0]
    lat_lon = locations_list["latLng"]

    # assign latitude and longitude
    lat = lat_lon["lat"]
    lon = lat_lon["lng"]

    return lat, lon

def meteostat_request(api_url, key, param_values):
    '''
    Make a request to the Rapid (Meteostat) API for data
    Returns: the response sent back in json
    '''
    # send a request to Meteostat API for JSON data
    response = requests.get(url = api_url, headers = key, params = param_values)

    # convert to JSON format
    json_data = json.loads(response.text)

    return json_data

def grab_station_id(json_data):
    '''
    Parse the JSON for the nearby station id
    Returns: weather station id
    '''
    data_list = json_data["data"]
    data_index = data_list[0]
    data_id = data_index["id"]

    return data_id

def json_to_df(json_data):
    '''
    Convert the daily weather JSON into
        a pandas DataFrame (index as date)
    Returns: a nice DataFrame object
    '''
    # use pandas to build a DataFrame
    new_df = pd.DataFrame(json_data["data"])
    
    # change index of DataFrame
    new_df.set_index("date", inplace = True)

    return new_df

def clean_DataFrame(current_df):
    '''
    Perform data cleaning operations
        on the weather data frame
    Returns: clean DataFrame
    '''
    # remove columns where more than 75% of data is missing
    current_df.dropna(axis = 1, thresh = (current_df.shape[0] * 0.75), inplace = True)

    # fill remaining missing values
    # middle
    current_df.interpolate(method = "linear", inplace = True)
    # first & last
    current_df = current_df.fillna(method = "ffill").fillna(method = "bfill")

    return current_df

def visualize_data(df, city):
    '''
    Prompt user for a column in the data set
        to use to display data in a chart.
    Returns: N/A
    '''
    # display choices
    for col in df.columns:
        print(col)

    # prompt user to choose a column from the list
    user_col = input("Enter a column name from above to show in a bar chart: ")
    
    # create a bar chart as a .png
    plt.bar(df.index.values, df[user_col])
    plt.title(city + " Daily " + user_col + " Data")
    plt.xlabel("Month")
    plt.ylabel(user_col)
    
    # member functions found in the matplotlib.dates documentation
    months = mdates.MonthLocator()
    date_format = mdates.DateFormatter('%b')
    bar_plot = plt.gca().xaxis
    bar_plot.set_major_locator(months)
    bar_plot.set_major_formatter(date_format)

    # save figure to a file
    plt.savefig(city + "_daily_" + user_col + ".png")