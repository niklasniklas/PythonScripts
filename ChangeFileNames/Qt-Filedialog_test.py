# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 08:42:36 2016

@author: NiclasLaptop
"""

#from PySide import QtGui
from PyQt4 import QtCore, QtGui

app = QtGui.QApplication([])
dialog = QtGui.QFileDialog()
dialog.setFileMode(QtGui.QFileDialog.Directory)
dialog.setOption(QtGui.QFileDialog.ShowDirsOnly)
dialog.exec_()
