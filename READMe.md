1. Got Blowfish python implementation from https://github.com/vnn/OpenBSD/blob/master/bfcrypt.py

    Install pycryptodome for Crypto module to work for Blowfish
    Still didn't work, works in python 2. So, proceeding with that.

    Here, the key is not automatically generated, so chuck.

2. Got blowfish code from https://pypi.org/project/blowfish/#files

    for setup, following https://pypi.org/project/blowfish/
    Note .. these work with python 3
    Here also, we have to enter the key
    So I am sticking to the old one itself.
    Deleted both

3. Found Java implementation of DES but has a key generator from https://www.journaldev.com/1309/java-des-algorithm-program
    Disabled decrypyion 
    adding command line arguments