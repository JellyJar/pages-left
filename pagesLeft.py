#!/usr/bin/env python3

#Here I'll add an option to create or open a text file containing book information
#Read current existing list
	#Create loopback if text file doesn't exist- "make sure text file isn't misplaced in another dir, deleted..."
#Writing information on a new line without overwriting

def info():
	bookInfo = input("Do you have your current book's information saved? (Y/N)\n").upper()

	# Don't quite know how to implement all of this yet
	if bookInfo == 'Y':
		a = open('BOOKINFO.txt', 'r')
		for line in a:
			print(line.strip('\n\r'))
		a.close()
		
	elif bookInfo == 'N':
		a = open('BOOKINFO.txt', 'w')

info()

#Old stuff- haven't touched this

pagesRead = int(input('How many pages have you read?\n'))  # you can convert to input to int
daysLeft = int(input('How many days do you have left?\n'))
totalPages = int(input('How many pages does your book have?\n'))  # Insert total number of pages here - this is currently just a place holder until I use a better method of keep track of pages per book

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
