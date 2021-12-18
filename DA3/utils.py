##############################################
# Programmer: Jonathan Smoley
# Class: CPSC 222-01, Fall 2021
# Assignment: Data Assignment #3
# Date: 10/12/21
# Description: This is the functions file for
#   data assignment 3.
##############################################
import pandas as pd

def load_file(csv_file, csv_col):
    '''
    Reads .csv data to a pandas DataFrame
    Parameter csv_file: file to read from
    Parameter csv_col: column to use as a key
    Returns: a new DataFrame object
    '''
    new_df = pd.read_csv(csv_file, index_col = csv_col)

    return new_df

def request_user_values(given_df):
    '''
    Asks user to enter values to slice the DataFrame at 
        and which column to analyze
    Returns: starting value, ending value, column to use
    '''
    start_value = input("Choose a start date to slice from: ")
    end_value = input("Choose an end date to slice up to & include: ")
    
    # show options for columns available to perform stats on
    for col in given_df.columns:
        print(col)
    print()

    selected_col = input("Choose a numeric column to perform statistics on: ")

    return start_value, end_value, selected_col

def slice_data_frame(given_df, start_value, end_value, selected_col):
    '''
    Slices the original DataFrame object to create a new
        DataFrame within the user-requested values
    Parameter given_df: DataFrame to drawn slice from
    Parameter start_value: index to start with
    Parameter end_value: index to end with
    Parameter selected_col: sliced column to return in a series
    Returns: new series object
    '''
    sliced_df = given_df.loc[start_value:end_value, :]
    new_ser = sliced_df[selected_col]

    return new_ser

def compute_stats(given_ser):
    '''
    Computes statistical values on a given series
    Parameter given_ser: series of values to analyze
    Returns: N/A
    '''
    sum_val = given_ser.sum()
    mean_val = given_ser.mean()
    std_val = given_ser.std()
    median_val = given_ser.median()
    min_val = given_ser.min()
    max_val = given_ser.max()
    
    new_ser = pd.Series([sum_val, mean_val, std_val, 
        median_val, min_val, max_val], index = ["Sum", "Mean", 
        "StdDev", "Median", "Smallest", "Largest"])

    new_ser.to_csv("statistics.csv")

def merge_frames(first_df, second_df, keyword):
    '''
    Joins two DataFrames together on a keyword
    Parameter first_df: primary DataFrame to use
    Parameter second_df: second DataFram to use
    Parameter keyword: attribute to join on
    Returns: combined DataFrame
    '''
    combined_df = first_df.merge(second_df, on = keyword)

    combined_df.to_csv("merged_data.csv")

    return combined_df

def split_apply_combine(given_df, selected_col):
    '''
    Separates a merged DataFrame into groups, applies mean,
        then combines means into a series, outputs it
        to a file
    Parameter given_df: a previously merged DataFrame
    Parameter selected_col: user-requested data column
    Returns: N/A
    '''
    grouped_by_week_day = given_df.groupby("Day of Week")

    new_ser = pd.Series(dtype = float)

    new_ser = grouped_by_week_day[selected_col].mean()

    new_ser.to_csv("daily_means.csv")