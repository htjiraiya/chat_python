# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'taocosung.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
from time import sleep
class Ui_Chat_Form(object):
    def setupUi(self, Form, con, tk):
        self.con = con 
        self.tk = tk
        self.ds_ban_be = ''
        self.id_nhan = ''
        self.list_hien_thi_lich_su_chat = {} # {ten: noi dung tin nhan}
        # self.list_friends = ''
        Thread(target=self.nhan_phan_hoi, args=([Form])).start() # the co bug giao dien

        Form.setObjectName("Form")
        Form.resize(779, 577)
        self.gridLayout_6 = QtWidgets.QGridLayout(Form)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_them_ban = QtWidgets.QPushButton(Form)
        self.pushButton_them_ban.setMaximumSize(QtCore.QSize(261, 23))
        self.pushButton_them_ban.setObjectName("pushButton_them_ban")
        self.gridLayout_3.addWidget(self.pushButton_them_ban, 0, 0, 1, 1)
        self.pushButton_dang_xuat = QtWidgets.QPushButton(Form)
        self.pushButton_dang_xuat.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButton_dang_xuat.setObjectName("pushButton_dang_xuat")
        self.gridLayout_3.addWidget(self.pushButton_dang_xuat, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 2)
        self.plainTextEdit_tim_kiem = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_tim_kiem.setMaximumSize(QtCore.QSize(201, 31))
        self.plainTextEdit_tim_kiem.setObjectName("plainTextEdit_tim_kiem")
        self.gridLayout_4.addWidget(self.plainTextEdit_tim_kiem, 1, 0, 1, 1)
        self.pushButton_tim_kiem = QtWidgets.QPushButton(Form)
        self.pushButton_tim_kiem.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButton_tim_kiem.setObjectName("pushButton_tim_kiem")
        self.gridLayout_4.addWidget(self.pushButton_tim_kiem, 1, 1, 1, 1)
        self.listWidget_list_friend = QtWidgets.QListWidget(Form)  
        self.listWidget_list_friend.setMaximumSize(QtCore.QSize(261, 16777215))
        self.listWidget_list_friend.setObjectName("listWidget_list_friend")
        self.gridLayout_4.addWidget(self.listWidget_list_friend, 2, 0, 1, 2)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plainTextEdit_hien_thi_chat = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_hien_thi_chat.setMaximumSize(QtCore.QSize(16777215, 11111111))
        self.plainTextEdit_hien_thi_chat.setObjectName("plainTextEdit_hien_thi_chat")
        self.gridLayout_2.addWidget(self.plainTextEdit_hien_thi_chat, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit_nhap_chat = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_nhap_chat.setMaximumSize(QtCore.QSize(16777215, 71))
        self.plainTextEdit_nhap_chat.setObjectName("plainTextEdit_nhap_chat")
        self.gridLayout.addWidget(self.plainTextEdit_nhap_chat, 0, 0, 1, 1)
        self.pushButton_gui_chat = QtWidgets.QPushButton(Form)
        self.pushButton_gui_chat.setMaximumSize(QtCore.QSize(75, 71))
        self.pushButton_gui_chat.setObjectName("pushButton_gui_chat")
        self.gridLayout.addWidget(self.pushButton_gui_chat, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.pushButton_gui_chat.clicked.connect(self.nhan_gui)
        self.pushButton_dang_xuat.clicked.connect(self.dang_xuat)
        self.retranslateUi(Form)
        self.pushButton_them_ban.clicked.connect(self.them_ban)
        self.pushButton_gui_chat.clicked.connect(self.nhan_gui)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.plainTextEdit_hien_thi_chat.setHidden(True)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_them_ban.setText(_translate("Form", "Thêm bạn bè"))
        self.pushButton_dang_xuat.setText(_translate("Form", "Đăng xuất"))
        self.pushButton_tim_kiem.setText(_translate("Form", "Tìm kiếm"))
        self.pushButton_gui_chat.setText(_translate("Form", "Gửi"))
        self.listWidget_list_friend.itemClicked.connect(self.chon_item)


    def nhan_gui(self): # gui tin nhan chat
        content_chat = self.plainTextEdit_nhap_chat.toPlainText()
        self.plainTextEdit_nhap_chat.clear() # hy vong ko bug
        

        if content_chat.strip() != '':
            
            mess_tin_nhan = f'chat-{self.tk},{self.id_nhan}-{content_chat}'

            self.con.send(mess_tin_nhan)
            print(f'da nhan nut gui {content_chat}')

        else:
            print(f'content ko dc rong => ko gui, {content_chat}')
    def nhan_phan_hoi(self, widget_chat):
        while True :
            # bug
            try :
                mess_response = self.con.recive()
                print(mess_response)
                # sleep(1)
                if mess_response != '':
                    self.xu_ly_phan_hoi(mess_response, widget_chat)
                    # continue
            except Exception as e:
                print('da co looi ket noi, ket noi se bi dong')
                print(e)
                break
        self.con.close()

    def xu_ly_phan_hoi(self, mess_response, widget_chat):
        # phan tich mess_response  thanh list_-
        mess_response = mess_response.split('-')
        if mess_response[0] == 'chat':
            
            if mess_response[1] == self.tk:
                
                content = f'You: {mess_response[2]}'
                self.list_hien_thi_lich_su_chat[mess_response[1]] += '\n'+content
                self.plainTextEdit_hien_thi_chat.clear()
                self.plainTextEdit_hien_thi_chat.appendPlainText(self.list_hien_thi_lich_su_chat[mess_response[1]])
            # self.plainTextEdit_hien_thi_chat.appendPlainText(mess_response[2])
            else:
                content = f'{mess_response[1]}: {mess_response[2]}'
                self.list_hien_thi_lich_su_chat[mess_response[1]] += '\n'+content
                self.plainTextEdit_hien_thi_chat.appendPlainText(content)
        if mess_response[0] == 'dadangxuat':
            widget_chat.close()
            self.con.close()

        if mess_response[0] =='dsbanbe':
            # mess_response[1] = dsbanbedangon; ds ban be 
            # phan tich ds ban be 
            self.ds_ban_be, self.ds_ban_be_dang_on = mess_response[1].split(';') # ['a,c' , 'a,s,d']
            # self.ds_ban_be_dang_on = ds_ban_be_dang_on.split(',')
            self.ds_ban_be = self.ds_ban_be.split(',')
            # self.ds_ban_be = list(self.ds_ban_be)
            self.ds_ban_be = set(self.ds_ban_be)
            self.ds_ban_be = list(self.ds_ban_be)
            # self.ds_ban_be.remove(',')

            for i in self.ds_ban_be:
                lich_su_chat = """"""
                self.list_hien_thi_lich_su_chat[i] = lich_su_chat
                a = QtWidgets.QListWidgetItem(i)
                self.listWidget_list_friend.addItem(a)

            print(mess_response)
            self.plainTextEdit_hien_thi_chat.appendPlainText(str(mess_response))


    def dang_xuat(self,):
        mess_dang_xuat = f'dangxuat-{self.tk}-dang xuat'
        self.con.send(mess_dang_xuat)

        # response_mess_dang_xuat = self.con.recive()
       

    def them_ban(self):
        # ko co tham so self
        text, ok = QtWidgets.QInputDialog.getText('Text Input Dialog', 'Enter your name:')
		
        if ok and text.strip() != '' :
            self.id_user = text
            mess_them_ban = f'themban-{self.id_user}'
            self.con.send()


    def chon_item(self):
        self.plainTextEdit_hien_thi_chat.setHidden(False)
        list_items_friends= self.listWidget_list_friend.selectedItems()
        for i in list_items_friends:
            if i.isSelected():
                self.id_nhan = i.text()
                content_chat_id_user = self.list_hien_thi_lich_su_chat[self.id_nhan]
                self.plainTextEdit_hien_thi_chat.clear()
                
                self.plainTextEdit_hien_thi_chat.appendPlainText(content_chat_id_user)
                print(content_chat_id_user)
                break


class chat1:
    def __init__(self, con, tk):
        self.con = con
        self.widget_chat = QtWidgets.QWidget()
        self.ui_chat = Ui_Chat_Form()
        self.ui_chat.setupUi(self.widget_chat, self.con, tk)
        # self.widget_chat.show()


# if __name__ == "__main__":
#     from client import Client
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     # Form = QtWidgets.QWidget()
#     client = Client()
#     ui = chat1(client)
#     ui.widget_chat.show()
#     sys.exit(app.exec_())
