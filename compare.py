import os
import subprocess
import sys
import operator

#table
from prettytable import PrettyTable

#split encryption and decryption time
def splitTime (output):
    times = (output.decode('utf-8')).splitlines()
    return times

#looping through the files to print in table format
table = PrettyTable()
table.field_names = ["File Type", "File size", "DES Encryption Time", "DES Decryption Time", "Blowfish Encryption Time", "Blowfish Decryption Time"]

for filename in os.listdir('../encfiles'):
    file_stat = os.stat('../encfiles/'+filename)
    filesize = str(round(file_stat.st_size/(1024*1024),3))+"MB"
    #file extension
    file_extension = filename.split('.')

    #Get the string for OS command for blow fish
    string = '../encfiles/'+filename


    # storing Blowfish encryption time in variable BFTime
    # calling java program
    javaout = subprocess.Popen(['javac','Blowfish.java'])
    javaout = subprocess.Popen(['java','Blowfish',string, 'out1','out2'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = javaout.communicate();
    #obtaining digits from the byte format of the returned value
    times = splitTime(stdout)
    BFEncryptionTime = times[0]
    BFDecryptionTime = times[1]

    #storing DES encryption and decryption times
    javaout = subprocess.Popen(['javac','des.java'])
    javaout = subprocess.Popen(['java','des',string, 'out1','out2'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = javaout.communicate();
    #obtaining digits from the byte format of the returned value
    times = splitTime(stdout)
    DESEncryptionTime = times[0]
    DESDecryptionTime = times[1]

    #Add to table
    table.add_row([file_extension[1], filesize, DESEncryptionTime, DESDecryptionTime, BFEncryptionTime, BFDecryptionTime])

print(table.get_string(sort_key=operator.itemgetter(1, 0), sortby="File size"))
