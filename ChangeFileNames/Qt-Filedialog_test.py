# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 08:42:36 2016

@author: NiclasLaptop
"""

"""
from PyQt4 import QtCore, QtGui

app = QtGui.QApplication([])
dialog = QtGui.QFileDialog()
dialog.setFileMode(QtGui.QFileDialog.Directory)
dialog.setOption(QtGui.QFileDialog.ShowDirsOnly)
dialog.exec_()
"""

"""
import sys
from PyQt4.QtGui import *
app = QApplication(sys.argv)
listWidget = QListWidget()
for i in range(10):
    item = QListWidgetItem("Item %i" % i)
    listWidget.addItem(item)
listWidget.show()
sys.exit(app.exec_())
"""
import sys
from PyQt4 import QtCore, QtGui

class MyWidget(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.button1 = QtGui.QPushButton('Test', self)
#        self.button1.clicked.connect(self.loadButton)
        self.button2 = QtGui.QPushButton('2', self)
#        self.button2.clicked.connect(self.secondButton)
        self.listWgt = QtGui.QListWidget(self)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.listWgt)
        self.listWgt.addItem("AA")
        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myWidgt = MyWidget()
    myWidgt.show()

    for i in range(5):
        myWidgt.listWgt.addItem("Hej %d" % i)    
    sys.exit(app.exec_())
