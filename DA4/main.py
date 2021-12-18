##############################################
# Programmer: Jonathan Smoley
# Class: CPSC 222, Fall 2021
# Assignment: Data Assignment #4
# Date: 10/20/21
# Description: This program utilizes API(s),
#   data cleaning, and JSON file parsing to
#   produce viable resulting data.
# Notes: I attempted the bonus!
##############################################
import utils

def main():
    # prompt user for name of large city
    city_formatted, city = utils.prompt_user()

    # collect an API url and key
    mapQ_url = "https://www.mapquestapi.com/geocoding/v1/address"
    mapQ_key = "HKDCNjkGCHx6xOEX8me100n1XKvhGFJe" # (my api key, but repo is private)

    # send a request to MapQuest API for geolocated latitude and longitude
    latitude, longitude = utils.map_quest_request(mapQ_url, mapQ_key, city_formatted)

    # collect an API url, key, and request parameters (using latitude and longitude)
    meteostat_url = "https://meteostat.p.rapidapi.com/stations/nearby"
    meteostat_key = {"x-rapidapi-host": "meteostat.p.rapidapi.com", 
                     "x-rapidapi-key": "d43655e34emsh84cbd24bc425d91p19a5ebjsncff3cb4de089" # (my api key, but repo is private)
                    }
    meteostat_params = {"lat": str(latitude), "lon": str(longitude)}

    # send a request to Meteostat API for nearby station data
    meteostat_json = utils.meteostat_request(meteostat_url, meteostat_key, meteostat_params)

    # parse for the weather station id
    station_id = utils.grab_station_id(meteostat_json)

    # collect an API url and params (use Rapid API key from above)
    meteostat_url = "https://meteostat.p.rapidapi.com/stations/daily"
    meteostat_params = {"station": str(station_id), "start": "2021-01-01", "end": "2021-10-21", "units": "imperial"}

    # send another request to Meteostat API for daily weather data
    daily_weather_json = utils.meteostat_request(meteostat_url, meteostat_key, meteostat_params)

    # structure into a pandas DataFrame, use date as index
    meteostat_df = utils.json_to_df(daily_weather_json)

    # write to csv file named after requested city
    meteostat_df.to_csv(city + "_daily_weather.csv")

    # clean the DataFrame
    clean_df = utils.clean_DataFrame(meteostat_df)

    # write cleaned DataFrame to new .csv file
    clean_df.to_csv(city + "_daily_weather_cleaned.csv")

    # bonus task (whole task done inside this function)
    utils.visualize_data(clean_df, city)

# main() call
main()