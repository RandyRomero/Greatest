#!python3

'''Exercise from Automate the Boring Stuff With Python. Find the folder in a directory tree that has the greatest number of files or the folder that uses the most disk space.'''

#def greatestNumber(path):
#def mostDiskSpace(path):

logFile = open('D:\\YandexDisk\\Studies\\Python\\Chapter 9\\GreatestNumberOfFiles\\logfile.txt', 'w')
logFile.write('Log file has created. Program has started.\n\n')

print('Hi there! Let\'s quickly get down to deal. \nIf you want to find a folder that contains the greatest number of files, press 1. \nIf you want to find a folder that uses the most disk space, press 2. \nYour answer is: ')
logFile.write('Hi there! Let\'s quickly get down to deal. \nIf you want to find a folder that contains the greatest number of files, press 1. \nIf you want to find a folder that uses the most disk space, press 2. Your answer is: ')

mode = input()
print('You have chosen ' + mode + '.')
logFile.write('User has chosen ' + mode + '.\n\n')


#TODO: ask user what does he want: folder with greatest number. Store answer as boolean
#TODO: ask user about directory
#TODO: check whether directory valind and exists
#TODO: launch on of two engines
#TODO: print out the result 