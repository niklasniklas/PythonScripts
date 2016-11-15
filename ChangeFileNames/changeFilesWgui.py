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
        self.button1 = QtGui.QPushButton('Choose files...', self)
        self.button1.clicked.connect(self.loadButton)
        self.button2 = QtGui.QPushButton('Change outputfolder', self)
        self.button2.clicked.connect(self.secondButton)
        self.listWgt = QtGui.QListWidget(self)
        self.labelPath = QtGui.QLabel()
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.listWgt)
        layout.addWidget(self.labelPath)
        

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
 
#    currentRow = self.ventana.listWidget.currentRow()
#    currentItem = self.ventana.listWidget.takeItem(currentRow)
#    self.ventana.listWidget.insertItem(currentRow - 1, currentItem)