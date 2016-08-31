#!/usr/bin/env python3
pagesRead = int(input('How many pages have you read?\n'))  # you can convert to input to int
daysLeft = int(input('How many days do you have left?\n'))
totalPages = input(# Insert total number of pages here)

d = str((totalPages - pagesRead) / daysLeft)
pagesLeft = totalPages - int(pagesRead)
percentage = round(100*(pagesRead / totalPages), 2)  # rounds float to nearest hundredth

if d.endswith('.0'):
	pagesPerDay = int((totalPages - pagesRead) / daysLeft)
else:
	pagesPerDay = int((totalPages - pagesRead) / daysLeft + 1)

print('''\nYou have %s days left to read %s more pages:
You are %s%% done.
That is %s pages per day to finish your book.''' % (daysLeft, pagesLeft, percentage, pagesPerDay))
