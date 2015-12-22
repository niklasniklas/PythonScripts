# -*- coding: utf-8 -*-
"""
Created on Wed May 13 09:39:32 2015

Öppnar alla bilder (av ett visst format) och sparar om filen i en annan
mapp med nytt namn.

@author: NIAP
"""

from PIL import Image
import os
import shutil

""" ### Functions ### """
def get_imlist(path):
    """ Returns a list of filenames for
    all images in a directory. """
#    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.bmp')]
    return [os.path.join(path,f) for f in os.listdir(path) ]


def basics(path):
    print os.listdir(path)                                  # lista med filnamn
    print [os.path.join(path, x) for x in os.listdir(path)] # lista med path+filnamn
    


""" ### Main script ### """
path = "C:\\Temp\\xxx"
#basics(path)
name = 'NiclasFile_'
ii = 1000                   
for files in os.listdir(path):
#    filename = name + str(ii) + '.' + files.split(".",1)[1]
    filename = name + str(ii) + '.jpg' 
    newfile = os.path.join(path, filename)
    shutil.move(os.path.join(path,files),newfile)
    ii += 1
    
"""    
TODO:
 - Ändra ii = 1000 till 0000 (gör funktion som returnerar värde i string med 5? siffror som startar på 00000)
 - os.listdir(path) - ska den kunna sorteras? iså fall hur?
 - testa shuntil.copy2(src,dest) ifall inte ren rename
 - hämta filer från flera under mappar (ex. cd1, cd2, cd3 ...) och stoppa dem i en mapp
 - valbart vilken ändelse (.jpg eller behålla ursprungs-ändelse)?
 - valbart vilken katalog?
 - gui
 - kopiera istället för att skriva över
 


""" 
