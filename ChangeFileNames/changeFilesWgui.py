# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 21:38:53 2016

@author: NiclasLaptop
"""


from PyQt4 import QtCore, QtGui
import os
import shutil


class FileDialog(QtGui.QFileDialog):
    def __init__(self, *args, **kwargs):
        super(FileDialog, self).__init__(*args, **kwargs)
        self.setOption(QtGui.QFileDialog.DontUseNativeDialog, True)
        self.setFileMode(QtGui.QFileDialog.ExistingFiles)

    def accept(self):
        QtGui.QDialog.accept(self)

class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.button = QtGui.QPushButton('Test', self)
        self.button.clicked.connect(self.loadButton)
        self.list = QtGui.QListView(self)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.button)
        layout.addWidget(self.list)

    def loadButton(self):
        dialog = FileDialog()
        print("Hej")
        print(dialog.selectedFiles())

        if dialog.exec_() == QtGui.QDialog.Accepted:
            print(dialog.selectedFiles())
            print(dialog.selectedFiles()[0])
            print(dialog.selectedFiles()[1])
            print(dialog.selectedFiles()[2])
            aa = dialog.selectedFiles()
            print len(aa)
            for file_i in dialog.selectedFiles:
                self.list.append(dialog.selectedFiles()[file_i])

if __name__ == '__main__':
    print 10
#    os.mkdir("C:\\xxx\\copy")
#    shutil.copy("C:\\xxx\\aaa.jpg","C:\\xxx\\copy\\cccc.jpg")
#    shutil.move(os.path.join(path,files),newfile)


    import sys
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