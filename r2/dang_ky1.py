# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dang_kycmnr.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from chat1 import chat1

class Ui_Dang_Ky_Form(object):
    def setupUi(self, Form, con):
        self.con = con
        Form.setObjectName("Form")
        Form.resize(198, 102)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_tai_khoan = QtWidgets.QLineEdit(Form)
        self.lineEdit_tai_khoan.setMaximumSize(QtCore.QSize(171, 31))
        self.lineEdit_tai_khoan.setText("")
        self.lineEdit_tai_khoan.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_tai_khoan.setObjectName("lineEdit_tai_khoan")
        self.gridLayout.addWidget(self.lineEdit_tai_khoan, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setMaximumSize(QtCore.QSize(171, 31))
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.pushButton_dang_ky = QtWidgets.QPushButton(Form)
        self.pushButton_dang_ky.setMaximumSize(QtCore.QSize(171, 23))
        self.pushButton_dang_ky.setObjectName("pushButton_dang_ky")
        self.gridLayout.addWidget(self.pushButton_dang_ky, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.pushButton_dang_ky.clicked.connect(lambda: self.nhan_dang_ky(Form))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_tai_khoan.setPlaceholderText(_translate("Form", "tài khoản"))
        self.lineEdit.setPlaceholderText(_translate("Form", "mật khẩu"))
        self.pushButton_dang_ky.setText(_translate("Form", "đăng ký"))


    def nhan_dang_ky(self, Form):
        tk = self.lineEdit_tai_khoan.text()
        mk = self.lineEdit.text()
        mess_dang_ky = f'dangky-{tk}-{mk}'
        print(mess_dang_ky)
        self.con.send(mess_dang_ky)

        response_mess_dang_ky = self.con.recive()
        # phan tich response_mess_dang_ky thanh list_-
        response_mess_dang_ky = response_mess_dang_ky.split('-')
        if response_mess_dang_ky[0] == 'dangkythanhcong' or response_mess_dang_ky[0] == 'thanhcong' :
            Form.hide()
            print('da hide Form ')
            self.chat = chat1(self.con,tk)
            self.chat.widget_chat.show()
            print('da hien thi chat')
            

        
        else :
            print(response_mess_dang_ky)
    

class dang_ky1:
    def __init__(self, con):
        self.con = con
        self.widget_dang_ky = QtWidgets.QWidget()
        self.ui_dang_ky = Ui_Dang_Ky_Form()
        self.ui_dang_ky.setupUi(self.widget_dang_ky, self.con)
        # self.widget_dang_ky.show()

# if __name__ == "__main__":
#     import sys
#     from client import Client
#     client = Client()
#     app = QtWidgets.QApplication(sys.argv)
#     a = dang_ky1(client)
# a.widget_dang_ky.show()
#     sys.exit(app.exec_())
