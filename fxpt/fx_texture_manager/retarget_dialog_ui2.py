# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'retarget_dialog_ui.ui'
#
# Created: Sat Nov 19 23:58:06 2016
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(614, 250)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QtCore.QSize(16777215, 250))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.uiLED_retargetRoot = LineEditPath(self.groupBox)
        self.uiLED_retargetRoot.setObjectName("uiLED_retargetRoot")
        self.gridLayout.addWidget(self.uiLED_retargetRoot, 0, 1, 1, 1)
        self.uiCHK_forceRetarget = QtWidgets.QCheckBox(self.groupBox)
        self.uiCHK_forceRetarget.setMinimumSize(QtCore.QSize(0, 20))
        self.uiCHK_forceRetarget.setObjectName("uiCHK_forceRetarget")
        self.gridLayout.addWidget(self.uiCHK_forceRetarget, 1, 1, 1, 1)
        self.uiBTN_browse = QtWidgets.QToolButton(self.groupBox)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiBTN_browse.setIcon(icon)
        self.uiBTN_browse.setIconSize(QtCore.QSize(18, 18))
        self.uiBTN_browse.setObjectName("uiBTN_browse")
        self.gridLayout.addWidget(self.uiBTN_browse, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.uiGRP_useSourceRoot = QtWidgets.QGroupBox(self.groupBox)
        self.uiGRP_useSourceRoot.setCheckable(True)
        self.uiGRP_useSourceRoot.setObjectName("uiGRP_useSourceRoot")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.uiGRP_useSourceRoot)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiLED_sourceRoot = LineEditPath(self.uiGRP_useSourceRoot)
        self.uiLED_sourceRoot.setObjectName("uiLED_sourceRoot")
        self.gridLayout_2.addWidget(self.uiLED_sourceRoot, 0, 1, 1, 1)
        self.uiBTN_browseSource = QtWidgets.QToolButton(self.uiGRP_useSourceRoot)
        self.uiBTN_browseSource.setIcon(icon)
        self.uiBTN_browseSource.setIconSize(QtCore.QSize(18, 18))
        self.uiBTN_browseSource.setObjectName("uiBTN_browseSource")
        self.gridLayout_2.addWidget(self.uiBTN_browseSource, 0, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.uiGRP_useSourceRoot)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.uiGRP_useSourceRoot)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.uiLBL_status = QtWidgets.QLabel(Dialog)
        self.uiLBL_status.setStyleSheet("QLabel {color : red}")
        self.uiLBL_status.setText("")
        self.uiLBL_status.setObjectName("uiLBL_status")
        self.horizontalLayout_2.addWidget(self.uiLBL_status)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.uiBTN_ok = QtWidgets.QPushButton(Dialog)
        self.uiBTN_ok.setObjectName("uiBTN_ok")
        self.horizontalLayout_2.addWidget(self.uiBTN_ok)
        self.uiBTN_cancel = QtWidgets.QPushButton(Dialog)
        self.uiBTN_cancel.setObjectName("uiBTN_cancel")
        self.horizontalLayout_2.addWidget(self.uiBTN_cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.uiBTN_cancel, QtCore.SIGNAL("clicked()"), Dialog.reject)
        QtCore.QObject.connect(self.uiBTN_browse, QtCore.SIGNAL("clicked()"), Dialog.onBrowseClicked)
        QtCore.QObject.connect(Dialog, QtCore.SIGNAL("finished(int)"), Dialog.onDialogFinished)
        QtCore.QObject.connect(self.uiLED_retargetRoot, QtCore.SIGNAL("editingFinished()"), Dialog.onValidateUiNeeded)
        QtCore.QObject.connect(self.uiBTN_ok, QtCore.SIGNAL("clicked()"), Dialog.onOkClicked)
        QtCore.QObject.connect(self.uiBTN_browseSource, QtCore.SIGNAL("clicked()"), Dialog.onBrowseSourceClicked)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.uiLED_retargetRoot, self.uiBTN_browse)
        Dialog.setTabOrder(self.uiBTN_browse, self.uiBTN_cancel)
        Dialog.setTabOrder(self.uiBTN_cancel, self.uiCHK_forceRetarget)
        Dialog.setTabOrder(self.uiCHK_forceRetarget, self.uiBTN_ok)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Retarget", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("Dialog", "Parameters", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "Retarget to:", None, -1))
        self.uiCHK_forceRetarget.setText(QtWidgets.QApplication.translate("Dialog", "Force retarget", None, -1))
        self.uiBTN_browse.setText(QtWidgets.QApplication.translate("Dialog", "...", None, -1))
        self.uiBTN_browse.setShortcut(QtWidgets.QApplication.translate("Dialog", "Ctrl+S, Ctrl+R", None, -1))
        self.uiGRP_useSourceRoot.setTitle(QtWidgets.QApplication.translate("Dialog", "Use source root", None, -1))
        self.uiBTN_browseSource.setText(QtWidgets.QApplication.translate("Dialog", "...", None, -1))
        self.uiBTN_browseSource.setShortcut(QtWidgets.QApplication.translate("Dialog", "Ctrl+S, Ctrl+R", None, -1))
        self.label_16.setText(QtWidgets.QApplication.translate("Dialog", "Source root folder:", None, -1))
        self.uiBTN_ok.setText(QtWidgets.QApplication.translate("Dialog", "OK", None, -1))
        self.uiBTN_cancel.setText(QtWidgets.QApplication.translate("Dialog", "Cancel", None, -1))

from line_edit_path import LineEditPath
import resources_rc2
