##############################################
# Programmer: Jonathan Smoley
# Class: CPSC 222-01, Fall 2021
# Assignment: Data Assignment #2
# Date: 9/28/21
# Description: This program reads in data from
#   a .csv file to compute a number of statistics
#   and then summarize it (output to console).
# Notes: This file is made for my project data.
##############################################

# reference the file with function definitions
import utils

def main():
    # read in data from the input file
    header, data = utils.read_data("Logged Commute Miles.csv")

    # display data to the user in a table
    utils.display_table(header, data)

    # request a column name to draw from the table from the user
    col_name = input("Enter the name of a column you wish to summarize: ")

    # get column requested by user
    column_header, column_data = utils.get_column(header, col_name, data)

    # compute statstics on selected data
    # mean
    column_mean = utils.compute_mean(column_data)
    # standard deviation
    std_dev = utils.compute_std_dev(column_data, column_mean)
    # median/min/max
    col_mid, col_min, col_max = utils.compute_mid_min_max(column_data)

    # output a summary of the results
    utils.print_stats(column_header, column_mean, std_dev, col_mid, col_min, col_max)

# call main() so program actually runs
main()