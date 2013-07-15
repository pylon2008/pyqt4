#-*- coding: gbk -*-

#加载有需要的Qt库
from PyQt4 import QtCore, QtGui

#从ui_test.py文件中读取Ui_Dialog类，Ui_Dialog类由pyuic4生成
from test import Ui_Dialog

#继承的类要和生成的ui对相
class Ui(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Ui, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())
