# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DFA.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1161, 664)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1161, 591))
        self.tabWidget.setToolTip("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 181, 19))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 551, 111))
        self.textEdit.setObjectName("textEdit")
        self.checkButton = QtWidgets.QPushButton(self.tab)
        self.checkButton.setGeometry(QtCore.QRect(444, 150, 111, 35))
        self.checkButton.setObjectName("checkButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 200, 501, 341))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 51, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(70, 40, 191, 19))
        self.label_5.setObjectName("label_5")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(10, 100, 471, 61))
        self.label_17.setObjectName("label_17")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(10, 70, 81, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(100, 70, 131, 19))
        self.label_13.setObjectName("label_13")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(570, 0, 581, 541))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(140, 350, 311, 161))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 81, 19))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 240, 191, 19))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 80, 531, 41))
        self.label.setObjectName("label")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(10, 130, 551, 61))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(20, 300, 251, 31))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(30, 360, 66, 19))
        self.label_16.setObjectName("label_16")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 451, 19))
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 230, 601, 321))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(70, 40, 121, 19))
        self.label_8.setObjectName("label_8")
        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        self.label_18.setGeometry(QtCore.QRect(10, 80, 161, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox_3)
        self.label_19.setGeometry(QtCore.QRect(10, 110, 581, 201))
        self.label_19.setObjectName("label_19")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(10, 50, 821, 151))
        self.label_12.setObjectName("label_12")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(620, 230, 521, 321))
        self.groupBox_4.setObjectName("groupBox_4")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.groupBox_4)
        self.tableWidget_3.setGeometry(QtCore.QRect(30, 40, 461, 191))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(4)
        self.tableWidget_3.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(4, 3, item)
        self.label_21 = QtWidgets.QLabel(self.groupBox_4)
        self.label_21.setGeometry(QtCore.QRect(30, 250, 231, 19))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.groupBox_4)
        self.label_22.setGeometry(QtCore.QRect(30, 280, 231, 19))
        self.label_22.setObjectName("label_22")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(850, 70, 241, 91))
        self.label_20.setObjectName("label_20")
        self.tabWidget.addTab(self.tab_2, "")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(1050, 600, 95, 35))
        self.exitButton.setObjectName("exitButton")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "DFA Demo"))
        self.label_3.setText(_translate("mainWindow", "Examples: aaabbb, aa, bb"))
        self.checkButton.setText(_translate("mainWindow", "Check String"))
        self.groupBox_2.setTitle(_translate("mainWindow", "Output"))
        self.label_4.setText(_translate("mainWindow", "Status:"))
        self.label_5.setText(_translate("mainWindow", "Waiting for input"))
        self.label_17.setText(_translate("mainWindow", "<html><head/><body><p>To know more about transitions made, click on the <span style=\" font-weight:600;\">DFA Diagram </span></p><p><span style=\" font-weight:600;\">and String Analysis</span> tab</p></body></html>"))
        self.label_10.setText(_translate("mainWindow", "Last State:"))
        self.label_13.setText(_translate("mainWindow", "Waiting for input"))
        self.groupBox.setTitle(_translate("mainWindow", "Machine Specifications"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("mainWindow", "Number of States (Q)"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("mainWindow", "Alphabets (Σ)"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("mainWindow", "Number of Initial States (q0)"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("mainWindow", "Number of Final States (F)"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "#"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("mainWindow", "6"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("mainWindow", "{a,b}"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("mainWindow", "1"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("mainWindow", "2"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("mainWindow", "Language:"))
        self.label_7.setText(_translate("mainWindow", "Machine Characteristics:"))
        self.label.setText(_translate("mainWindow", "<html><head/><body><p><img src=\":/root/Lang.png\"/></p></body></html>"))
        self.label_14.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\">To know more about this language and view the transition diagram, click on the </p><p align=\"center\"><span style=\" font-weight:600;\">DFA Diagram and String Analysis</span> tab</p></body></html>"))
        self.label_15.setText(_translate("mainWindow", "<html><head/><body><p><img src=\":/root/machine.png\"/></p></body></html>"))
        self.label_16.setText(_translate("mainWindow", "where,"))
        self.label_9.setText(_translate("mainWindow", "Enter any string in the textbox below with only {a, b} as alphabets"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainWindow", "Testing DFA"))
        self.label_11.setText(_translate("mainWindow", "Transition Diagram:"))
        self.groupBox_3.setTitle(_translate("mainWindow", "Current Input"))
        self.label_6.setText(_translate("mainWindow", "String:"))
        self.label_8.setText(_translate("mainWindow", "Waiting for input"))
        self.label_18.setText(_translate("mainWindow", "Path taken by string:"))
        self.label_19.setText(_translate("mainWindow", "Waiting for Input"))
        self.label_12.setText(_translate("mainWindow", "<html><head/><body><p><img src=\":/root/g1.png\"/></p></body></html>"))
        self.groupBox_4.setTitle(_translate("mainWindow", "Transition Table and Transition Function:"))
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("mainWindow", "→*q0"))
        item = self.tableWidget_3.verticalHeaderItem(1)
        item.setText(_translate("mainWindow", "q1"))
        item = self.tableWidget_3.verticalHeaderItem(2)
        item.setText(_translate("mainWindow", "*q2"))
        item = self.tableWidget_3.verticalHeaderItem(3)
        item.setText(_translate("mainWindow", "*q3"))
        item = self.tableWidget_3.verticalHeaderItem(4)
        item.setText(_translate("mainWindow", "q4"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "a"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "b"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "𝛿 for a"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("mainWindow", "𝛿 for b"))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        item = self.tableWidget_3.item(0, 0)
        item.setText(_translate("mainWindow", "q1"))
        item = self.tableWidget_3.item(0, 1)
        item.setText(_translate("mainWindow", "q4"))
        item = self.tableWidget_3.item(0, 2)
        item.setText(_translate("mainWindow", "𝛿(q0, a) = q1"))
        item = self.tableWidget_3.item(0, 3)
        item.setText(_translate("mainWindow", "𝛿(q0, b) = q4"))
        item = self.tableWidget_3.item(1, 0)
        item.setText(_translate("mainWindow", "q2"))
        item = self.tableWidget_3.item(1, 1)
        item.setText(_translate("mainWindow", "q3"))
        item = self.tableWidget_3.item(1, 2)
        item.setText(_translate("mainWindow", "𝛿(q1, a) = q2"))
        item = self.tableWidget_3.item(1, 3)
        item.setText(_translate("mainWindow", "𝛿(q1, b) = q3"))
        item = self.tableWidget_3.item(2, 0)
        item.setText(_translate("mainWindow", "q1"))
        item = self.tableWidget_3.item(2, 1)
        item.setText(_translate("mainWindow", "q4"))
        item = self.tableWidget_3.item(2, 2)
        item.setText(_translate("mainWindow", "𝛿(q2, a) = q1"))
        item = self.tableWidget_3.item(2, 3)
        item.setText(_translate("mainWindow", "𝛿(q2, b) = q4"))
        item = self.tableWidget_3.item(3, 0)
        item.setText(_translate("mainWindow", "D"))
        item = self.tableWidget_3.item(3, 1)
        item.setText(_translate("mainWindow", "q4"))
        item = self.tableWidget_3.item(3, 2)
        item.setText(_translate("mainWindow", "𝛿(q3, a) = D"))
        item = self.tableWidget_3.item(3, 3)
        item.setText(_translate("mainWindow", "𝛿(q3, b) = q4"))
        item = self.tableWidget_3.item(4, 0)
        item.setText(_translate("mainWindow", "D"))
        item = self.tableWidget_3.item(4, 1)
        item.setText(_translate("mainWindow", "q4"))
        item = self.tableWidget_3.item(4, 2)
        item.setText(_translate("mainWindow", "𝛿(q4, a) = D"))
        item = self.tableWidget_3.item(4, 3)
        item.setText(_translate("mainWindow", "𝛿(q4, b) = q4"))
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        self.label_21.setText(_translate("mainWindow", "* marked states are final states."))
        self.label_22.setText(_translate("mainWindow", "→ marked states are start states."))
        self.label_20.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Examples of strings accepted:</span></p><p>λ,ab,aabb,...</p><p>where, λ = Null string</p><p><br/></p><p><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainWindow", "DFA Diagram and String Analysis"))
        self.exitButton.setText(_translate("mainWindow", "Exit"))
import Language_rc