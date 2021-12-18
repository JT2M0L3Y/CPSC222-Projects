##############################################
# Programmer: Jonathan Smoley
# Class: CPSC 222-01, Fall 2021
# Data Assignment #1
# 9/16/20
# Description: This program computes a list of
#   common statistical calcualtions on a list
#   of exclusively floating-point numbers.
# Notes: I attempted the bonus!
##############################################
import math

# list of floating point numbers given
data_set = [84.4, 75.8, 42.1, 25.9, 51.1, 40.5, 78.4, 30.3, 47.7, 58.3, 90.8, 50.5, 28.2, 75.6, 61.8, 25.1, 91.0]

# take length of list (counts how many elements are in the list)
nums_count = len(data_set)
print("Number of floats in the data set:", round(float(nums_count), 2))

# take average of the data set using sum of and count of numbers
nums_avg = sum(data_set) / nums_count
print("Average of the data set:", round(float(nums_avg), 2))

# standard deviation of numbers using formula from given link and a for loop
std_dev = math.sqrt(sum(pow(num - nums_avg, 2) for num in data_set) / (nums_count - 1))
print("Standard Deviation for the data set:", round(float(std_dev), 2))

# sort data from smallest to largest, take value in middle of sorted list
sorted_set = sorted(data_set)
median_num = sorted_set[(nums_count // 2)]
print("Median of the data set:", round(float(median_num), 2))

# use standard min() function to find smallest number in data_set
smallest_num = min(data_set)
print("Smallest number in the data set:", round(float(smallest_num), 2))

# use standard max() function to find largest number in data_set
largest_num = max(data_set)
print("Largest number in the data set:", round(float(largest_num), 2))

# prompt user for start & end value for range of list values to double
start = int(input("Enter starting value in the data_set: "))
end = int(input("Enter an ending value in the data_set: "))

# replace values within user's given range with 0
modified_data = data_set.copy()
for num in range(start, end + 1):
    modified_data[num] = 0

# print list with replaced values
for i in modified_data:
    if i != len(modified_data):
        print(float(i), end = " ")
    else:
        print(i)

# print the original list, but in reverse
rev_data = data_set[::-1]

print()
for i in rev_data:
    if i != len(rev_data):
        print(i, end = " _ ")
    else:
        print(i)