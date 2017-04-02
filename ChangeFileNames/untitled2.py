# -*- coding: utf-8 -*-
"""
Created on Sun Mar 05 22:10:50 2017

@author: NiclasLaptop
"""

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class checkdemo(QWidget):
   def __init__(self, parent = None):
      super(checkdemo, self).__init__(parent)
      
      layout = QHBoxLayout()
      self.b1 = QCheckBox("Button1")
      self.b1.setChecked(True)
      self.b1.stateChanged.connect(lambda:self.btnstate(self.b1))
      layout.addWidget(self.b1)
		
      self.b2 = QCheckBox("Button2")
      self.b2.toggled.connect(lambda:self.btnstate(self.b2))

      layout.addWidget(self.b2)
      self.setLayout(layout)
      self.setWindowTitle("checkbox demo")

   def btnstate(self,b):
      if b.text() == "Button1":
         if b.isChecked() == True:
            print b.text()+" is selected"
         else:
            print b.text()+" is deselected"
				
      if b.text() == "Button2":
         if b.isChecked() == True:
            print b.text()+" is selected"
         else:
            print b.text()+" is deselected"
            
   def Checked1(self):
      msgBox = QtGui.QMessageBox()
      msgBox.setText("on_checkBox_stateChanged")
      msgBox.exec_()

				
def main():

   app = QApplication(sys.argv)
   ex = checkdemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
   