import sys
import csv
import re
import pandas as pd
from PyQt5 import QtWidgets
import mainUIAction
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import win32api, win32con
from RegUI import Ui_regedit
from FrmUI import Ui_frmMain


# 注册页功能
class regDialog(QtWidgets.QDialog, Ui_regedit):
    def __init__(self):
        super(regDialog, self).__init__()
        self.setupUi(self)
        self.label.setPixmap(QPixmap.fromImage(QImage('./images/logo_bg.png')))

    # 注册功能函数，连接数据库
    def save_reg_info(self, user, pwd):
        return True

    def slot_ok(self):
        user = self.user_lineEdit.text()
        pwd = self.pwd_lineEdit.text()
        self.path="pass_log.csv"

        if user == '' or pwd == '':
            win32api.MessageBox(0, "用户名或密码不能为空,请重新输入!", "注册提醒", win32con.MB_ICONWARNING)

        NewID = user
        PassWord = pwd
        data = pd.read_csv(self.path, sep=',', encoding='utf-8')  # encoding='unicode_escape'    'utf-8'  'GBK'注意区分这几种编码格式
        a = data['UserID'].tolist()
        if NewID in a:
            win32api.MessageBox(0, "用户名已存在,请重新输入!", "注册提醒", win32con.MB_ICONWARNING)
            NewID = self.user_lineEdit.text()
        else:
            with open(self.path, 'a+', newline="") as f:
                csv_write = csv.writer(f)
                data_row = [NewID, PassWord]
                csv_write.writerow(data_row)
                win32api.MessageBox(0, "注册成功!", "注册提醒", win32con.MB_ICONWARNING)
                self.close()


class MyMainWindow(QMainWindow, Ui_frmMain):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1280, 720)  # 固定大小
        self.okButton.clicked.connect(self.ok_action)  # 点击登录按钮
        self.pushButtonReg.clicked.connect(self.reg_action)  # 点击注册按钮
        # self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
        self.startAnimation()
        self.initQSS()
        self.path = "pass_log.csv"


    def reg_action(self):
        reg_dialog.show()

    def login_by_acount_action(self):
        self.pushButtonAcount.setStyleSheet('color:#0088ff;')
        self.pushButtonPhone.setStyleSheet('color:black;')

    '''  验证登录是否正确  '''

    def adj_login(self, user, pwd):

        with open(self.path, "r+", encoding='utf-8') as f:
            csv_read = csv.reader(f)
            rows = [row for row in csv_read]

        if ([user, pwd] in rows):
            return True
        else:
            # QMessageBox.critical(self, '错误', '密码错误！')
            self.lineEditPwd.clear()
            return False

    ''' 点击登录按钮事件 '''

    def ok_action(self):

        user = self.lineEditUser.text().strip()
        pwd = self.lineEditPwd.text().strip()
        if user == '' or pwd == '':
            win32api.MessageBox(0, "用户名或密码不能为空,请重新输入!", "登录提醒", win32con.MB_ICONWARNING)
            return False

        if self.adj_login(user, pwd) == True:
            # 打开功能页面
            self.another_window = mainUIAction.mainUIAction()
            self.another_window.show()
            # 关闭登录窗口
            self.close()
        else:
            win32api.MessageBox(0, "用户名或密码不正确,请重新输入!", "登录提醒", win32con.MB_ICONWARNING)
            return False

    def closeWindowAnimation(self):
        '''
        关闭时的动画效果
        '''
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()
        self.animation.finished.connect(self.close)

    def startAnimation(self):
        '''
        启动时的动画效果
        '''
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def initQSS(self):
        '''
        初始化样式
        '''
        style_file = QFile("style.css")
        if style_file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(style_file)
            style_sheet = stream.readAll()
            # print(style_sheet)
            self.setStyleSheet(style_sheet)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    reg_dialog = regDialog()
    myWin.show()
    sys.exit(app.exec_())
