#-*- coding: gbk -*-

#��������Ҫ��Qt��
from PyQt4 import QtCore, QtGui

#��ui_test.py�ļ��ж�ȡUi_Dialog�࣬Ui_Dialog����pyuic4����
from test import Ui_Dialog

#�̳е���Ҫ�����ɵ�ui����
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
