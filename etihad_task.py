# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 23:30:39 2019

@author: Danijel
"""

import pandas as pd
import numpy as np

file = pd.ExcelFile('C:/Users/Danijel/Desktop/Meteorological Data.xlsx')

#get all sheet names
sheet_names = file.sheet_names

df1 = pd.read_excel(file, sheet_names[0])
#print (df1["Maximum temperature (°C)"])
print ("MAX", np.abs(df1["Maximum temperature (°C)"]))
#number of rows and columns
df1.shape
#I believe this is a difficult question to answer because people will have different definitions of what the best weather is.
# I do know is that “best” is relative.
#the warmer the better

#Interestingly, other weather conditions such as humidity and levels of wind did not appear to 
#significantly alter the the participants' personality traits.
#And that's good news for Sydneysiders, because 22 degrees is roughly the average temperature of Sydney in December.
# Perth is also in luck with an average December temperature hovering around 22 before things really heat up to 25 degrees for the rest of summer.

#The psychology researchers conclude with a warning: as climate change brings higher average temperatures and greater extremes, our personality traits may gradually shift.

#There are many cities in the world that have the same weather conditions throughout the year. 
#Sydney - The city has 340 sunny days a year 
#Sunshine is delicious, rain is refreshing, wind braces us up, snow is exhilarating; there is really no such thing as bad weather, only different kinds of good weather. John Ruskin
