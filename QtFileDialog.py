# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 12:02:56 2014

@author: NIAP
"""

from PyQt4.QtGui import *
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)


    filedialog = QFileDialog()
    filedialog.setModal(True)
    filedialog.show()
    print str(filedialog.selectedFiles().takeFirst())
    
#    dlg = QFileDialog()
#    dlg.show()
    sys.exit(app.exec_())
#    app.quit()