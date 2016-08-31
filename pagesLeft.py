#!/usr/bin/env python3

pagesRead = input('How many pages have you read?\n')
daysLeft = input('How many days do you have left?\n')
pagesRead1 = int(pagesRead)
daysLeft1 = int(daysLeft)
totalPages = #Insert total number of pages here

d = str((totalPages - pagesRead1) / daysLeft1)
pagesLeft = totalPages - int(pagesRead)
#Quickfix - need to round float to nearest hundredth.
    #This current version rounds down to nearest integer.
percentage = int(100*(pagesRead1 / totalPages)) 

if d.endswith('.0'):
	pagesPerDay = int((totalPages - pagesRead1) / daysLeft1)
else:
	pagesPerDay = int((totalPages - pagesRead1) / daysLeft1 + 1)

print('''\nYou have %s days left to read %s more pages:
You are %s%% done.
That is %s pages per day to finish your book.''' % (daysLeft, pagesLeft, percentage, pagesPerDay))
