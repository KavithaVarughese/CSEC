import os
import subprocess

#table 
from prettytable import PrettyTable

# x = os.popen('python bf.py -e files/XML/001.xml out1').read()
# print(x)

# y = os.system('java des files/XML/001.xml out2')
# print(y)

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
    BFTime = 120
    # get string to run OS command for des
    string = 'java des files/XML/'+filenames+' out2'
    #store time in DESTime
    os.system(string)
    DESTime = 120
    #Add to table
    table.add_row(["XML",size,DESTime, BFTime])
    size=size+10

size = 10
for filenames in os.listdir('files/MP4'):
    #Get the string for OS command for blow fish
    string = 'python bf.py -e files/MP4/'+filenames+' out1'
    #get the time for blowfish 
    # store in BFTIME
    os.system(string)
    BFTime = 120
    # get string to run OS command for des
    string = 'java des files/MP4/'+filenames+' out2'
    #store time in DESTime
    os.system(string)
    DESTime = 120
    #Add to table
    table.add_row(["MP4",size,DESTime, BFTime])
    size=size+10


print(table)