import os
import subprocess
import sys
import operator

#table
import pandas as pd

#graph
import matplotlib.pyplot as plt

#split encryption and decryption time
def splitTime (output):
    times = (output.decode('utf-8')).splitlines()
    return times

#looping through the files to print in table format
table = pd.DataFrame(columns= ["File_Type", "File size", "DES Encryption Time", "DES Decryption Time", "Blowfish Encryption Time", "Blowfish Decryption Time"])

#sorting the files folder list
listfiles = os.listdir('encfiles')
listfiles.sort()

for filename in listfiles:
    file_stat = os.stat('encfiles/'+filename)
    filesize = str(round(file_stat.st_size/(1024*1024),3))+"MB"
    #file extension
    file_extension = filename.split('.')

    #Get the string for OS command for blow fish
    string = 'encfiles/'+filename


    # storing Blowfish encryption time in variable BFTime
    # calling java program
    javaout = subprocess.Popen(['javac','Blowfish.java'])
    javaout = subprocess.Popen(['java','Blowfish',string, 'out1','out2'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = javaout.communicate();
    #obtaining digits from the byte format of the returned value
    times = splitTime(stdout)
    BFEncryptionTime = int(times[0])
    BFDecryptionTime = int(times[1])

    #storing DES encryption and decryption times
    javaout = subprocess.Popen(['javac','des.java'])
    javaout = subprocess.Popen(['java','des',string, 'out1','out2'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = javaout.communicate();
    #obtaining digits from the byte format of the returned value
    times = splitTime(stdout)
    DESEncryptionTime = int(times[0])
    DESDecryptionTime = int(times[1])

    #Add to table
    new_row = {'File_Type':file_extension[1],'File size':filesize,'DES Encryption Time':DESEncryptionTime,'DES Decryption Time':DESDecryptionTime,'Blowfish Encryption Time':BFEncryptionTime,'Blowfish Decryption Time':BFDecryptionTime}
    table = table.append(new_row,ignore_index=True)

print(table)

#Encryption time for XML files
ax = plt.gca()

table[table.File_Type == 'xml'].plot(kind='line',x='File size',y='DES Encryption Time',ax=ax,title='Encryption Time vs File Size Graph for XML Files', marker = 'o')
table[table.File_Type == 'xml'].plot(kind='line',x='File size',y='Blowfish Encryption Time', color='red', ax=ax, marker = 'o')

plt.show()

#Encryption for MP4 Files

ax = plt.gca()

table[table.File_Type == 'mp4'].plot(kind='line',x='File size',y='DES Encryption Time',ax=ax,title='Encryption Time vs File Size Graph for MP4 Files', marker = 'o')
table[table.File_Type == 'mp4'].plot(kind='line',x='File size',y='Blowfish Encryption Time', color='red', ax=ax, marker = 'o')

plt.show()

#Encryption for MP3 Files

ax = plt.gca()

table[table.File_Type == 'mp3'].plot(kind='line',x='File size',y='DES Encryption Time',ax=ax,title='Encryption Time vs File Size Graph for MP3 Files', marker = 'o')
table[table.File_Type == 'mp3'].plot(kind='line',x='File size',y='Blowfish Encryption Time', color='red', ax=ax, marker = 'o')

plt.show()

#Decryption time for XML files
ax = plt.gca()

table[table.File_Type == 'xml'].plot(kind='line',x='File size',y='DES Decryption Time',ax=ax,title='Decryption Time vs File Size Graph for XML Files', marker = 'o')
table[table.File_Type == 'xml'].plot(kind='line',x='File size',y='Blowfish Decryption Time', color='red', ax=ax, marker = 'o')

plt.show()

#Decryption time for MP4 files
ax = plt.gca()

table[table.File_Type == 'mp4'].plot(kind='line',x='File size',y='DES Decryption Time',ax=ax,title='Decryption Time vs File Size Graph for MP4 Files', marker = 'o')
table[table.File_Type == 'mp4'].plot(kind='line',x='File size',y='Blowfish Decryption Time', color='red', ax=ax, marker = 'o')

plt.show()

#Decryption time for MP3 files
ax = plt.gca()

table[table.File_Type == 'mp3'].plot(kind='line',x='File size',y='DES Decryption Time',ax=ax,title='Decryption Time vs File Size Graph for MP3 Files', marker = 'o')
table[table.File_Type == 'mp3'].plot(kind='line',x='File size',y='Blowfish Decryption Time', color='red', ax=ax, marker = 'o')

plt.show()

ax = plt.gca()

table[table.File_Type == 'xml'].plot(kind='line',x='File size',y='DES Encryption Time',ax=ax,title='Encryption Time vs File Size Graph for All Files', marker = 'o', label ='xml')
table[table.File_Type == 'mp4'].plot(kind='line',x='File size',y='DES Encryption Time', color='red', ax=ax, marker = 'o', label='mp4')
table[table.File_Type == 'mp3'].plot(kind='line',x='File size',y='DES Encryption Time', color='green', ax=ax, marker = 'o',label='mp3')

plt.show()

ax = plt.gca()

table[table.File_Type == 'xml'].plot(kind='line',x='File size',y='Blowfish Encryption Time',ax=ax,title='Encryption Time vs File Size Graph for All Files', marker = 'o', label ='xml')
table[table.File_Type == 'mp4'].plot(kind='line',x='File size',y='Blowfish Encryption Time', color='red', ax=ax, marker = 'o', label='mp4')
table[table.File_Type == 'mp3'].plot(kind='line',x='File size',y='Blowfish Encryption Time', color='green', ax=ax, marker = 'o',label='mp3')

plt.show()