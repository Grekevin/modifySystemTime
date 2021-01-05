# -*- coding: utf-8 -*-
"""
服务器时间同步助手的图形化界面
"""

from os import read, system
from config import Config
from getservertime import ServerTime
import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets

class setSystemTimeUi(QtWidgets.QWidget):
    def __init__(self, parent = None):
        self.config = Config()
        super(setSystemTimeUi, self).__init__(parent=None)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('服务器时间同步助手')
        self.setFixedSize(380, 200)
        self.server_label()
        self.server_combobox()
        self.sync_btn()
        self.add_edit()
        self.show_current_time()


    # 标签
    def server_label(self):
        self.server_label = QtWidgets.QLabel(self)
        self.server_label.setGeometry(QtCore.QRect(10, 32, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.server_label.setFont(font)
        self.server_label.setAlignment(QtCore.Qt.AlignCenter)
        self.server_label.setText("选择服务器：")

        self.new_server_label = QtWidgets.QLabel(self)
        self.new_server_label.setGeometry(QtCore.QRect(10, 85, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.new_server_label.setFont(font)
        self.new_server_label.setAlignment(QtCore.Qt.AlignCenter)
        self.new_server_label.setText("服务器名称：")

        self.server_url_label = QtWidgets.QLabel(self)
        self.server_url_label.setGeometry(QtCore.QRect(16, 130, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.server_url_label.setFont(font)
        self.server_url_label.setAlignment(QtCore.Qt.AlignCenter)
        self.server_url_label.setText("服务器url：")

    # 添加编辑框
    def add_edit(self):
        self.name_lineEdit = QtWidgets.QLineEdit(self)
        self.name_lineEdit.setGeometry(QtCore.QRect(110, 85, 163, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.name_lineEdit.setFont(font)

        self.url_lineEdit = QtWidgets.QLineEdit(self)
        self.url_lineEdit.setGeometry(QtCore.QRect(110, 130, 163, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.url_lineEdit.setFont(font)

    # 服务器列表
    def server_combobox(self):
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(110, 30, 161, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox.setFont(font)

        self.comboBox.addItems(self.config.read_data().keys())
        
        self.comboBox.currentIndexChanged.connect(self.cnmbox_change)
    
    def cnmbox_change(self):
        print(self.comboBox.currentText())

    # 按钮
    def sync_btn(self):
        self.sync_pushButton = QtWidgets.QPushButton(self)
        self.sync_pushButton.setGeometry(QtCore.QRect(290, 29, 75, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.sync_pushButton.setFont(font)
        self.sync_pushButton.setText('同步时间')
        self.sync_pushButton.clicked.connect(self.sync_date_time)

        self.sync_pushButton = QtWidgets.QPushButton(self)
        self.sync_pushButton.setGeometry(QtCore.QRect(290, 100, 75, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.sync_pushButton.setFont(font)
        self.sync_pushButton.setText('添加服务器')
        self.sync_pushButton.clicked.connect(self.add_server_dialog)

    # 同步成功提示对话框
    def message_box(self):
        msgbox = QtWidgets.QDialog()
        label = QtWidgets.QLabel(msgbox)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        label.setFont(font)
        label.setText('时间同步成功！')
        label.move(50, 35)
        msgbox.setWindowTitle('提醒')
        msgbox.setFixedSize(200, 100)
        msgbox.setWindowModality(QtCore.Qt.ApplicationModal)
        msgbox.exec_()
    
    def add_server_dialog(self):
        msg_str = ''

        server_name = self.name_lineEdit.text()
        if '服务器' not in server_name and len(server_name)>0:
            server_name = ''.join([server_name, '服务器'])
            
        server_url = self.url_lineEdit.text()

        if server_name and server_url:
            if server_name in self.config.read_data().keys():
                msg_str = '服务器已存在！'
            else:
                self.config.write_data(server_name, server_url)
                self.comboBox.addItem(server_name)
                msg_str = '服务器添加成功！'
        else:
             msg_str = '无效数据！'

        msgbox = QtWidgets.QDialog()
        label = QtWidgets.QLabel(msgbox)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        label.setFont(font)
        label.setText(msg_str)
        label.move(50, 35)
        msgbox.setWindowTitle('提醒')
        msgbox.setFixedSize(200, 100)
        msgbox.setWindowModality(QtCore.Qt.ApplicationModal)
        msgbox.exec_()
        
    # 当前系统时间显示标签
    def show_current_time(self):
        self.ctm_lable = QtWidgets.QLabel(self)
        self.ctm_lable.setGeometry(QtCore.QRect(2, 180, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.ctm_lable.setFont(font)
        self.ctm_lable.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ctm_lable.setIndent(-1)
        self.timer = QtCore.QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.dynamic_show_time)

    # 动态显示当前系统时间
    def dynamic_show_time(self):
        time_str = time.strftime('%Y-%m-%d %H:%M:%S')
        self.ctm_lable.setText('当前系统时间: {}'.format(time_str))

    # 获取服务器时间
    def get_datetime(self):
        server_data = self.config.read_data()
        server_name = self.comboBox.currentText()
        server_datetime = ServerTime(server_data, server_name).get_datetime().split(' ')
        server_date = server_datetime[0]
        server_time = server_datetime[1]
        return (server_date, server_time)

    # 时间同步
    def sync_date_time(self):
        date_time = self.get_datetime()
        date = ' '.join(['date', date_time[0]])
        time = ' '.join(['time', date_time[1]])
        print(date)
        print(time)
        for cmd in [date, time]:
            system(cmd)
        self.sync_pushButton.clicked.connect(self.add_server_dialog)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_win = setSystemTimeUi()
    main_win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()