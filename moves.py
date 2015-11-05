# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:07:46 2015

@author: francescoperera
"""
import datetime as dt
import matplotlib.dates as mdates
import matplotlib.pyplot as plt


sedentaryThreshold=[5000]
lowActiveThreshold=[7499]
somewhatActiveThreshold=[9999]
highlyActiveThreshold=[12500]

# Francesco's Moves analysis

myDataListFrancesco = []
datesFrancesco=[]
newDatesFrancesco=[]
stepsPerDayFrancesco=[]

movesFrancesco=open('Francesco_summary.csv')

for line in movesFrancesco:
    row=line.strip().split(',')
    if row[1]=="walking":
        datesFrancesco.append(row[0])
        stepsPerDayFrancesco.append(row[5])
        

for array in myDataListFrancesco:
     if array[1]=="walking":
         datesFrancesco.append(array[0])
         stepsPerDayFrancesco.append(array[5])


for date in datesFrancesco:
    if len(date)==8:
        newDate=date[:6]+"20"+date[6:]
    elif len(date)==7:
        newDate=date[:5]+"20"+date[5:]   
    newDatesFrancesco.append(newDate)
        

print datesFrancesco
print
print stepsPerDayFrancesco


xDateFrancesco=[dt.datetime.strptime(newDate,'%m/%d/%Y').date() for newDate in newDatesFrancesco]

# this graph shows Francesco's stepsPerDay
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(xDateFrancesco,stepsPerDayFrancesco,'ob-')
plt.plot(xDateFrancesco,sedentaryThreshold *len(xDateFrancesco),'r')
plt.plot(xDateFrancesco,lowActiveThreshold *len(xDateFrancesco),'g')
plt.plot(xDateFrancesco,somewhatActiveThreshold *len(xDateFrancesco),'c')
plt.plot(xDateFrancesco,highlyActiveThreshold *len(xDateFrancesco),'m')

plt.setp(plt.xticks()[1], rotation=60)
#plt.gcf().autofmt_xdate()
plt.show()


# Daniel's Moves analysis

myDataListDaniel = []
datesDaniel=[]
newDatesDaniel=[]
stepsPerDayDaniel=[]

movesDaniel=open('Daniel_summary.csv')
count=0
for line in movesDaniel:
    row=line.strip().split(',')
    myDataListDaniel.append(row)

for array in myDataListDaniel:
     if array[1]=="walking":
         datesDaniel.append(array[0])
         stepsPerDayDaniel.append(array[5])

for date in datesDaniel:
    if len(date)==8:
        newDate=date[:6]+"20"+date[6:]
    elif len(date)==7:
        newDate=date[:5]+"20"+date[5:]   
    newDatesDaniel.append(newDate)
        

xDateDaniel=[dt.datetime.strptime(newDate,'%m/%d/%Y').date() for newDate in newDatesDaniel]

# this graph shows Daniel's stepsPerDay 
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(xDateDaniel,stepsPerDayDaniel,'ob-')
plt.plot(xDateDaniel,sedentaryThreshold *len(xDateDaniel),'r')
plt.plot(xDateDaniel,lowActiveThreshold *len(xDateDaniel),'g')
plt.plot(xDateDaniel,somewhatActiveThreshold *len(xDateDaniel),'c')
plt.plot(xDateDaniel,highlyActiveThreshold *len(xDateDaniel),'m')

plt.setp(plt.xticks()[1], rotation=60)
#plt.gcf().autofmt_xdate()
plt.show()

# following graph includes both Francesco's and Daniel's stepsPerDay plots
#blue plot shows Daniel's steps per day
#black plot shows Francesco's steps per day

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(xDateDaniel,stepsPerDayDaniel,'ob-')
plt.plot(xDateFrancesco,stepsPerDayFrancesco,'ok-')
plt.plot(xDateDaniel,sedentaryThreshold *len(xDateDaniel),'r')
plt.plot(xDateDaniel,lowActiveThreshold *len(xDateDaniel),'g')
plt.plot(xDateDaniel,somewhatActiveThreshold *len(xDateDaniel),'c')
plt.plot(xDateDaniel,highlyActiveThreshold *len(xDateDaniel),'m')

plt.setp(plt.xticks()[1], rotation=60)
#plt.gcf().autofmt_xdate()
plt.show()




     