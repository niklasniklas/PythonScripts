# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 21:38:53 2016

@author: NiclasLaptop

changeFilesWgui
changeMultipleFilenames_general
changeMultipleFilenames_images
QtMultipleFileSelection
"""


from PyQt4 import QtCore, QtGui
import os
import shutil
import sys


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


class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.resize(800,800)
        self.setMinimumSize(500,500)

        #horizGroupBox = QtGui.QGroupBox(self)
        #horizGroupBox.setTitle("Input files")
        self.buttonload = QtGui.QPushButton('Add files...', self)
        self.listWgt = QtGui.QListWidget(self)
        loadLayout = QtGui.QGridLayout(self)
        loadLayout.addWidget(self.loadButton,  0,0)
        loadLayout.addWidget(self.listWgt,0,1)
        
        
        #        http://stackoverflow.com/questions/21478270/pyqt-how-to-add-a-grid-layout-inside-a-qgroupbox-in-pyqt4
        
        
        
        """
        # input        
        self.button1 = QtGui.QPushButton('Choose files...', self)
        self.listWgt = QtGui.QListWidget(self)
        
        # output
        self.button2 = QtGui.QPushButton('Change outputfolder...', self)
        self.labelPath = QtGui.QLabel(self)
        self.edit1 = QtGui.QLineEdit(self)
        self.edit2 = QtGui.QLineEdit(self)
        
        self.button1.setMinimumWidth(200)
        
        layout1 = QtGui.QHBoxLayout(self)
        layout1.addWidget(self.button1)
        layout1.addWidget(self.button2)
      
        layout = QtGui.QGridLayout(self)
        #layout.addLayout(layout1,1,1)
        layout.addWidget(self.button1, 0, 0)
        layout.addWidget(self.listWgt, 1, 0, 1, 1)
        layout.addWidget(self.button2, 0, 1)
        #layout.addWidget(self.labelPath, 1, 1)
        layout.addWidget(self.edit1, 2, 1)
        layout.addWidget(self.edit2, 3, 1)
        

        #layout = QtGui.QVBoxLayout(self)
        #layout.addWidget(self.button1)
        #layout.addWidget(self.button2)
        #layout.addWidget(self.listWgt)
        #layout.addWidget(self.labelPath)

        self.labelPath.setText("AAA")

        self.button1.clicked.connect(self.loadButton)
        self.button2.clicked.connect(self.secondButton)
        """     


    def secondButton(self):
        dialog= PathDialog()
        if dialog.exec_() == QtGui.QDialog.Accepted:
            print dialog.selectFile()[0]
        self.labelPath.setText("2: Hej")
        item = QtGui.QListWidgetItem("Aaaa")
#        self.listWgt.addItem(item)
        

    def loadButton(self):
        dialog = FileDialog()
        if dialog.exec_() == QtGui.QDialog.Accepted:
            for i in range(0,len(dialog.selectedFiles())):
#                print dialog.selectedFiles()[i]
                item = QtGui.QListWidgetItem(dialog.selectedFiles()[i])
                self.listWgt.addItem(item)


if __name__ == '__main__':
#    os.mkdir("C:\\xxx\\copy")
#    shutil.copy("C:\\xxx\\aaa.jpg","C:\\xxx\\copy\\cccc.jpg")
#    shutil.move(os.path.join(path,files),newfile)
#    n = 101
#    sum = 0
#    for i in range(1,n):
#        print i
#        sum = sum + i
#    print sum

#    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
   
"""    
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