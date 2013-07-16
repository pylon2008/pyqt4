#-*- coding: gbk -*-

#��������Ҫ��Qt��
from PyQt4 import QtCore, QtGui

#��ui_test.py�ļ��ж�ȡUi_Dialog�࣬Ui_Dialog����pyuic4����
from fengsi import Ui_Fengsi

#�̳е���Ҫ�����ɵ�ui����
class Ui(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Ui, self).__init__(parent)
        self.ui = Ui_Fengsi()
        self.ui.setupUi(self)
        
    def beginSearch(self):  
        stri = self.ui.m_targetURL.toPlainText()
        row = 2
        col = 5
        self.ui.tableWidget.setRowCount(row)
        self.ui.tableWidget.setColumnCount(col)  
        self.ui.tableWidget.setHorizontalHeaderLabels(['SUN','MON','TUE','WED','THU'])     
        self.ui.tableWidget.horizontalHeader().setClickable(False)
        for i in range(row):
            for j in range(col):
                value = str(i)+str(j)
                item = QtGui.QTableWidgetItem(QtGui.QIcon("pic//b_blue_1.gif"), value)
                #item = QtGui.QTableWidgetItem(value)
                self.ui.tableWidget.setItem(i,j,item)
        self.ui.tableWidget.show()
        self.show()

if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())
