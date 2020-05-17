import os
import subprocess

x = os.popen('python bf.py -e files/001.xml out1').read()
print(x)


# storing DES encryption time in variable javatime
# calling java program
javaout = subprocess.Popen(['java','des', '../test.xml', '../encxml'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
stdout,stderr = javaout.communicate();
stdout = str(stdout)
#obtaining digits from the byte format of the returned value
javatime = ''
for c in stdout:
    if c.isdigit():
        javatime=javatime+c
# print("Encryption Time for DES : " + javatime)

print("DONE")
