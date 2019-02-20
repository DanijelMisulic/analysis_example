# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 23:30:39 2019

@author: Danijel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.ExcelFile('C:/Users/Danijel/Desktop/Meteorological Data.xlsx')

#get all sheet names
sheet_names = data.sheet_names
min_difference = np.inf
min_index = -1

for i in range (0, len(sheet_names)):
    #load one sheet at a time
    df1 = pd.read_excel(data, i)

    #GETTING TO KNOW THE DATA

    #number of rows and columns
    df1.shape

    df1.dtypes

    #checking if there are still missing values after update of the file
    df1[df1["Maximum temperature (°C)"].isnull() == True].shape
    df1[df1["Minimum temperature (°C)"].isnull() == True].shape

    #checking for outliers
    np.max(df1["Maximum temperature (°C)"])
    np.min(df1["Maximum temperature (°C)"])
    np.max(df1["Minimum temperature (°C)"])
    np.min(df1["Minimum temperature (°C)"])
    
    #compute average temperature on a daily basis
    day_to_day_avg = np.round((df1["Maximum temperature (°C)"] + df1["Minimum temperature (°C)"])/2, 1)
    
    if np.abs(np.average(day_to_day_avg) - 22) < min_difference:
        min_difference = np.abs(np.average(day_to_day_avg) - 22)
        min_index = i
    
    
    n_groups = 1
    means_city = (np.average(day_to_day_avg))
    means_22 = (22)
     
    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8
     
    rects1 = plt.bar(index, means_city, bar_width,
    alpha=opacity,
    color='b',
    label=sheet_names[i].split(" ")[0])
     
    rects2 = plt.bar(index + bar_width, means_22, bar_width,
    alpha=opacity,
    color='g',
    label='22 Celsius')
     
    plt.ylabel('Average temperature')
    plt.title('Differences')
    plt.legend()
     
    plt.tight_layout()
    plt.show()

    
    
    
print ("The city that has the smallest difference to the hapiest average temp of 22 is ",sheet_names[min_index].split(" ")[0], "with average difference of",min_difference)