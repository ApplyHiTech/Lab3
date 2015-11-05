# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 17:03:46 2015

@author: francescoperera
"""

import datetime as dt
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

# Moves analysis

sedentaryThreshold=[5000]
lowActiveThreshold=[7499]
somewhatActiveThreshold=[9999]
highlyActiveThreshold=[12500]


def fileReader(x):

    DataList = []
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


def plotPatient(xData,yData):
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
    xval,yval=fileReader(x)
    plotPatient(xval,yval)


if __name__ == '__main__': 
    Francesco='Francesco_summary.csv'
    Daniel='Daniel_summary.csv'
    #plt.figure(1)
    #plt.subplot(211)
    movesAnalysis(Francesco)
    #plt.subplot(212)
    movesAnalysis(Daniel)
