# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        LoginPage.setObjectName("LoginPage")
        LoginPage.resize(800, 600)
        self.gridLayoutWidget = QtWidgets.QWidget(LoginPage)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 801, 601))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(50, 50, 50, 50)
        self.gridLayout.setObjectName("gridLayout")
        self.LoginTab = QtWidgets.QTabWidget(self.gridLayoutWidget)
        self.LoginTab.setStyleSheet("")
        self.LoginTab.setObjectName("LoginTab")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("background-color: rgb(255, 238, 220);")
        self.tab.setObjectName("tab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 701, 481))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(30, 30, 30, 30)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Password_Lable = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.Password_Lable.setStyleSheet("background-color: rgb(207, 194, 190);")
        self.Password_Lable.setAlignment(QtCore.Qt.AlignCenter)
        self.Password_Lable.setObjectName("Password_Lable")
        self.gridLayout_2.addWidget(self.Password_Lable, 3, 0, 1, 2)
        self.Password_Getter = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.Password_Getter.setStyleSheet("background-color: rgb(220, 228, 234);")
        self.Password_Getter.setObjectName("Password_Getter")
        self.gridLayout_2.addWidget(self.Password_Getter, 3, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 4, 0, 1, 3)
        self.LoginButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.LoginButton.setStyleSheet("background-color: rgb(150, 156, 161);")
        self.LoginButton.setObjectName("LoginButton")
        self.gridLayout_2.addWidget(self.LoginButton, 5, 0, 1, 3)
        self.UserId_Getter = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.UserId_Getter.setStyleSheet("background-color: rgb(220, 228, 234);")
        self.UserId_Getter.setObjectName("UserId_Getter")
        self.gridLayout_2.addWidget(self.UserId_Getter, 2, 2, 1, 1)
        self.User_Id_Lable = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.User_Id_Lable.setStyleSheet("background-color: rgb(207, 194, 190);")
        self.User_Id_Lable.setAlignment(QtCore.Qt.AlignCenter)
        self.User_Id_Lable.setObjectName("User_Id_Lable")
        self.gridLayout_2.addWidget(self.User_Id_Lable, 2, 0, 1, 2)
        self.SignUpButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.SignUpButton.setStyleSheet("background-color: rgb(150, 156, 161);")
        self.SignUpButton.setObjectName("SignUpButton")
        self.gridLayout_2.addWidget(self.SignUpButton, 6, 2, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox.setStyleSheet("background-color: rgb(207, 194, 190);")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 6, 0, 1, 2)
        self.Login_Tutorial_Lable = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        self.Login_Tutorial_Lable.setFont(font)
        self.Login_Tutorial_Lable.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.Login_Tutorial_Lable.setAlignment(QtCore.Qt.AlignCenter)
        self.Login_Tutorial_Lable.setObjectName("Login_Tutorial_Lable")
        self.gridLayout_2.addWidget(self.Login_Tutorial_Lable, 0, 0, 1, 3)
        self.LoginTab.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("background-color: rgb(255, 238, 220);")
        self.tab_2.setObjectName("tab_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab_2)
        self.calendarWidget.setGeometry(QtCore.QRect(90, 90, 501, 301))
        self.calendarWidget.setStyleSheet("background-color: rgb(198, 243, 255);")
        self.calendarWidget.setObjectName("calendarWidget")
        self.LoginTab.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.LoginTab, 0, 0, 1, 1)
        self.Password_Lable.setBuddy(self.Password_Getter)
        self.User_Id_Lable.setBuddy(self.UserId_Getter)

        self.retranslateUi(LoginPage)
        self.LoginTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)

    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "Form"))
        self.Password_Lable.setText(_translate("LoginPage", "Password:"))
        self.LoginButton.setText(_translate("LoginPage", "Login in!"))
        self.User_Id_Lable.setText(_translate("LoginPage", "User Id:"))
        self.SignUpButton.setText(_translate("LoginPage", "Sign Up!"))
        self.checkBox.setText(_translate("LoginPage", "Manager"))
        self.Login_Tutorial_Lable.setText(_translate("LoginPage", "Input your infomation to login in!"))
        self.LoginTab.setTabText(self.LoginTab.indexOf(self.tab), _translate("LoginPage", "Login"))
        self.LoginTab.setTabText(self.LoginTab.indexOf(self.tab_2), _translate("LoginPage", "Date"))
