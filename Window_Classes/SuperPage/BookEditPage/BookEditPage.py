# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BookEditPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BookEditPage(object):
    def setupUi(self, BookEditPage):
        BookEditPage.setObjectName("BookEditPage")
        BookEditPage.resize(800, 600)
        self.gridLayoutWidget = QtWidgets.QWidget(BookEditPage)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 581))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(50, 50, 50, 50)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.GoBackButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.GoBackButton.setObjectName("GoBackButton")
        self.gridLayout.addWidget(self.GoBackButton, 11, 2, 1, 2)
        self.BookView = QtWidgets.QTableView(self.gridLayoutWidget)
        self.BookView.setObjectName("BookView")
        self.gridLayout.addWidget(self.BookView, 1, 0, 1, 2)
        self.AddTypeButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.AddTypeButton.setObjectName("AddTypeButton")
        self.gridLayout.addWidget(self.AddTypeButton, 11, 4, 1, 1)
        self.BookNameLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.BookNameLine.setObjectName("BookNameLine")
        self.gridLayout.addWidget(self.BookNameLine, 4, 1, 1, 1)
        self.BookIdLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.BookIdLine.setObjectName("BookIdLine")
        self.gridLayout.addWidget(self.BookIdLine, 2, 1, 2, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 4, 3, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 2, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 2, 2, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 2, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 0, 3, 1, 2)
        self.DeleteTypeButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.DeleteTypeButton.setObjectName("DeleteTypeButton")
        self.gridLayout.addWidget(self.DeleteTypeButton, 10, 4, 1, 1)
        self.RefreshButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.RefreshButton.setObjectName("RefreshButton")
        self.gridLayout.addWidget(self.RefreshButton, 9, 2, 1, 2)
        self.StockLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.StockLine.setObjectName("StockLine")
        self.gridLayout.addWidget(self.StockLine, 5, 1, 1, 1)
        self.ChangeBookTypeButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ChangeBookTypeButton.setObjectName("ChangeBookTypeButton")
        self.gridLayout.addWidget(self.ChangeBookTypeButton, 9, 4, 1, 1)
        self.ChangeBookButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ChangeBookButton.setObjectName("ChangeBookButton")
        self.gridLayout.addWidget(self.ChangeBookButton, 9, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 2)
        self.DeleteButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.DeleteButton.setObjectName("DeleteButton")
        self.gridLayout.addWidget(self.DeleteButton, 10, 0, 1, 2)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 5, 3, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 6, 3, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 2, 1, 1)
        self.PriceLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.PriceLine.setObjectName("PriceLine")
        self.gridLayout.addWidget(self.PriceLine, 6, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 10, 2, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.AddBookButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.AddBookButton.setObjectName("AddBookButton")
        self.gridLayout.addWidget(self.AddBookButton, 11, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 2, 3, 2, 2)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 2, 1, 1)
        self.BookTypeView = QtWidgets.QTableView(self.gridLayoutWidget)
        self.BookTypeView.setObjectName("BookTypeView")
        self.gridLayout.addWidget(self.BookTypeView, 1, 3, 1, 2)
        self.BookTypeComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.BookTypeComboBox.setObjectName("BookTypeComboBox")
        self.gridLayout.addWidget(self.BookTypeComboBox, 7, 1, 2, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 7, 0, 2, 1)
        self.label_5.setBuddy(self.StockLine)
        self.label_3.setBuddy(self.BookIdLine)
        self.label_4.setBuddy(self.BookNameLine)
        self.label_6.setBuddy(self.PriceLine)
        self.label_11.setBuddy(self.BookTypeComboBox)

        self.retranslateUi(BookEditPage)
        QtCore.QMetaObject.connectSlotsByName(BookEditPage)

    def retranslateUi(self, BookEditPage):
        _translate = QtCore.QCoreApplication.translate
        BookEditPage.setWindowTitle(_translate("BookEditPage", "Form"))
        self.label_5.setText(_translate("BookEditPage", "Stock"))
        self.GoBackButton.setText(_translate("BookEditPage", "Go Back"))
        self.AddTypeButton.setText(_translate("BookEditPage", "Add Type"))
        self.label_3.setText(_translate("BookEditPage", "Id"))
        self.label_7.setText(_translate("BookEditPage", "TextLabel"))
        self.label_8.setText(_translate("BookEditPage", "TextLabel"))
        self.comboBox_2.setItemText(0, _translate("BookEditPage", "新建项目"))
        self.comboBox_2.setItemText(1, _translate("BookEditPage", "新建项目"))
        self.comboBox_2.setItemText(2, _translate("BookEditPage", "新建项目"))
        self.comboBox_2.setItemText(3, _translate("BookEditPage", "新建项目"))
        self.comboBox_2.setItemText(4, _translate("BookEditPage", "新建项目"))
        self.comboBox_2.setItemText(5, _translate("BookEditPage", "新建项目"))
        self.DeleteTypeButton.setText(_translate("BookEditPage", "DeleteTypeButton"))
        self.RefreshButton.setText(_translate("BookEditPage", "Refresh"))
        self.ChangeBookTypeButton.setText(_translate("BookEditPage", "ChangeBookTypeButton"))
        self.ChangeBookButton.setText(_translate("BookEditPage", "ChangeBookButton"))
        self.comboBox.setItemText(0, _translate("BookEditPage", "Act1"))
        self.comboBox.setItemText(1, _translate("BookEditPage", "新建项目"))
        self.comboBox.setItemText(2, _translate("BookEditPage", "新建项目"))
        self.comboBox.setItemText(3, _translate("BookEditPage", "新建项目"))
        self.comboBox.setItemText(4, _translate("BookEditPage", "新建项目"))
        self.comboBox.setItemText(5, _translate("BookEditPage", "新建项目"))
        self.DeleteButton.setText(_translate("BookEditPage", "DeleteButton"))
        self.label_4.setText(_translate("BookEditPage", "Name"))
        self.label_2.setText(_translate("BookEditPage", "Noting"))
        self.label_9.setText(_translate("BookEditPage", "TextLabel"))
        self.label.setText(_translate("BookEditPage", "TextLabel"))
        self.label_6.setText(_translate("BookEditPage", "Price"))
        self.AddBookButton.setText(_translate("BookEditPage", "Add Book"))
        self.label_10.setText(_translate("BookEditPage", "TextLabel"))
        self.label_11.setText(_translate("BookEditPage", "Type"))
