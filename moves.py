# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:07:46 2015

@author: francescoperera
"""
import matplotlib.pyplot as plt

myDataList = []
dates=[]
stepsPerDay=[]
moves=open('summary_2015-10.csv')
count=0
for line in moves:
    row=line.strip().split(',')
    myDataList.append(row)

for array in myDataList:
     if array[1]=="walking":
         dates.append(array[0])
         stepsPerDay.append(array[5])



     