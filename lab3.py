# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 17:03:46 2015

@author: francescoperera
"""

import datetime as dt
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import csv     # imports the csv module
import sys      # imports the sys module
import numpy as np
import pandas as pd

sedentaryThreshold=[5000]
lowActiveThreshold=[7499]
somewhatActiveThreshold=[9999]
highlyActiveThreshold=[12500]
sleepLowerThreshold=[6.5]
sleepUpperThreshold=[8]

############ Moves analysis

def movesFileReader(x):
    #DataList = []
    dates=[]
    newDates=[]
    stepsPerDay=[]
    movesFile=open(x)
    for line in movesFile:
        row=line.strip().split(',')
        if row[1]=="walking":
            dates.append(row[0])
            stepsPerDay.append(row[5])   
    for date in dates:
        if len(date)==8:
            newDate=date[:6]+"20"+date[6:]
        elif len(date)==7:
            newDate=date[:5]+"20"+date[5:]
        newDates.append(newDate)
    movesFile.close()
    return (newDates,stepsPerDay)
    
def plotMoves(xData,yData):
    xDate=[dt.datetime.strptime(date,'%m/%d/%Y') for date in xData ]
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    locator = mdates.DayLocator()
    locator.MAXTICKS = 4000
    plt.gca().xaxis.set_major_locator(locator)
    plt.plot(xDate,yData,'ob-')
    plt.plot(xDate,sedentaryThreshold *len(xData),'r')
    plt.plot(xDate,lowActiveThreshold *len(xData),'g')
    plt.plot(xDate,somewhatActiveThreshold *len(xData),'c')
    plt.plot(xDate,highlyActiveThreshold *len(xData),'m')
    plt.setp(plt.xticks()[1], rotation=60)
    plt.show()

def movesAnalysis(x):
    xval,yval=movesFileReader(x)
    plotMoves(xval,yval)

####### Self Report Analysis    
def selfReportReader(x):
    """this function takes the self report csv file and divides into two different csv files
    one for francesco and for daniel. These two csv files will be run on other functions"""
    df = pd.read_csv(x)
    #Convert Sleep column so we can deal with ints
    df.loc[df.Sleep=='4-5', 'Sleep'] = 4.5
    df.loc[df.Sleep=='5-6', 'Sleep'] = 5.5
    df.loc[df.Sleep=='6-7', 'Sleep'] = 6.5
    df.loc[df.Sleep=='7-8', 'Sleep'] = 7.5
    df2= df[['Timestamp','Sleep','ID']]
    df2.sort('Timestamp').groupby('ID')

    #Daniel's D.f. columns=Date,Sleep
    #Francesco's data frames columns=Date,Sleep
    df_Daniel= df2.loc[df2['ID'] == 'Daniel']
    df_Francesco = df2.loc[df2['ID']=='Francesco']
    df_Daniel.to_csv('Daniel_sleep.csv')
    df_Francesco.to_csv('Francesco_sleep.csv')

def sleepTimeGenerator(x):
    sleepHours=[]
    dates=[]
    sleepFile=open(x)
    for line in sleepFile:
        row=line.strip().split(',')
        dates.append(row[1])
        sleepHours.append(row[2])
    dates.pop(0)
    sleepHours.pop(0)
    return (dates,sleepHours)
    

def plotSelfReport(xData,yData):
    xDate=[dt.datetime.strptime(date,'%m/%d/%Y') for date in xData ]
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    locator = mdates.DayLocator()
    locator.MAXTICKS = 4000
    plt.gca().xaxis.set_major_locator(locator)
    plt.gca().set_ylim([4,8.5]) # the y-axis was set between 4 and 8.5 to provide 
    plt.plot(xDate,yData,'og-')
    plt.plot(xDate,sleepLowerThreshold *len(xData),'r')
    plt.plot(xDate,sleepUpperThreshold *len(xData),'r')
    plt.setp(plt.xticks()[1], rotation=60)
    plt.show()
    
def selfReportAnalysis(x):
    xval,yval=sleepTimeGenerator(x)
    plotSelfReport(xval,yval)

######### Empatica Analysis
def empaticaReader(x):
    #DataList = []
    dates=[]
    newDates=[]
    hrFrancesco=[]
    hrDaniel=[]
    hrFile=open(x)
    for line in hrFile:
        row=line.strip().split(',')
        dates.append(row[0])
        hrDaniel.append(row[1])
        hrFrancesco.append(row[2]) 
    dates.pop(0)
    hrFrancesco.pop(0)
    hrDaniel.pop(0)
    for date in dates:
        if len(date)==8:
            newDate=date[:6]+"20"+date[6:]
        elif len(date)==7:
            newDate=date[:5]+"20"+date[5:]
        newDates.append(newDate)
    hrFile.close()
    return (newDates,hrFrancesco,hrDaniel)

def plotEmpatica(xData,yData1,):
    xDate=[dt.datetime.strptime(date,'%m/%d/%Y') for date in xData ]
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    locator = mdates.DayLocator()
    locator.MAXTICKS = 4000
    plt.gca().xaxis.set_major_locator(locator)
    plt.plot(xDate,yData1,'ok-')
    plt.setp(plt.xticks()[1], rotation=60)
    plt.show()

def empaticaAnalysis(x):
    dates,hrPatient1,hrPatient2=empaticaReader(x)
    plotEmpatica(dates,hrPatient1) #hrPatient1=Francesco
    plotEmpatica(dates,hrPatient2) #hrPatient2=Daniel
    

if __name__ == '__main__': 
    # this function only needs to run once to generate Francesco_sleep.csv and Daniel_sleep.csv
    #selfReportReader('selfreport.csv')
    movesFrancesco='Francesco_summary.csv' # this csv file is the moves csv file for Francesco
    movesDaniel='Daniel_summary.csv' # this csv file is the moves csv file for Daniel
    selfReportFrancesco='Francesco_sleep.csv' # this csv file is self report file for Francesco
    selfReportDaniel='Daniel_sleep.csv' # this csv file is the self report file fro Daniel
    restingHeartRate='HeartRate.csv'
    movesAnalysis(movesFrancesco)
    movesAnalysis(movesDaniel)
    selfReportAnalysis(selfReportFrancesco)
    selfReportAnalysis(selfReportDaniel)
    empaticaAnalysis(restingHeartRate)
    
    """"
    1.The first plot is the moves plot for Francesco
    2.The second plot is the moves plot for Daniel
    3.The third plot is the self report plot for Francesco
    4.The fourth plot is the self report plot for Daniel
    5.The fifth plot is the empatica plot for Francesco
    6.The sixth plot is the empatica plot for Daniel
    """
    

