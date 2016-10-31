# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 16:19:03 2015

@author: NIAP
"""

from PyQt4 import QtCore, QtGui

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
        self.button.clicked.connect(self.handleButton)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.button)

    def handleButton(self):
        dialog = FileDialog()

        if dialog.exec_() == QtGui.QDialog.Accepted:
            print(dialog.selectedFiles())

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
    

"""
def loadFiles(self):

    filter = "TXT (*.txt);;PDF (*.pdf)"
    file_name = QtGui.QFileDialog()
    file_name.setFileMode(QFileDialog.ExistingFiles)
    names = file_name.getOpenFileNameAndFilter(self, "Open files", "C\\Desktop", filter)
    print names

if __name__ == '__main__':
    app = QApplication(sys.argv)

    filedialog = QFileDialog()
    #filedialog.setModal(True)
    filedialog.show()
    app.exec_()
    print str("Hejjj")
    print str(filedialog.selectedFiles().takeFirst())
    app.quit()
"""