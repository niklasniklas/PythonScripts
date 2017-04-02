# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 20:33:33 2017

@author: NiclasLaptop
"""

# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Application(QtGui.QWidget):
    """ Main application window """

    def __init__(self):
        super(Application, self).__init__()
        self.initUI()

    def initUI(self):
        self.openBtn = QtGui.QPushButton("Open", self)
        self.label = QtGui.QLabel("This is a test label", self)

        self.hBox = QtGui.QHBoxLayout()
        self.hBox.addWidget(self.openBtn)
        self.hBox.addWidget(self.label)

        self.group = QtGui.QGroupBox("Style")
        self.radioBtn1 = QtGui.QRadioButton("Button 1", self.group)
        self.radioBtn2 = QtGui.QRadioButton("Button 2", self.group)
        self.radioLayout = QtGui.QVBoxLayout(self.group)
        self.radioLayout.addWidget(self.radioBtn1)
        self.radioLayout.addWidget(self.radioBtn2)
        self.group.setLayout(self.radioLayout)

        self.hBox2 = QtGui.QHBoxLayout()
        self.hBox2.addWidget(self.group)

        self.vBox = QtGui.QVBoxLayout()
        self.vBox.addLayout(self.hBox2)
        self.vBox.addLayout(self.hBox)

        self.setLayout(self.vBox)
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    mainapp = Application()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    
    