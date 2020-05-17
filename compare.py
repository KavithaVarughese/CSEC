import os
import subprocess

#table 
from prettytable import PrettyTable

#looping through the files to print in table format
table = PrettyTable()
table.field_names = ["File Type", "File size", "DES Time", "Blowfish Time"]


#FOR XML FILES
size = 10
for filenames in os.listdir('files/XML'):
    #Get the string for OS command for blow fish
    string = 'python bf.py -e files/XML/'+filenames+' out1'
    #get the time for blowfish 
    # store in BFTIME
    os.system(string)

    with open('bfval.txt') as f:
        BFTime = f.readline()


    # get string to run OS command for des
    string = 'files/XML/'+filenames

    # storing DES encryption time in variable DESTime
    # calling java program
    javaout = subprocess.Popen(['java','des',string, '../encxml'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = javaout.communicate();
    stdout = str(stdout)
    #obtaining digits from the byte format of the returned value
    DESTime = ''
    for c in stdout:
        if c.isdigit():
            DESTime=DESTime+c   

    #Add to table
    table.add_row(["XML",size,DESTime, BFTime])
    size=size+10


#MP4 files
size = 10
for filenames in os.listdir('files/MP4'):
    #Get the string for OS command for blow fish
    string = 'python bf.py -e files/MP4/'+filenames+' out1'
    #get the time for blowfish 
    # store in BFTIME
    os.system(string)
    
    with open('bfval.txt') as f:
        BFTime = f.readline()

    # get string to run OS command for des
    string = 'files/MP4/'+filenames

    # storing DES encryption time in variable DESTime
    # calling java program
    javaout = subprocess.Popen(['java','des',string, '../encxml'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = javaout.communicate();
    stdout = str(stdout)
    #obtaining digits from the byte format of the returned value
    DESTime = ''
    for c in stdout:
        if c.isdigit():
            DESTime=DESTime+c   

    #Add to table
    table.add_row(["MP4",size,DESTime, BFTime])
    size=size+10


print(table)

