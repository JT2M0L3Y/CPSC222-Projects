##############################################
# Programmer: Jonathan Smoley
# Class: CPSC 222-01, Fall 2021
# Assignment: Data Assignment #2
# Date: 9/28/21
# Description: The is the functions file for
#   the main.py file that reads and
#   summarizes the data from a .csv.
##############################################
import math

def read_data(filename):
    '''
    Reads in the data by referencing a .csv file one line at a time
    Parameter filename: references a path for the file to read from
    Returns: header list, data list
    '''
    # open input file to read from
    in_file = open(filename, "r")

    # read in all lines
    lines = in_file.readlines()

    # clean up the data lines
    clean_data_lines(lines)

    # read in the data lines
    data = get_data(lines)

    # separate the header list
    header = get_header(data)

    # clean up the header list
    clean_data_lines(header)

    # close the input file
    in_file.close()

    # return the new lists to the main() function
    return header, data

def clean_data_lines(lines):
    '''
    Removes characters that are awkward to work with
    Parameter lines: 1D list of all data pulled from the file
    Returns: same 1D list, but without '\n' chars
    '''
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

def get_data(lines):
    '''
    uses the 1D list of all the file data to find just the the numeric
        data needed for calculations
    Parameter lines: the aforementioned 1D list
    Returns: 2D data list holding each line as a single list element
    '''
    # initialize an empty 1D list to be populated
    data = []

    # loop through the lines read in to fill the data list
    for line in lines:
        data_line = line.split(",")
        data.append(data_line)

    return data

def get_header(data):
    '''
    Removes the first line of the data set read in as it is just the
        headers of each column
    Parameter data: the list containing everything read from the file
    Returns: a list for the header row of the .csv file
    '''
    # remove top line of data and send it to a 1D list
    header = data.pop(0)

    return header

def display_table(header, data):
    '''
    Shows the data in a grid-like table with headers at the top for
        easy reading
    Parameter header: 1D list for the column headers
    Parameter data: 2D list for the numeric data in the file
    Returns: N/A
    '''
    # print the column headers
    for i in header:
        print(i, end = " ")
    print()
    
    # print the data in a grid-like format
    for row in data:
        for col in row:
            print(col, end = "\t")
        print()

def get_column(header, col_name, data):
    '''
    Takes a copy of the user-requested column from the data collected
        to perform calculations on just the subject data
    Parameter header: 1D list for the column headers
    Parameter col_name: string var for column name
    Parameter data: 2D list of data to return the data from the
        requested column
    '''
    # grab the index of the user's requested column
    col_index = header.index(col_name)

    # initialize 1D column data list
    column_data = []

    # iterate through the 2D data list to grab the col_index value out of each inner list
    for row in data:
        for i in range(len(row)):
            if i == col_index:
                column_header = header[i]
                column_data.append(row[i])
    
    return column_header, column_data

def compute_mean(column_data):
    '''
    computes average of the data in the user-requested column
    Parameter column_data: data from the user's desired column
    Returns: mean value
    '''
    # fill a new list with the numeric version of string data values
    data = [float(value) for value in column_data]

    # compute mean
    column_mean = round(sum(data) / len(data), 2)

    return column_mean

def compute_std_dev(column_data, column_mean):
    '''
    computes standard deviation of column data
    Parameter column_data: data from the user's desired column
    Parameter column_mean: average of user's desired column
    Returns: column's standard deviation value
    '''
    # compute standard deviation
    std_dev = math.sqrt(sum(pow(float(data) - column_mean, 2) for data in column_data) / (len(column_data) - 1))

    return round(std_dev, 2)

def compute_mid_min_max(column_data):
    '''
    computes all three: median, minimum, maximum
    Parameter column_data: data from the user's desired column
    Returns: column median, column minimum, column maximum
    '''
    # find median value
    sorted_column = sorted(column_data)
    col_mid = round(float(sorted_column[(len(sorted_column) // 2)]), 2)

    # find minimum value
    col_min = column_data[0]
    for num in column_data:
        if float(num) < float(col_min):
            col_min = float(num)
    col_min = round(col_min, 2)

    # find maximum value
    col_max = column_data[0]
    for num in column_data:
        if float(num) > float(col_max):
            col_max = float(num)
    col_max = round(col_max, 2)

    return col_mid, col_min, col_max

def print_stats(column_header, column_mean, std_dev, col_mid, col_min, col_max):
    '''
    outputs stats calculations for the provided column
    Parameter column_header: header of column requested by user
    Parameter column_mean: average of the column
    Parameter std_dev: standard deviation of the column
    Parameter col_mid, col_min, col_max: associated min/max/median of column
    Returns: N/A
    '''
    # tell which column this summary is for
    print("This is a summary of the", column_header, "column!")
    
    # provide actual stats
    print("This is the mean:", column_mean)
    print("This is the standard deviation:", std_dev)
    print("This is the median:", col_mid)
    print("This is the smallest value:", col_min)
    print("This is the largest value:", col_max)