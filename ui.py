# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(471, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 9, 441, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(353, 0, 31, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setText("")
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(403, 0, 31, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setText("")
        self.pushButton.setAutoRepeatDelay(292)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../.designer/backup/img/btn_set_normal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 0, 131, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(10, 40, 441, 531))
        self.widget_2.setObjectName("widget_2")
        self.login = QtWidgets.QPushButton(self.widget_2)
        self.login.setGeometry(QtCore.QRect(282, 132, 141, 61))
        self.login.setObjectName("login")
        self.device_id = QtWidgets.QLineEdit(self.widget_2)
        self.device_id.setGeometry(QtCore.QRect(22, 132, 231, 31))
        self.device_id.setWhatsThis("")
        self.device_id.setMaxLength(32)
        self.device_id.setObjectName("device_id")
        self.tabWidget = QtWidgets.QTabWidget(self.widget_2)
        self.tabWidget.setGeometry(QtCore.QRect(20, 220, 401, 291))
        self.tabWidget.setToolTipDuration(-6)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser.setGeometry(QtCore.QRect(6, 8, 381, 251))
        self.textBrowser.setStyleSheet("QTextBrowser{border-width:0;border-style:outset;font-size:12}")
        self.textBrowser.setLineWrapColumnOrWidth(0)
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.tab_2, "")
        self.safe_code = QtWidgets.QLineEdit(self.widget_2)
        self.safe_code.setGeometry(QtCore.QRect(22, 172, 231, 31))
        self.safe_code.setEchoMode(QtWidgets.QLineEdit.Password)
        self.safe_code.setObjectName("safe_code")
        self.ad1 = QtWidgets.QLabel(self.widget_2)
        self.ad1.setGeometry(QtCore.QRect(20, 10, 401, 101))
        self.ad1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ad1.setText("")
        self.ad1.setObjectName("ad1")
        self.show_w_btn = QtWidgets.QPushButton(self.widget_2)
        self.show_w_btn.setGeometry(QtCore.QRect(290, 200, 0, 0))
        self.show_w_btn.setMaximumSize(QtCore.QSize(0, 0))
        self.show_w_btn.setObjectName("show_w_btn")
        self.video_script = QtWidgets.QPushButton(self.widget_2)
        self.video_script.setGeometry(QtCore.QRect(282, 197, 141, 41))
        self.video_script.setObjectName("video_script")
        self.progressBar = QtWidgets.QProgressBar(self.widget_2)
        self.progressBar.setGeometry(QtCore.QRect(120, 220, 141, 20))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.widget_2.raise_()
        self.widget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 471, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "神秘鸭 smya.cn"))
        self.login.setText(_translate("MainWindow", "连接服务器"))
        self.device_id.setToolTip(_translate("MainWindow", "您的设备ID"))
        self.device_id.setPlaceholderText(_translate("MainWindow", "你的设备ID"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "运行日志"))
        self.safe_code.setStatusTip(_translate("MainWindow", "设备安全码在后台可获得"))
        self.safe_code.setPlaceholderText(_translate("MainWindow", "你的设备安全码"))
        self.show_w_btn.setText(_translate("MainWindow", "PushButton"))
        self.video_script.setText(_translate("MainWindow", "录制脚本"))
