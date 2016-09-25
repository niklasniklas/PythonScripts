# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 23:09:33 2016

@author: NiclasLaptop
"""

#--------------

""" *** Hello World example ***

def printNA():
    print("Hello World")


printNA()
"""

class Missle:
    def __init__(self,xx,yy):
        self.x = xx
        self.y = yy
        
    #def
    #https://docs.python.org/2/tutorial/classes.html
        

# *** Matlab-plot example ***
import numpy as np
import matplotlib.pyplot as plt

msl = Missle(1,2)

print msl.x
print msl.y
print "aaa"

plt.figure(1)
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()

print "hej"

plt.figure(2)
# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
""" 
"""
#A simple example of an animated plot
"""

from PyQt4.QtGui import *

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)        # x-array
line, = ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x+i/10.0))  # update the data
    return line,

#Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
    interval=25, blit=True)
plt.show()


        
        
"""
        
