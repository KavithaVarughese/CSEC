import os
import subprocess

x = os.popen('python bf.py -e files/001.xml out1').read()
print(x)

y = os.system('java des files/001.xml out2')
print(y)

print("DONE")
