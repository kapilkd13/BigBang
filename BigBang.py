'''
Created on 29-Oct-2016

@author: kapil
'''
from tkinter.filedialog import askdirectory
from os import listdir,path,replace
from os import walk
import random
import string
import csv
foldername=askdirectory()
print(foldername)
fileslist=[f for f in listdir(path=foldername)]
print (fileslist)
print(''.join([random.SystemRandom().choice(string.ascii_letters+string.digits) for _ in range(10)]))
print(string.ascii_letters)
def getNewNames(dirname,filename):
    randomname=''.join([random.SystemRandom().choice(string.ascii_letters+string.digits) for _ in range(13)])\
    +'.txt'
    return path.join(dirname,randomname)

# with open('kapil.csv', mode='a') as fp:
#     writer=csv.writer(fp,delimiter='!')
#     for(dirpath, dirnames,filenames) in walk(foldername):
#         for file in filenames:
#             oldname=path.join(dirpath,file)
#             newname=getNewNames(dirpath, file)
#         #save file names to file
#             writer.writerow([oldname,newname])
#         #replace names 
#             replace(oldname,newname)
#      
with open('kapil.csv', mode='r') as fp:
    reader=csv.reader(fp,delimiter='!')
    for row in reader:
        try:
            replace(row[1],row[0])
        except FileNotFoundError:
            print(row[1]+' not found')
            
            
            
            