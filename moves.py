#This is Lab 3 for Health Tech


#create a table that has: 
# Columns: patient ID, hours of sleep, 


#Read the Moves Steps App. 

import csv     # imports the csv module
import sys      # imports the sys module
import pandas as pd
df = pd.read_csv(sys.argv[1]) # opens the csv file


df2 = df[df.Activity == 'walking']

df3 = df2[['Date','Steps']]
df4 = df3.groupby(df3.Steps) 
df2.set_index('Date')