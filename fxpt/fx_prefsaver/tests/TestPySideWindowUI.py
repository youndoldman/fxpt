# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestQtWindowUI.ui'
#
# Created: Mon Oct 27 20:53:21 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(771, 584)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout.addWidget(self.comboBox_2)
        self.uiBTN_showDialog = QtGui.QPushButton(self.centralwidget)
        self.uiBTN_showDialog.setObjectName("uiBTN_showDialog")
        self.verticalLayout.addWidget(self.uiBTN_showDialog)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget = QtGui.QListWidget(self.tab)
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName("listWidget")
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        self.horizontalLayout_2.addWidget(self.listWidget)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.treeView = QtGui.QTreeView(self.tab_2)
        self.treeView.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.treeView.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.treeView.setObjectName("treeView")
        self.horizontalLayout_3.addWidget(self.treeView)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tab_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableWidget = QtGui.QTableWidget(self.tab_3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(7)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        self.horizontalLayout_4.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout_6.addWidget(self.tabWidget)
        self.horizontalLayout_6.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.uiBTN_savePrefs = QtGui.QPushButton(self.centralwidget)
        self.uiBTN_savePrefs.setObjectName("uiBTN_savePrefs")
        self.horizontalLayout_5.addWidget(self.uiBTN_savePrefs)
        self.uiBTN_loadPrefs = QtGui.QPushButton(self.centralwidget)
        self.uiBTN_loadPrefs.setObjectName("uiBTN_loadPrefs")
        self.horizontalLayout_5.addWidget(self.uiBTN_loadPrefs)
        self.uiBTN_resetPrefs = QtGui.QPushButton(self.centralwidget)
        self.uiBTN_resetPrefs.setObjectName("uiBTN_resetPrefs")
        self.horizontalLayout_5.addWidget(self.uiBTN_resetPrefs)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QObject.connect(self.uiBTN_savePrefs, QtCore.SIGNAL("clicked()"), MainWindow.onSavePrefsClicked)
        QtCore.QObject.connect(self.uiBTN_loadPrefs, QtCore.SIGNAL("clicked()"), MainWindow.onLoadPrefsClicked)
        QtCore.QObject.connect(self.uiBTN_resetPrefs, QtCore.SIGNAL("clicked()"), MainWindow.onResetPrefsClicked)
        QtCore.QObject.connect(self.uiBTN_showDialog, QtCore.SIGNAL("clicked()"), MainWindow.onShowDialogClicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", "CheckBox", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("MainWindow", "RadioButton1", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("MainWindow", "RadioButton2", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Check Button", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "Item1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "Item2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "Item3", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("MainWindow", "Item4", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("MainWindow", "Item5", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(5, QtGui.QApplication.translate("MainWindow", "Item6", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(6, QtGui.QApplication.translate("MainWindow", "Item7", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBTN_showDialog.setText(QtGui.QApplication.translate("MainWindow", "Show Dialog", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.item(0).setText(QtGui.QApplication.translate("MainWindow", "Item1", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(1).setText(QtGui.QApplication.translate("MainWindow", "Item2", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(2).setText(QtGui.QApplication.translate("MainWindow", "Item3", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(3).setText(QtGui.QApplication.translate("MainWindow", "Item4", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(4).setText(QtGui.QApplication.translate("MainWindow", "Item5", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(5).setText(QtGui.QApplication.translate("MainWindow", "Item6", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(6).setText(QtGui.QApplication.translate("MainWindow", "Item7", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "List Widget", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Tree Widget", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Row1", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Row2", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Row3", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "Row4", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindow", "Row5", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(5).setText(QtGui.QApplication.translate("MainWindow", "Row6", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(6).setText(QtGui.QApplication.translate("MainWindow", "Row7", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Column1", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Column2", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.item(0, 0).setText(QtGui.QApplication.translate("MainWindow", "value11", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.item(0, 1).setText(QtGui.QApplication.translate("MainWindow", "value12", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.item(1, 0).setText(QtGui.QApplication.translate("MainWindow", "value21", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.item(1, 1).setText(QtGui.QApplication.translate("MainWindow", "value22", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.item(2, 0).setText(QtGui.QApplication.translate("MainWindow", "value31", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.item(2, 1).setText(QtGui.QApplication.translate("MainWindow", "value32", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.item(3, 0).setText(QtGui.QApplication.translate("MainWindow", "value41", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.item(3, 1).setText(QtGui.QApplication.translate("MainWindow", "value42", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.item(4, 0).setText(QtGui.QApplication.translate("MainWindow", "value51", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.item(4, 1).setText(QtGui.QApplication.translate("MainWindow", "value52", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.item(5, 0).setText(QtGui.QApplication.translate("MainWindow", "value61", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.item(5, 1).setText(QtGui.QApplication.translate("MainWindow", "value62", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.item(6, 0).setText(QtGui.QApplication.translate("MainWindow", "value71", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.item(6, 1).setText(QtGui.QApplication.translate("MainWindow", "value72", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Table Widget", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBTN_savePrefs.setText(QtGui.QApplication.translate("MainWindow", "Save Prefs", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBTN_loadPrefs.setText(QtGui.QApplication.translate("MainWindow", "Load Prefs", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBTN_resetPrefs.setText(QtGui.QApplication.translate("MainWindow", "Reset Prefs", None, QtGui.QApplication.UnicodeUTF8))

