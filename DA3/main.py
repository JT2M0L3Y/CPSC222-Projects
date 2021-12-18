##############################################
# Programmer: Jonathan Smoley
# Class: CPSC 222-01, Fall 2021
# Assignment: Data Assignment #3
# Date: 10/12/21
# Description: This program uses the pandas
#   module to read data from a .csv file and
#   to perform a set of stats on said data.
##############################################
import utils

def main():
    # load each file into its own DataFrame
    youtube_df = utils.load_file("youtube_analytics_9-20-20_9-20-21.csv", "Date")
    days_df = utils.load_file("days_of_week_9-20-20_9-20-21.csv", "Date")

    # prompt user for a start date, end date, and numeric column to analyze
    start_date, end_date, user_col = utils.request_user_values(youtube_df)

    # create a series with data between the slice dates and in the user-selected column
    youtube_ser = utils.slice_data_frame(youtube_df, start_date, end_date, user_col)

    # compute stats on user-requested column and form a statistics series object
    utils.compute_stats(youtube_ser)

    # join both DataFrame objects together on "Date" keyword & write to file
    merged_df = utils.merge_frames(youtube_df, days_df, "Date")

    # perform the split-apply-combine technique
    utils.split_apply_combine(merged_df, user_col)

# call main function
main()