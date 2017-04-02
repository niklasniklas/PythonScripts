# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 20:33:33 2017

@author: NiclasLaptop
"""

# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import math
import os
import shutil


class PathDialog(QtGui.QFileDialog):
    def __init__(self, *args, **kwargs):
        super(PathDialog, self).__init__(*args, **kwargs)
        self.setFileMode(QtGui.QFileDialog.Directory)
        self.setOption(QtGui.QFileDialog.ShowDirsOnly, True)

    def accept(self):
        QtGui.QDialog.accept(self)



class FileDialog(QtGui.QFileDialog):
    def __init__(self, *args, **kwargs):
        super(FileDialog, self).__init__(*args, **kwargs)
#        self.setFileMode(QtGui.QFileDialog.Directory)
#        self.setOption(QtGui.QFileDialog.ShowDirsOnly, True)
#        self.setOption(QtGui.QFileDialog.DontUseNativeDialog, True)
        self.setFileMode(QtGui.QFileDialog.ExistingFiles)

    def accept(self):
        QtGui.QDialog.accept(self)


class Application(QtGui.QWidget):
    """ Main application window """

    def __init__(self):
        super(Application, self).__init__()
        self.initUI()

    def initUI(self):
        #left side
        self.leftGroup  = QtGui.QGroupBox("Input")
        self.loadBtn    = QtGui.QPushButton("Load...", self.leftGroup)
        self.upBtn     = QtGui.QPushButton("Move Up", self.leftGroup)
        self.downBtn    = QtGui.QPushButton("Move Down", self.leftGroup)
        self.updownLine = QtGui.QHBoxLayout()
        self.updownLine.addWidget(self.upBtn)
        self.updownLine.addWidget(self.downBtn)
        self.fileList   = QtGui.QListWidget(self.leftGroup)
        self.noOfFiles  = QtGui.QLabel("No of files in list: 0",self.leftGroup)
        self.removeBtn  = QtGui.QPushButton("Clear all", self.leftGroup)
        self.leftBox = QtGui.QVBoxLayout(self.leftGroup)
        self.leftBox.addWidget(self.loadBtn)
        self.leftBox.addLayout(self.updownLine)
        self.leftBox.addWidget(self.fileList)
        self.leftBox.addWidget(self.noOfFiles)
        self.leftBox.addWidget(self.removeBtn)
        self.leftGroup.setLayout(self.leftBox)
        # -- convert box to layout
        self.leftSide = QtGui.QVBoxLayout()
        self.leftSide.addWidget(self.leftGroup)
        
        
        #middle        
        self.copyBtn    = QtGui.QPushButton(">>", self)
        self.copyBtn.setMaximumSize(30,50)
        

        #self.group2 = QtGui.QGroupBox("Style")
        #self.radioBtn3 = QtGui.QRadioButton("Button 3", self.group2)
        #self.radioBtn4 = QtGui.QRadioButton("Button 4", self.group2)
        #self.radioLayout1 = QtGui.QVBoxLayout(self.group2)
        #self.radioLayout1.addWidget(self.radioBtn3)
        #self.radioLayout1.addWidget(self.radioBtn4)
        #self.group2.setLayout(self.radioLayout1)

        #right side ---
        self.rightGroup  = QtGui.QGroupBox("Output")
        #line1
        self.check1      = QtGui.QCheckBox("Pre-Text", self.rightGroup)
        self.edit1       = QtGui.QLineEdit(self.rightGroup)
        self.line1       = QtGui.QHBoxLayout()
        self.line1.addWidget(self.check1)
        self.line1.addWidget(self.edit1)
        #line2
        self.check2      = QtGui.QCheckBox("No.", self.rightGroup)
        self.label2      = QtGui.QLabel("Start at:", self.rightGroup)
        self.spinbox2    = QtGui.QSpinBox(self.rightGroup)
        self.check21     = QtGui.QCheckBox("", self.rightGroup)
        self.label21     = QtGui.QLabel("No of dgts", self.rightGroup)
        self.spinbox21   = QtGui.QSpinBox(self.rightGroup)
        self.line2       = QtGui.QHBoxLayout()
        self.line2.addWidget(self.check2)
        self.line2.addWidget(self.label2)
        self.line2.addWidget(self.spinbox2)   
        self.line2.addWidget(self.check21)
        self.line2.addWidget(self.label21)
        self.line2.addWidget(self.spinbox21)   
        
        
        #line2_1
        self.radio6      = QtGui.QRadioButton("Filename",self.rightGroup)
        #self.check6      = QtGui.QCheckBox("Mid-text", self.rightGroup)
        self.edit6       = QtGui.QLineEdit(self.rightGroup)
        self.line6       = QtGui.QHBoxLayout()
        self.line6.addWidget(self.radio6)
        self.line6.addWidget(self.edit6)
        
        #line3
        self.radio3      = QtGui.QRadioButton("", self.rightGroup)
        #self.check3      = QtGui.QCheckBox("", self.rightGroup)
        self.fileList3   = QtGui.QTextEdit(self.rightGroup)
        self.line3       = QtGui.QHBoxLayout()
        self.line3.addWidget(self.radio3)
        self.line3.addWidget(self.fileList3)
        
        #line3_1
        self.check7      = QtGui.QCheckBox("End-text", self.rightGroup)
        self.edit7       = QtGui.QLineEdit(self.rightGroup)
        self.line7       = QtGui.QHBoxLayout()
        self.line7.addWidget(self.check7)
        self.line7.addWidget(self.edit7)
        
        #line4
        self.check4      = QtGui.QCheckBox("No.", self.rightGroup)
        self.label4      = QtGui.QLabel("Start at:", self.rightGroup)
        self.spinbox4    = QtGui.QSpinBox(self.rightGroup)
        self.line4       = QtGui.QHBoxLayout()
        self.line4.addWidget(self.check4)
        self.line4.addWidget(self.label4)
        self.line4.addWidget(self.spinbox4)   
        
        #line5
        self.check5      = QtGui.QCheckBox("", self.rightGroup)
        self.label5      = QtGui.QLabel("Extension", self.rightGroup)
        self.edit5   = QtGui.QLineEdit(self.rightGroup)
        self.line5       = QtGui.QHBoxLayout()
        self.line5.addWidget(self.check5)
        self.line5.addWidget(self.label5)
        self.line5.addWidget(self.edit5)

        self.label8        = QtGui.QLabel("Output Dir:",self.rightGroup)
        self.edit8         = QtGui.QLineEdit(self.rightGroup)
        self.outputDirBtn  = QtGui.QPushButton("Output dir...", self.rightGroup)
        self.line8         = QtGui.QHBoxLayout()
        self.line8.addWidget(self.label8)
        self.line8.addWidget(self.edit8)
        self.line8.addWidget(self.outputDirBtn)        
        
        self.rightBox = QtGui.QVBoxLayout(self.rightGroup)

        self.rightBox.addLayout(self.line1)
        self.rightBox.addLayout(self.line2)
        self.rightBox.addLayout(self.line6)
        self.rightBox.addLayout(self.line3)
        self.rightBox.addLayout(self.line7)
        self.rightBox.addLayout(self.line4)
        self.rightBox.addLayout(self.line5)
        self.rightBox.addLayout(self.line8)
        
        self.rightGroup.setLayout(self.rightBox)

        self.generateBtn   = QtGui.QPushButton("Generate")
        self.exampleLabel  = QtGui.QLabel("Example:")

        # convert box to layout
        self.rightSide = QtGui.QVBoxLayout()
        self.rightSide.addWidget(self.rightGroup)
        self.rightSide.addWidget(self.exampleLabel)
        self.rightSide.addWidget(self.generateBtn)
        
        # - end right side


        """
        self.group = QtGui.QGroupBox("Style")
        self.check1 = QtGui.QCheckBox("No", self.group)
        self.radioBtn2 = QtGui.QRadioButton("Button 2", self.group)
        self.radioLayout = QtGui.QVBoxLayout(self.group)
        self.radioLayout.addWidget(self.check1)
        self.radioLayout.addWidget(self.radioBtn2)
        self.group.setLayout(self.radioLayout)

        self.hBox2 = QtGui.QVBoxLayout()
        self.hBox2.addWidget(self.group)

        self.xx = QtGui.QLineEdit()
        """
        # the whole layout - add all parts to layout
        self.programLayout = QtGui.QHBoxLayout()
        self.programLayout.addLayout(self.leftSide)
        self.programLayout.addWidget(self.copyBtn)
        #self.programLayout.addLayout(self.hBox2)
        self.programLayout.addLayout(self.rightSide)
        #self.programLayout.addWidget(self.xx)

        self.setLayout(self.programLayout)
        self.show()
        
        self.check1.setChecked(False)
        self.check2.setChecked(True)
        self.check21.setChecked(False)
        self.radio3.setChecked(False)
        self.check4.setChecked(False)
        self.check5.setChecked(False)
        self.radio6.setChecked(True)
        self.check7.setChecked(False)

        # connect Signals and Slots        
        #---left
        self.loadBtn.clicked.connect(self.loadButton)
        #--middle
        self.copyBtn.clicked.connect(self.copyButton)
        #---right        
        self.check1.clicked.connect(self.Clk_check1)
        self.check2.clicked.connect(self.Clk_check2)
        self.check21.clicked.connect(self.Clk_check21)
        self.radio3.clicked.connect(self.Clk_check3)
        self.radio3.clicked.connect(self.Clk_check6)
        self.check4.clicked.connect(self.Clk_check4)
        self.check5.clicked.connect(self.Clk_check5)
        self.radio6.clicked.connect(self.Clk_check6)
        self.radio6.clicked.connect(self.Clk_check3)
        self.check7.clicked.connect(self.Clk_check7)
        
        self.check1.clicked.connect(self.UpdatePreview)
        self.check2.clicked.connect(self.UpdatePreview)
        self.check21.clicked.connect(self.UpdatePreview)
        self.radio3.clicked.connect(self.UpdatePreview)
        self.radio3.clicked.connect(self.UpdatePreview)
        self.check4.clicked.connect(self.UpdatePreview)
        self.check5.clicked.connect(self.UpdatePreview)
        self.radio6.clicked.connect(self.UpdatePreview)
        self.radio6.clicked.connect(self.UpdatePreview)
        self.check7.clicked.connect(self.UpdatePreview)

        self.edit1.textChanged.connect(self.UpdatePreview)
        self.spinbox2.valueChanged.connect(self.UpdatePreview)
        self.spinbox21.valueChanged.connect(self.UpdatePreview)
        self.fileList3.textChanged.connect(self.UpdatePreview)
        self.spinbox4.valueChanged.connect(self.UpdatePreview)
        self.edit5.textChanged.connect(self.UpdatePreview)  
        self.edit6.textChanged.connect(self.UpdatePreview)
        self.edit7.textChanged.connect(self.UpdatePreview)
        
        self.outputDirBtn.clicked.connect(self.SelectOutputDir)
        self.generateBtn.clicked.connect(self.GenerateFiles)
        
        self.edit8.setText("C:\Temp")
        self.edit8.setDisabled(True)        
        
        self.Clk_check1()
        self.Clk_check2()
        self.Clk_check21()
        self.Clk_check3()
        self.Clk_check4()
        self.Clk_check5()
        self.Clk_check6()
        self.Clk_check7()
        self.Clk_check8()
        
    def SelectOutputDir(self):
        dialog = PathDialog()
        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.edit8.setText(dialog.selectedFiles()[0])
            
            
        
    def GenerateFiles(self) :
        if (self.fileList.count() == 0):
            print "Empty"
            msgBox = QtGui.QMessageBox()
            msgBox.setText("Input list empty!")
            msgBox.show()
        else:            
            for ii in range(self.fileList.count()):
                src = os.path._getfullpathname(self.fileList.item(ii).text())
                dest = self.edit8.text() + "\\" + self.getNewFilename(ii) 
                print src
                print dest
                shutil.copy2(src,dest)
                #print self.fileList.document().findBlockByLineNumber(ii).text()
                #print os.path.basename(self.fileList.item(ii).text())
                #print os.path._getfullpathname(self.fileList.item(ii).text())
                #print os.path.dirname(self.fileList.item(ii).text())



    def getSpinboxValue(self, x):
        number = self.fileList.count()
        if number == 0:
            return str(x)
            
        aa = ""
        length = len(str(x))
        exponent = math.floor(math.log10(number)) + 1
        if self.check21.isChecked() :
            if self.spinbox21.value() > exponent :
                tmp2 = self.spinbox21.value()
            else:
                tmp2 = exponent
        else:
            tmp2 = exponent
        for i in range(int(tmp2)-length) : 
            aa = aa + "0"
        
        aa = aa + str(x)
        return aa


    def copyButton(self):
        for i in range(self.fileList.count()):
            #print os.path.basename(self.fileList.item(i).text())
            item = os.path.splitext(os.path.basename(self.fileList.item(i).text()))[0]   # 0001
            self.fileList3.append(item)


    def getNewFilename(self, number):
        if self.check1.isChecked():
            part1 = self.edit1.text()
        else:
            part1 = ""
            
        if self.check2.isChecked():
            part2 = str(self.getSpinboxValue(self.spinbox2.value()+number))
        else:
            part2 = ""
            
        if self.radio6.isChecked():
            part21 = self.edit6.text()
        else:
            part21 = ""
                
        if self.radio3.isChecked():
            #part3 = "_" + self.fileList3.document().findBlockByLineNumber(0).text()
            part3 = self.fileList3.document().findBlockByLineNumber(number).text()
        else:
            part3 = ""
            
        if self.check7.isChecked():
            part31 = self.edit7.text()
        else:
            part31 = ""
            
        if self.check4.isChecked():
            part4 = str(self.spinbox4.value()+number)
        else:
            part4 = ""
            
        if self.check5.isChecked():
            part5 = self.edit5.text()
        else:
            if self.fileList.count() == 0:
                part5 = ""
            else:
                part5 = os.path.splitext(os.path.basename(self.fileList.item(number).text()))[1]    #file ext
        return part1 + part2 + part21 + part3 + part31 + part4 + "." + part5

   
    def UpdatePreview(self):
       text = "Ex:" + self.getNewFilename(0)
       self.exampleLabel.setText(text)


    def loadButton(self):
        dialog = FileDialog()
        if dialog.exec_() == QtGui.QDialog.Accepted:
            for i in range(0,len(dialog.selectedFiles())):
#                print dialog.selectedFiles()[i]
                item = QtGui.QListWidgetItem(dialog.selectedFiles()[i])
                self.fileList.addItem(item)


 
    def Clk_check1(self):
        if self.check1.isChecked() == False:
            self.edit1.setDisabled(1)
        else:
            self.edit1.setEnabled(1)
        
    def Clk_check2(self):
        if self.check2.isChecked() == False:
            self.spinbox2.setDisabled(1)
        else:
            self.spinbox2.setEnabled(1)
             
    def Clk_check21(self):
        if self.check21.isChecked() == False:
            self.spinbox21.setDisabled(1)
        else:
            self.spinbox21.setEnabled(1)
             
    def Clk_check3(self):
        if self.radio3.isChecked() == False:
            self.fileList3.setDisabled(1)
        else:
            self.fileList3.setEnabled(1)

    def Clk_check4(self):
        if self.check4.isChecked() == False:
            self.spinbox4.setDisabled(1)
        else:
            self.spinbox4.setEnabled(1)

    def Clk_check5(self):
        if self.check5.isChecked() == False:
            self.edit5.setDisabled(1)
        else:
            self.edit5.setEnabled(1)

    def Clk_check6(self):
        if self.radio6.isChecked() == False:
            self.edit6.setDisabled(1)
        else:
            self.edit6.setEnabled(1)

    def Clk_check7(self):
        if self.check7.isChecked() == False:
            self.edit7.setDisabled(1)
        else:
            self.edit7.setEnabled(1)

    def Clk_check8(self):
        if self.check21.isChecked() == False:
            self.spinbox21.setDisabled(1)
        else:
            self.spinbox21.setEnabled(1)

    def Checked1(self):
        if self.check1.isChecked() == False:
            self.edit1.setDisabled(1)
        else:
            self.edit1.setEnabled(1)
            
        #msgBox = QtGui.QMessageBox()
        #msgBox.setText("on_checkBox_stateChanged")
        #msgBox.exec_()
            
    def secondButton(self):
        dialog= PathDialog()
        if dialog.exec_() == QtGui.QDialog.Accepted:
            print dialog.selectFile()[0]
        self.labelPath.setText("2: Hej")
        item = QtGui.QListWidgetItem("Aaaa")
#        self.listWgt.addItem(item)
        



def main():
    app = QtGui.QApplication(sys.argv)
    mainapp = Application()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    
    