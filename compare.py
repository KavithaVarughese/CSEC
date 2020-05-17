import os
import subprocess

x = os.popen('python bf.py -e test.xml out1').read()
print(x)

y = os.system('java des test.xml out2')
print(y)

print("DONE")
