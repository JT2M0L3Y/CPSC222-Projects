#################################
# CPSC 222 - DA5 Project Part 4 #
# Jonathan Smoley               #
# October 30, 2021              #
# This is the functions file    #
# I attempted the bonus task !  #
#################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

########## Programming Functions ##########

# load data
def read_patient_data(file):
    '''
    Description: This function reads in the patient data
        from the given .csv file path.
    Returns: a DataFrame with a set index and headers
    '''
    df = pd.read_csv(file, index_col = 'ID')

    return df

# clean data
def clean_marital(df, states):
    '''
    Description: This function applies a strict encoding
        system to the Marital Status column
    Returns: DataFrame with clean Marital Status column
    '''
    # encode the Marital Status column
    for val in df['Marital Status']:
        if ("sin" in val) or ("Sin" in val) or ("SIN" in val):
            df.replace(val, states[0], inplace = True)
        elif ("div" in val) or ("Div" in val) or ("DIV" in val):
            df.replace(val, states[1], inplace = True)
        elif ("mar" in val) or ("Mar" in val) or ("MAR" in val):
            df.replace(val, states[2], inplace = True)
        elif ("wid" in val) or ("Wid" in val) or ("WID" in val):
            df.replace(val, states[3], inplace = True)
        elif ("sep" in val) or ("Sep" in val) or ("SEP" in val):
            df.replace(val, states[4], inplace = True)
        else:
            df.replace(val, np.NaN, inplace = True)

    return df

def clean_RIC(df, ric_dict):
    '''
    Description: This function replaces the keys
        for RIC values with their paired values.
    Returns: DataFrame with clean RIC column
    '''
    df['RIC'].replace(ric_dict, inplace = True)

    return df

def write_data(df, file):
    '''
    Description: This function outputs the clean
        DataFrame to an output file.
    Returns: N/A
    '''
    # write clean data to an output file
    df.to_csv(file)

# aggregate data
def sum_patients(df):
    '''
    Description: This function adds up
        the number of patients listed
        in the dataset.
    Returns: the overall count
    '''
    patients = len(df)

    return patients

def compute_gender_totals(df):
    '''
    Description: This function counts the number
        of each gender listed in the dataset.
    Returns: male count, female count
    '''
    males = 0
    females = 0

    for gen in df['Gender']:
        if gen == 'M':
            males += 1
        elif gen == 'F':
            females += 1

    return males, females

def count_married(df):
    '''
    Description: This function counts the number
        of patients who are married.
    Return: married patient count
    '''
    married_total = 0
    for state in df['Marital Status']:
        if state == "Married":
            married_total += 1

    return married_total

def mc_ric_stats(df):
    '''
    Description: This function computes the # of 
        occurences of each RIC and finds the type
        with the most.
    Returns: most type and number of that type
    '''
    mc_ric = df['RIC'].value_counts().index[0]
    mc_ric_total = max(df['RIC'].value_counts())

    return mc_ric, mc_ric_total

def general_stroke_stats(df):
    '''
    Description: This function computes an
        average and standard deviation on all
        intances in the DataFrame.
    Returns: average and stdDev of stroke ages
    '''
    new_ser = df['Age'].where(df.loc[:,'RIC'] == "Stroke")
    new_ser.dropna(inplace = True)

    data_avg = new_ser.mean()
    data_std = new_ser.std()

    return round(data_avg, 2), round(data_std, 2)

def male_stroke_stats(df):
    '''
    Description: This function computes an
        average and standard deviation on male
        intances in the DataFrame.
    Returns: average and stdDev of stroke ages of males
    '''
    male_ser = df['Age'].where((df.loc[:,'RIC'] == "Stroke") & (df.loc[:,'Gender'] == 'M'))
    male_ser.dropna(inplace = True)

    male_avg = male_ser.mean()
    male_std = male_ser.std()

    return round(male_avg, 2), round(male_std, 2)

def female_stroke_stats(df):
    '''
    Description: This function computes an
        average and standard deviation on female
        intances in the DataFrame.
    Returns: average and stdDev of stroke ages of females
    '''
    female_ser = df['Age'].where((df.loc[:,'RIC'] == "Stroke") & (df.loc[:,'Gender'] == 'F'))
    female_ser.dropna(inplace = True)

    female_avg = female_ser.mean()
    female_std = female_ser.std()

    return round(female_avg, 2), round(female_std,2)

def output_stats(stats_ser):
    '''
    Description: This function outputs a 
        Series object of the statistics performed.
    Returns: N/A
    '''
    print(stats_ser)

# plot data
def get_age_data(item):
    '''
    Description: This function finds the age-related
        data associated with the current RIC type.
    Returns: mean, std_dev
    '''
    mean = round(item['Age'].mean(), 2)
    std_dev = round(item['Age'].std(), 2)

    return mean, std_dev

def plot_hist(key, item, count, mean, std_dev):
    '''
    Description: This function creates and outputs a
        histogram for each RIC type based on the
        age-related data.
    Returns: N/A
    '''
    plt.figure()

    # create/plot normal distribution line
    dist_line = norm.pdf(x = item['Age'], loc = mean, scale = std_dev)
    plt.plot(item['Age'], dist_line, color = 'red')

    # plot historgram bins
    plt.hist(item['Age'], bins = 30, color = 'green')

    # plot labels
    plt.title(key + " Age (N=" + str(count) + "): $ \mu $=" + str(mean) + ", $ \sigma $=" + str(std_dev))
    plt.xlabel("Age (Years)")
    plt.ylabel("Frequency")

    plt.show()

def get_male_scores(item):
    '''
    Description: This function finds the male-related
        data for the current RIC type.
    Returns: admission scores, discharge scores, male count
    '''
    admit_scores = item['Admission Total FIM Score'].where((item.loc[:,'Gender'] == 'M')).dropna()

    dis_scores = item['Discharge Total FIM Score'].where((item.loc[:,'Gender'] == 'M')).dropna()

    counts = admit_scores.value_counts().sum()

    return admit_scores, dis_scores, counts

def get_female_scores(item):
    '''
    Description: This function finds the female-related
        data for the current RIC type.
    Returns: admission scores, discharge scores, female count
    '''
    admit_scores = item['Admission Total FIM Score'].where((item.loc[:,'Gender'] == 'F')).dropna()

    dis_scores = item['Discharge Total FIM Score'].where((item.loc[:,'Gender'] == 'F')).dropna()

    counts = admit_scores.value_counts().sum()

    return admit_scores, dis_scores, counts

def plot_scatter(key, female_admit, female_dis, male_admit, male_dis, count, females, males):
    '''
    Description: This function creates and outputs
        a scatter plot for each RIC type based on
        the male and female data for admission
        and discharge RIC scores.
    Returns: N/A
    '''
    plt.figure()
    plt.scatter(female_admit, female_dis, s = 100, c = 'r', marker = '+')
    plt.scatter(male_admit, male_dis, s = 100, c = 'b', marker = '.')
    plt.plot(np.arange(0,140), c = 'black', linestyle = '--')
    plt.title(key + " (N=" + str(count) + ")")
    plt.xlabel("Admission Total FIM Score")
    plt.ylabel("Discharge Total FIM Score")
    plt.legend(["No Change", "Female (N=" + str(females) + ")", "Male (N=" + str(males) + ")"], loc = 'lower right')
    plt.show()

########## Project Part 4 Functions ##########

def load_data(file):
    '''
    Description: This function takes a file to read from 
        and reads data from said file into a DataFrame.
    Returns: new DataFrame filled with data
    '''
    df = pd.read_csv(file, index_col = 'Date')

    return df

def clean_data(df):
    '''
    Description: This function takes a pandas DataFrame
        and removes all the empty rows and columns.
    Returns: a clean pandas DataFrame
    '''
    df.dropna(axis = 0, how = 'all', thresh = 2, inplace = True)
    df.dropna(axis = 1, how = 'all', inplace = True)

    return df

def display_data(df):
    '''
    Description: plot data from the clean dataset
    Returns: N/A
    '''
    x_data = df.index
    y_data = df['Total Notifications']

    plt.bar(x = x_data, height = y_data, width = 0.5, bottom = None, align = 'edge', color = 'red', edgecolor = 'black')
    plt.title("Notification Data In October 2021")
    plt.xlabel("Date")
    plt.ylabel("Total Notifications")
    plt.xticks(ticks = x_data, rotation = 45)
    plt.show()
    