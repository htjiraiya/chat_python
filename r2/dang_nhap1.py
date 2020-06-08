# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dang_nhap_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from dang_ky1 import dang_ky1
from chat1 import chat1
from client import Client
from time import sleep

class Ui_gridLayout_dang_nhap(object):
    def setupUi(self, gridLayout_dang_nhap, con):
        # self.form_chat = chat1('s')
        # self.form_dang_ky = dang_nhap1('s')
        self.con = con
        gridLayout_dang_nhap.setObjectName("gridLayout_dang_nhap")
        gridLayout_dang_nhap.resize(255, 115)
        gridLayout_dang_nhap.setMaximumSize(QtCore.QSize(255, 115))
        self.gridLayout_2 = QtWidgets.QGridLayout(gridLayout_dang_nhap)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit_tai_khoan = QtWidgets.QTextEdit(gridLayout_dang_nhap)
        self.textEdit_tai_khoan.setMaximumSize(QtCore.QSize(241, 31))
        self.textEdit_tai_khoan.setObjectName("textEdit_tai_khoan")
        self.gridLayout.addWidget(self.textEdit_tai_khoan, 0, 0, 1, 2)
        # qline edit mk => mode qline 
        self.textEdit_mat_khau = QtWidgets.QLineEdit(gridLayout_dang_nhap)

        self.textEdit_mat_khau.setMaximumSize(QtCore.QSize(241, 31))
        self.textEdit_mat_khau.setObjectName("textEdit_mat_khau")
        self.gridLayout.addWidget(self.textEdit_mat_khau, 1, 0, 1, 2)
        self.pushButton_dang_nhap = QtWidgets.QPushButton(gridLayout_dang_nhap)
        self.pushButton_dang_nhap.setMaximumSize(QtCore.QSize(121, 23))
        self.pushButton_dang_nhap.setObjectName("pushButton_dang_nhap")
        self.gridLayout.addWidget(self.pushButton_dang_nhap, 2, 0, 1, 1)
        self.pushButton_dang_ky = QtWidgets.QPushButton(gridLayout_dang_nhap)
        self.pushButton_dang_ky.setMaximumSize(QtCore.QSize(111, 23))
        self.pushButton_dang_ky.setObjectName("pushButton_dang_ky")
        self.gridLayout.addWidget(self.pushButton_dang_ky, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.textEdit_mat_khau.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton_dang_nhap.clicked.connect(lambda : self.nhan_dang_nhap(gridLayout_dang_nhap))
        self.pushButton_dang_ky.clicked.connect(lambda: self.nhan_dang_ky(gridLayout_dang_nhap))
        self.retranslateUi(gridLayout_dang_nhap)
        QtCore.QMetaObject.connectSlotsByName(gridLayout_dang_nhap)
        
    def retranslateUi(self, gridLayout_dang_nhap):
        _translate = QtCore.QCoreApplication.translate
        gridLayout_dang_nhap.setWindowTitle(_translate("gridLayout_dang_nhap", "Form"))
        self.textEdit_tai_khoan.setPlaceholderText(_translate("gridLayout_dang_nhap", "tài khoản"))
        self.textEdit_mat_khau.setPlaceholderText(_translate("gridLayout_dang_nhap", "mật khẩu"))
        self.pushButton_dang_nhap.setText(_translate("gridLayout_dang_nhap", "đăng nhập"))
        self.pushButton_dang_ky.setText(_translate("gridLayout_dang_nhap", "đăng ký"))

    def nhan_dang_nhap(self,gridLayout_dang_nhap):
        # lay tthong tin dang nhap
        tk = self.textEdit_tai_khoan.toPlainText()
        tk = tk.strip()
        # QLineEdit
        mk = self.textEdit_mat_khau.text()
        mk = mk.strip()
        if tk != '' or mk != '':

            mess_dang_nhap = f'dangnhap-{tk}-{mk}'
            # gui toi server
            self.con.send(mess_dang_nhap)
            sleep(1)
            response_mess_dang_nhap = self.con.recive()
            # phan tich response_mess_dang_nhap thanh list_-
            response_mess_dang_nhap = response_mess_dang_nhap.split('-')
            # server kiem tra va tra ket qua thong qua con 
            if response_mess_dang_nhap[0] == 'thanhcong' or response_mess_dang_nhap[0] =='dangnhapthanhcong':
                message_box = QtWidgets.QMessageBox.question(gridLayout_dang_nhap, 'dang nhap thanh cong', str(response_mess_dang_nhap), QtWidgets.QMessageBox.Ok)
                
                self.form_chat = chat1(self.con, tk)
                self.form_chat.widget_chat.show()
                gridLayout_dang_nhap.hide()
            else :
                message_box = QtWidgets.QMessageBox.question(gridLayout_dang_nhap, 'thong tin dang nhap khong duoc rong', 'kiem tra lai tai khoan hoac mat khau', QtWidgets.QMessageBox.Ok)
                

        else:
            print('thong tin dang nhap khong dc rong')
            message_box = QtWidgets.QMessageBox.question(gridLayout_dang_nhap, 'dang nhap that bai', 'thong tin dang nhap ko dc rong', QtWidgets.QMessageBox.Ok)
            

    def nhan_dang_ky(self,gridLayout_dang_nhap):
       
        self.form_dang_ky = dang_ky1(self.con)
        self.form_dang_ky.widget_dang_ky.show()
        gridLayout_dang_nhap.hide()
        
class dang_nhap1:
    def __init__(self, con):
        self.con = con
        self.widget_dang_nhap = QtWidgets.QWidget()
        self.ui_dang_nhap = Ui_gridLayout_dang_nhap()
        self.ui_dang_nhap.setupUi(self.widget_dang_nhap, self.con)
        self.widget_dang_nhap.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    client =  Client()
    a = dang_nhap1(client)
    sys.exit(app.exec_())
