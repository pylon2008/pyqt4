# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\WorkStation\Git\Hub\pyqt4\fengsi.ui'
#
# Created: Tue Jul 16 14:36:30 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Fengsi(object):
    def setupUi(self, Fengsi):
        Fengsi.setObjectName(_fromUtf8("Fengsi"))
        Fengsi.resize(665, 532)
        self.m_btnOK = QtGui.QPushButton(Fengsi)
        self.m_btnOK.setGeometry(QtCore.QRect(320, 330, 75, 23))
        self.m_btnOK.setObjectName(_fromUtf8("m_btnOK"))
        self.m_btnCancle = QtGui.QPushButton(Fengsi)
        self.m_btnCancle.setGeometry(QtCore.QRect(410, 330, 75, 23))
        self.m_btnCancle.setObjectName(_fromUtf8("m_btnCancle"))
        self.m_targetURL = QtGui.QTextEdit(Fengsi)
        self.m_targetURL.setGeometry(QtCore.QRect(50, 10, 351, 30))
        self.m_targetURL.setObjectName(_fromUtf8("m_targetURL"))
        self.tableWidget = QtGui.QTableWidget(Fengsi)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 481, 261))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtGui.QLabel(Fengsi)
        self.label.setGeometry(QtCore.QRect(10, 20, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.m_btnSearch = QtGui.QPushButton(Fengsi)
        self.m_btnSearch.setGeometry(QtCore.QRect(410, 14, 75, 23))
        self.m_btnSearch.setObjectName(_fromUtf8("m_btnSearch"))
        self.m_Type = QtGui.QComboBox(Fengsi)
        self.m_Type.setGeometry(QtCore.QRect(70, 330, 69, 22))
        self.m_Type.setObjectName(_fromUtf8("m_Type"))
        self.tabWidget = QtGui.QTabWidget(Fengsi)
        self.tabWidget.setGeometry(QtCore.QRect(120, 370, 211, 141))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.pushButton = QtGui.QPushButton(self.tab_1)
        self.pushButton.setGeometry(QtCore.QRect(20, 50, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.pushButton_2 = QtGui.QPushButton(self.tab_4)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 20, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))

        self.retranslateUi(Fengsi)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QObject.connect(self.m_btnOK, QtCore.SIGNAL(_fromUtf8("clicked()")), Fengsi.close)
        QtCore.QObject.connect(self.m_btnCancle, QtCore.SIGNAL(_fromUtf8("clicked()")), Fengsi.close)
        QtCore.QObject.connect(self.m_btnSearch, QtCore.SIGNAL(_fromUtf8("clicked()")), Fengsi.beginSearch)
        QtCore.QMetaObject.connectSlotsByName(Fengsi)

    def retranslateUi(self, Fengsi):
        Fengsi.setWindowTitle(_translate("Fengsi", "Dialog", None))
        self.m_btnOK.setText(_translate("Fengsi", "确定", None))
        self.m_btnCancle.setText(_translate("Fengsi", "取消", None))
        self.label.setText(_translate("Fengsi", "目标:", None))
        self.m_btnSearch.setText(_translate("Fengsi", "开始", None))
        self.pushButton.setText(_translate("Fengsi", "PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Fengsi", "1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Fengsi", "2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Fengsi", "3", None))
        self.pushButton_2.setText(_translate("Fengsi", "PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Fengsi", "4", None))

