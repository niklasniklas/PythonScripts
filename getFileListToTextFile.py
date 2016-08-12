# -*- coding: utf-8 -*-
"""
Created on Wed May 13 09:39:32 2015

Öppnar alla bilder (av ett visst format) och sparar om filen i en annan
mapp med nytt namn.

@author: NIAP
"""

import os

""" ### Functions ### """
def get_imlist(path):
    """ Returns a list of filenames for
    all jpg images in a directory. """
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.bmp')]


def basics():
    lista = get_imlist("C:\\Temp\\xx")
    print lista[0]                                          # C:\Temp\xx\0001.bmp
    print os.path.basename(lista[0])                        # 0001.bmp
    print os.path.dirname(lista[0])                         # C:\Temp\xx    
    print os.path.splitext(os.path.basename(lista[0]))      # ('0001', '.bmp')
    print os.path.splitext(os.path.basename(lista[0]))[0]   # 0001
    print os.path.splitext(os.path.basename(lista[0]))[1]   # .bmp

    a = os.path.basename(lista[0])                          # 0001.bmp
    b = os.path.dirname(lista[0])                           # C:\Temp\xx    
    print os.path.join(b,a)                                 # C:\Temp\xx\0001.bmp



lista = os.listdir("C:\\xxxx")

print lista


"""

path = os.path.dirname(lista[0]) + "\\result"
if not os.path.exists(path):
    os.makedirs(path)

for filepath in lista:
    filename = os.path.splitext(os.path.basename(filepath))[0]
    im = Image.open(filepath)
    new_filename = "05_" + filename + os.path.splitext(filepath)[1]
    new_filepath = os.path.join(path,new_filename)
    print new_filepath
    im.save(new_filepath)

"""