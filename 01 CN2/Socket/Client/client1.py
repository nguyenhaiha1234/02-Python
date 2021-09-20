# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\01 Github\02-Python\01 CN2\Socket\Client\client1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from clsMisc import Misc

class Ui_HHClient(object):
    def setupUi(self, HHClient):
        HHClient.setObjectName("HHClient")
        HHClient.resize(443, 224)
        self.txtServerIP = QtWidgets.QTextEdit(HHClient)
        self.txtServerIP.setGeometry(QtCore.QRect(90, 10, 161, 21))
        self.txtServerIP.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtServerIP.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtServerIP.setPlaceholderText("")
        self.txtServerIP.setObjectName("txtServerIP")
        self.labServerAddress = QtWidgets.QLabel(HHClient)
        self.labServerAddress.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.labServerAddress.setObjectName("labServerAddress")
        self.btnConnect = QtWidgets.QPushButton(HHClient)
        self.btnConnect.setGeometry(QtCore.QRect(260, 10, 75, 23))
        self.btnConnect.setObjectName("btnConnect")
        self.btnDisconect = QtWidgets.QPushButton(HHClient)
        self.btnDisconect.setGeometry(QtCore.QRect(350, 10, 75, 23))
        self.btnDisconect.setObjectName("btnDisconect")
        self.btnExit = QtWidgets.QPushButton(HHClient)
        self.btnExit.setGeometry(QtCore.QRect(350, 172, 75, 41))
        self.btnExit.setObjectName("btnExit")
        self.btnRegistry = QtWidgets.QPushButton(HHClient)
        self.btnRegistry.setGeometry(QtCore.QRect(90, 170, 241, 41))
        self.btnRegistry.setObjectName("btnRegistry")
        self.btnProcessRun = QtWidgets.QToolButton(HHClient)
        self.btnProcessRun.setGeometry(QtCore.QRect(10, 50, 71, 161))
        self.btnProcessRun.setObjectName("btnProcessRun")
        self.btnAppRun = QtWidgets.QToolButton(HHClient)
        self.btnAppRun.setGeometry(QtCore.QRect(90, 50, 241, 51))
        self.btnAppRun.setObjectName("btnAppRun")
        self.btnShutdown = QtWidgets.QToolButton(HHClient)
        self.btnShutdown.setGeometry(QtCore.QRect(90, 110, 111, 51))
        self.btnShutdown.setObjectName("btnShutdown")
        self.btnScreenShot = QtWidgets.QToolButton(HHClient)
        self.btnScreenShot.setGeometry(QtCore.QRect(210, 110, 121, 51))
        self.btnScreenShot.setObjectName("btnScreenShot")
        self.btnKeyStroke = QtWidgets.QPushButton(HHClient)
        self.btnKeyStroke.setGeometry(QtCore.QRect(350, 50, 75, 111))
        self.btnKeyStroke.setObjectName("btnKeyStroke")
       
        self.retranslateUi(HHClient)
        QtCore.QMetaObject.connectSlotsByName(HHClient)
    
   #Event
        self.btnConnect.clicked.connect(self.btnConnect_Click)
        self.btnExit.clicked.connect(self.btnExit_Click)


    def btnConnect_Click(self):
        print("Press button")       
        Misc.Mbox('Your title', 'Your text', 1)
        Misc.DienTich(6,5)

    
    def btnExit_Click(sekf):
        print("Thoát khỏi chương trình Client")
        quit()

    def retranslateUi(self, HHClient):
        _translate = QtCore.QCoreApplication.translate
        HHClient.setWindowTitle(_translate("HHClient", "Client - Bài tập Mạng máy tính"))
        self.txtServerIP.setHtml(_translate("HHClient", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">127.0.0.1</p></body></html>"))
        self.labServerAddress.setText(_translate("HHClient", "Server address:"))
        self.btnConnect.setText(_translate("HHClient", "Kết nối"))
        self.btnDisconect.setText(_translate("HHClient", "Ngắt kết nối"))
        self.btnExit.setText(_translate("HHClient", "Thoát"))
        self.btnRegistry.setText(_translate("HHClient", "Sửa Registry"))
        self.btnProcessRun.setText(_translate("HHClient", "Process\n"
"Running"))
        self.btnAppRun.setText(_translate("HHClient", "App Running"))
        self.btnShutdown.setText(_translate("HHClient", "Tắt máy"))
        self.btnScreenShot.setText(_translate("HHClient", "Chụp màn hình"))
        self.btnKeyStroke.setText(_translate("HHClient", "Keystroke"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HHClient = QtWidgets.QDialog()
    ui = Ui_HHClient()
    ui.setupUi(HHClient)
    HHClient.show()
    sys.exit(app.exec_())
