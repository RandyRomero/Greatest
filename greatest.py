#!python3

'''Exercise from Automate the Boring Stuff With Python. Find the folder in a directory tree that has the greatest number of files or the folder that uses the most disk space.'''

import os

def prlog(message):
	#function that print user message and write to log file simultaneously
	print(message)
	logFile.write(message + '\n')

def greatestNumber(path):
	numberOfFiles = 0
	greatestFolder = ''
	for root, subfolders, files in os.walk(path):
		#exclude hidden folders
		subfolders[:] = [x for x in subfolders if not x.startswith('.')]  
		numberOfFilesInCurrentFolder = len(os.listdir(root))
		if numberOfFilesInCurrentFolder > numberOfFiles:
			numberOfFiles = numberOfFilesInCurrentFolder
			greatestFolder = root
			prlog(str(numberOfFiles))
			prlog(greatestFolder + '\n')

	prlog('*******************************************************')		
	prlog('A folder with the greatest number of files is this: ')
	prlog(greatestFolder)
	prlog('It contains {} files'.format(numberOfFiles))
	prlog('*******************************************************')
	prlog('\n')	

def mostDiskSpace(path):
	totalSize = 0
	heaviestFolder = ''
	haviestFolder = ''
	for root, subfolders, files in os.walk(path):
		
		totalSizeCurrentRoot = 0
		#exclude hidden folders
		subfolders[:] = [x for x in subfolders if not x.startswith('.')]
		files = [x for x in files if not x.startswith('.')]
		for file in files:
			try:
				totalSizeCurrentRoot += os.path.getsize(os.path.join(root, file))
			except FileNotFoundError:
				totalSizeCurrentRoot += os.path.getsize(os.path.join('\\\\?\\' + root, file))	
		
		if totalSizeCurrentRoot > totalSize:
			totalSize = totalSizeCurrentRoot
			heaviestFolder = root
			prlog(heaviestFolder)
			prlog(str(totalSize / 1024 / 1024) + ' MB')
			prlog('')

	prlog('*******************************************************')		
	prlog('A folder that uses the most disk space is this: ')
	prlog(heaviestFolder)
	prlog('Sum of its files is ' + str(totalSize / 1024 / 1024) + ' MB')
	prlog('*******************************************************')
	prlog('\n')				


logFile = open('.\\logfile.txt', 'w', encoding='UTF-8')
logFile.write('Log file has created. Program has started.\n\n')

############################### Choosing mode ###############################

while True:
	userMessage1 = 'Hi there! Let\'s quickly get down to deal. \nIf you want to find a folder that contains the greatest number of files, press 1. \nIf you want to find a folder that uses the most disk space, press 2. \nYour answer is: '
	mode = input(userMessage1)
	logFile.write(userMessage1 + ' \n\n')
	if mode == '1' or mode == '2':
		prlog('You have chosen ' +str(mode) + '.')
		break
	else:
		prlog('Error: you must choose 1 or 2. Try Again.\n')
		continue

############################### Asking path ##################################
		
while True:
	path = input('\nPlease write down path to directory: ')
	logFile.write('Please write down path to directory. User wrote: ' + path + '\n')
	if os.path.exists(path):
		print('Thank you.')
		logFile.write('Path exists.\n')
		break
	else:
		prlog('Error: try another address.')	
		continue

if mode == '1':
	greatestNumber(path)
else:
	mostDiskSpace(path)

prlog('Program has reached end. Ciao.')

#TODO: launch on of two engines
#TODO: print out the result 