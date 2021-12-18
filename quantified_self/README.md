# Quantified-Self Project

## Overview

As technology becomes more important to our daily lives, so does a separation from reality. For this project, the domain is my iPhone. With this domain, I can explore the amount of time I spent out of reality this semester. The iPhone has a setting that tracks the screen time of a given user down to the number of times a user picks up their phone.  

While my screen time data was collected manually into a .csv file using MS Excel, I also utilized data from the Visual Crossing REST API for weather data. I had originally planned to make a direct request for data within this report. However, Visual Crossing was in the process of updating their UI so I found it easier to download another .csv from the API webpage. Instead of manually combining both tables into a single dataset, I decided to read in each table individually, combine them into a pandas DataFrame, and then write said DataFrame to a new .csv file that would not be read in again for access. This dataset has many more attributes than I plan to use as I recorded virtually everything I could find on my screen time data and the API has no setting to limit the attributes I receive. Thus, I have about 30 attributes including max/min/mean temperatures, weather conditions, app usage times, apps used, notification counts, and even a count of pick ups each day.  

I am attempting to classify how much time I spent on my phone given the temperature and weather conditions for a given day. This classification could result in my taking a step to change my iPhone usage habits. Beyond personal applications, this classification could be used by others iPhone users to find what they need to do to decrease, or even increase, their screen time habits.

## Resources

[Directions to Your iPhone's Screen Time Data](https://support.apple.com/guide/iphone/view-your-screen-time-summary-iph24dcd4fb8/ios) - manually collected, different for every user

[Visual Crossing's Weather API](https://www.visualcrossing.com/) - used to draw out weather condition and temperature data
