# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ROIInfoGui.ui'
#
# Created: Sun Mar 15 10:30:38 2015
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ROIInfoWindow(object):
    def setupUi(self, ROIInfoWindow):
        ROIInfoWindow.setObjectName(_fromUtf8("ROIInfoWindow"))
        ROIInfoWindow.resize(409, 309)
        ROIInfoWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(ROIInfoWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(5, 5, 396, 251))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.layoutWidget = QtGui.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(5, 0, 78, 106))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_23 = QtGui.QLabel(self.layoutWidget)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.verticalLayout_6.addWidget(self.label_23)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_6.addWidget(self.label)
        self.label_25 = QtGui.QLabel(self.layoutWidget)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.verticalLayout_6.addWidget(self.label_25)
        self.label_21 = QtGui.QLabel(self.layoutWidget)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.verticalLayout_6.addWidget(self.label_21)
        self.label_30 = QtGui.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(75, 110, 46, 26))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.layoutWidget_3 = QtGui.QWidget(self.frame)
        self.layoutWidget_3.setGeometry(QtCore.QRect(180, 15, 214, 191))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_29 = QtGui.QLabel(self.layoutWidget_3)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.verticalLayout_4.addWidget(self.label_29)
        self.label_5 = QtGui.QLabel(self.layoutWidget_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_4.addWidget(self.label_5)
        self.label_7 = QtGui.QLabel(self.layoutWidget_3)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_4.addWidget(self.label_7)
        self.label_9 = QtGui.QLabel(self.layoutWidget_3)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_4.addWidget(self.label_9)
        self.label_11 = QtGui.QLabel(self.layoutWidget_3)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_4.addWidget(self.label_11)
        self.label_14 = QtGui.QLabel(self.layoutWidget_3)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_4.addWidget(self.label_14)
        self.label_13 = QtGui.QLabel(self.layoutWidget_3)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_4.addWidget(self.label_13)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.txtT1 = QtGui.QTextEdit(self.layoutWidget_3)
        self.txtT1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtT1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtT1.setObjectName(_fromUtf8("txtT1"))
        self.verticalLayout_3.addWidget(self.txtT1)
        self.txtT2 = QtGui.QTextEdit(self.layoutWidget_3)
        self.txtT2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtT2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtT2.setObjectName(_fromUtf8("txtT2"))
        self.verticalLayout_3.addWidget(self.txtT2)
        self.txtADC = QtGui.QTextEdit(self.layoutWidget_3)
        self.txtADC.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtADC.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtADC.setObjectName(_fromUtf8("txtADC"))
        self.verticalLayout_3.addWidget(self.txtADC)
        self.txtConcentration = QtGui.QTextEdit(self.layoutWidget_3)
        self.txtConcentration.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtConcentration.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtConcentration.setObjectName(_fromUtf8("txtConcentration"))
        self.verticalLayout_3.addWidget(self.txtConcentration)
        self.txtProtonDensity = QtGui.QTextEdit(self.layoutWidget_3)
        self.txtProtonDensity.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtProtonDensity.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtProtonDensity.setObjectName(_fromUtf8("txtProtonDensity"))
        self.verticalLayout_3.addWidget(self.txtProtonDensity)
        self.lblAve = QtGui.QTextEdit(self.layoutWidget_3)
        self.lblAve.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lblAve.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lblAve.setObjectName(_fromUtf8("lblAve"))
        self.verticalLayout_3.addWidget(self.lblAve)
        self.lblSd = QtGui.QTextEdit(self.layoutWidget_3)
        self.lblSd.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lblSd.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lblSd.setObjectName(_fromUtf8("lblSd"))
        self.verticalLayout_3.addWidget(self.lblSd)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.layoutWidget_2 = QtGui.QWidget(self.frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(85, 0, 91, 106))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.lblROISet = QtGui.QLabel(self.layoutWidget_2)
        self.lblROISet.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lblROISet.setFrameShape(QtGui.QFrame.WinPanel)
        self.lblROISet.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblROISet.setText(_fromUtf8(""))
        self.lblROISet.setObjectName(_fromUtf8("lblROISet"))
        self.verticalLayout_5.addWidget(self.lblROISet)
        self.lblROIType = QtGui.QLabel(self.layoutWidget_2)
        self.lblROIType.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lblROIType.setFrameShape(QtGui.QFrame.WinPanel)
        self.lblROIType.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblROIType.setText(_fromUtf8(""))
        self.lblROIType.setObjectName(_fromUtf8("lblROIType"))
        self.verticalLayout_5.addWidget(self.lblROIType)
        self.lblROIIndex = QtGui.QLabel(self.layoutWidget_2)
        self.lblROIIndex.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lblROIIndex.setFrameShape(QtGui.QFrame.WinPanel)
        self.lblROIIndex.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblROIIndex.setText(_fromUtf8(""))
        self.lblROIIndex.setObjectName(_fromUtf8("lblROIIndex"))
        self.verticalLayout_5.addWidget(self.lblROIIndex)
        self.txtd1 = QtGui.QTextEdit(self.layoutWidget_2)
        self.txtd1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtd1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtd1.setObjectName(_fromUtf8("txtd1"))
        self.verticalLayout_5.addWidget(self.txtd1)
        self.splitter = QtGui.QSplitter(self.frame)
        self.splitter.setGeometry(QtCore.QRect(5, 130, 166, 76))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget_4 = QtGui.QWidget(self.splitter)
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_15 = QtGui.QLabel(self.layoutWidget_4)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_2.addWidget(self.label_15)
        self.label_19 = QtGui.QLabel(self.layoutWidget_4)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.verticalLayout_2.addWidget(self.label_19)
        self.label_16 = QtGui.QLabel(self.layoutWidget_4)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout_2.addWidget(self.label_16)
        self.layoutWidget_5 = QtGui.QWidget(self.splitter)
        self.layoutWidget_5.setObjectName(_fromUtf8("layoutWidget_5"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.txtXCenter = QtGui.QTextEdit(self.layoutWidget_5)
        self.txtXCenter.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtXCenter.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtXCenter.setObjectName(_fromUtf8("txtXCenter"))
        self.verticalLayout.addWidget(self.txtXCenter)
        self.txtYCenter = QtGui.QTextEdit(self.layoutWidget_5)
        self.txtYCenter.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtYCenter.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtYCenter.setObjectName(_fromUtf8("txtYCenter"))
        self.verticalLayout.addWidget(self.txtYCenter)
        self.txtZCenter = QtGui.QTextEdit(self.layoutWidget_5)
        self.txtZCenter.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtZCenter.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtZCenter.setObjectName(_fromUtf8("txtZCenter"))
        self.verticalLayout.addWidget(self.txtZCenter)
        self.label_28 = QtGui.QLabel(self.frame)
        self.label_28.setGeometry(QtCore.QRect(245, -5, 121, 26))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.pbUpdate = QtGui.QPushButton(self.frame)
        self.pbUpdate.setGeometry(QtCore.QRect(125, 215, 93, 28))
        self.pbUpdate.setObjectName(_fromUtf8("pbUpdate"))
        ROIInfoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ROIInfoWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 409, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuUpdate_Values = QtGui.QMenu(self.menubar)
        self.menuUpdate_Values.setObjectName(_fromUtf8("menuUpdate_Values"))
        ROIInfoWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ROIInfoWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ROIInfoWindow.setStatusBar(self.statusbar)
        self.actionUpdate_values = QtGui.QAction(ROIInfoWindow)
        self.actionUpdate_values.setObjectName(_fromUtf8("actionUpdate_values"))
        self.menubar.addAction(self.menuUpdate_Values.menuAction())

        self.retranslateUi(ROIInfoWindow)
        QtCore.QMetaObject.connectSlotsByName(ROIInfoWindow)

    def retranslateUi(self, ROIInfoWindow):
        ROIInfoWindow.setWindowTitle(QtGui.QApplication.translate("ROIInfoWindow", "ROI Information", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("ROIInfoWindow", "ROI set", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ROIInfoWindow", "ROI type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("ROIInfoWindow", "ROI index", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("ROIInfoWindow", "ROI diameter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate("ROIInfoWindow", "center", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("ROIInfoWindow", "T1 (ms)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ROIInfoWindow", "T2 (ms)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ROIInfoWindow", "ADC*1000 (mm2/s)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ROIInfoWindow", "Concentration (mM)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("ROIInfoWindow", "proton density (%)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("ROIInfoWindow", "Ave signal", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("ROIInfoWindow", "standard deviation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("ROIInfoWindow", "X (mm)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("ROIInfoWindow", "Y (mm)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("ROIInfoWindow", "Z (mm)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("ROIInfoWindow", "Reference Values", None, QtGui.QApplication.UnicodeUTF8))
        self.pbUpdate.setText(QtGui.QApplication.translate("ROIInfoWindow", "update", None, QtGui.QApplication.UnicodeUTF8))
        self.menuUpdate_Values.setTitle(QtGui.QApplication.translate("ROIInfoWindow", "Files", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate_values.setText(QtGui.QApplication.translate("ROIInfoWindow", "Update values", None, QtGui.QApplication.UnicodeUTF8))

