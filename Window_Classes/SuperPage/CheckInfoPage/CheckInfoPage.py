# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CheckInfoPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CheckInfoPage(object):
    def setupUi(self, CheckInfoPage):
        CheckInfoPage.setObjectName("CheckInfoPage")
        CheckInfoPage.resize(800, 600)
        self.gridLayoutWidget = QtWidgets.QWidget(CheckInfoPage)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 801, 601))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(50, 50, 50, 50)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 4, 1, 5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 3, 5, 1, 4)
        self.BookCombo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.BookCombo.setObjectName("BookCombo")
        self.BookCombo.addItem("")
        self.BookCombo.addItem("")
        self.BookCombo.addItem("")
        self.gridLayout.addWidget(self.BookCombo, 0, 1, 1, 3)
        self.QueryUserButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.QueryUserButton.setObjectName("QueryUserButton")
        self.gridLayout.addWidget(self.QueryUserButton, 10, 7, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 8, 0, 1, 9)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 9)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 4, 1, 1)
        self.UserCombo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.UserCombo.setObjectName("UserCombo")
        self.UserCombo.addItem("")
        self.gridLayout.addWidget(self.UserCombo, 0, 5, 1, 4)
        self.UserView = QtWidgets.QTableView(self.gridLayoutWidget)
        self.UserView.setObjectName("UserView")
        self.gridLayout.addWidget(self.UserView, 7, 4, 1, 5)
        self.BookView = QtWidgets.QTableView(self.gridLayoutWidget)
        self.BookView.setObjectName("BookView")
        self.gridLayout.addWidget(self.BookView, 7, 0, 1, 4)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 9, 7, 1, 2)
        self.BookNameLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.BookNameLine.setObjectName("BookNameLine")
        self.gridLayout.addWidget(self.BookNameLine, 3, 1, 1, 3)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 4)
        self.PriceLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.PriceLine.setObjectName("PriceLine")
        self.gridLayout.addWidget(self.PriceLine, 2, 1, 1, 3)
        self.UserIdLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.UserIdLine.setObjectName("UserIdLine")
        self.gridLayout.addWidget(self.UserIdLine, 2, 5, 1, 4)
        self.QueryBookButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.QueryBookButton.setObjectName("QueryBookButton")
        self.gridLayout.addWidget(self.QueryBookButton, 9, 0, 1, 2)
        self.toolButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 9, 2, 1, 1)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.gridLayoutWidget)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.gridLayout.addWidget(self.commandLinkButton, 9, 3, 1, 1)
        self.SaveUserButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.SaveUserButton.setObjectName("SaveUserButton")
        self.gridLayout.addWidget(self.SaveUserButton, 9, 4, 1, 3)
        self.SaveBookButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.SaveBookButton.setObjectName("SaveBookButton")
        self.gridLayout.addWidget(self.SaveBookButton, 10, 0, 1, 3)
        self.RefreshButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.RefreshButton.setObjectName("RefreshButton")
        self.gridLayout.addWidget(self.RefreshButton, 10, 3, 1, 1)
        self.GoBackButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.GoBackButton.setObjectName("GoBackButton")
        self.gridLayout.addWidget(self.GoBackButton, 10, 4, 1, 3)
        self.dateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 4, 5, 1, 4)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 1)
        self.BookAlineTypeCombo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.BookAlineTypeCombo.setObjectName("BookAlineTypeCombo")
        self.BookAlineTypeCombo.addItem("")
        self.BookAlineTypeCombo.addItem("")
        self.gridLayout.addWidget(self.BookAlineTypeCombo, 5, 1, 1, 3)
        self.UserAlineCombo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.UserAlineCombo.setObjectName("UserAlineCombo")
        self.gridLayout.addWidget(self.UserAlineCombo, 5, 5, 1, 4)
        self.BookTypeCombo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.BookTypeCombo.setObjectName("BookTypeCombo")
        self.gridLayout.addWidget(self.BookTypeCombo, 4, 1, 1, 3)
        self.label_9.setBuddy(self.UserView)
        self.label_5.setBuddy(self.lineEdit_3)
        self.label.setBuddy(self.BookCombo)
        self.label_3.setBuddy(self.PriceLine)
        self.label_4.setBuddy(self.UserIdLine)
        self.label_2.setBuddy(self.UserCombo)
        self.label_8.setBuddy(self.BookView)

        self.retranslateUi(CheckInfoPage)
        QtCore.QMetaObject.connectSlotsByName(CheckInfoPage)

    def retranslateUi(self, CheckInfoPage):
        _translate = QtCore.QCoreApplication.translate
        CheckInfoPage.setWindowTitle(_translate("CheckInfoPage", "Form"))
        self.label_9.setText(_translate("CheckInfoPage", "Users"))
        self.BookCombo.setItemText(0, _translate("CheckInfoPage", "Basic Book Info"))
        self.BookCombo.setItemText(1, _translate("CheckInfoPage", "Query Book"))
        self.BookCombo.setItemText(2, _translate("CheckInfoPage", "UnReturned Book Info"))
        self.QueryUserButton.setText(_translate("CheckInfoPage", "Query User"))
        self.label_5.setText(_translate("CheckInfoPage", "UserName"))
        self.label.setText(_translate("CheckInfoPage", "Check Type Of Books"))
        self.label_3.setText(_translate("CheckInfoPage", "Price"))
        self.label_6.setText(_translate("CheckInfoPage", "Rent date"))
        self.label_10.setText(_translate("CheckInfoPage", "Book Name"))
        self.label_4.setText(_translate("CheckInfoPage", "UserId"))
        self.UserCombo.setItemText(0, _translate("CheckInfoPage", "Check User Renting History"))
        self.label_2.setText(_translate("CheckInfoPage", "Check Type Of Users"))
        self.label_7.setText(_translate("CheckInfoPage", "Aline Type"))
        self.label_8.setText(_translate("CheckInfoPage", "Books"))
        self.QueryBookButton.setText(_translate("CheckInfoPage", "Query Book"))
        self.toolButton.setText(_translate("CheckInfoPage", "..."))
        self.commandLinkButton.setText(_translate("CheckInfoPage", "More Detail"))
        self.SaveUserButton.setText(_translate("CheckInfoPage", "Save User Info"))
        self.SaveBookButton.setText(_translate("CheckInfoPage", " Save Book Info"))
        self.RefreshButton.setText(_translate("CheckInfoPage", "Refresh"))
        self.GoBackButton.setText(_translate("CheckInfoPage", "Go Back"))
        self.label_12.setText(_translate("CheckInfoPage", "Type"))
        self.label_11.setText(_translate("CheckInfoPage", "Aline Type"))
        self.BookAlineTypeCombo.setItemText(0, _translate("CheckInfoPage", "Desc"))
        self.BookAlineTypeCombo.setItemText(1, _translate("CheckInfoPage", "Asc"))
