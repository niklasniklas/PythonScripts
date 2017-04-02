# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 21:51:51 2017

@author: NiclasLaptop
"""

#from PyQt4 import QtCore

import math

x = 3
number = 2

if number == 0:
    print str(x)
    
aa = ""
length = len(str(x))
exponent = math.floor(math.log10(number))

print length
print exponent 

for i in range(int(exponent)-length+1) : 
    print "loop: "+ str(i)
    aa = aa + "0"

aa = aa + str(x)

print aa

