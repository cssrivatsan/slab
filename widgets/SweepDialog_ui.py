# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/SweepDialog.ui'
#
# Created: Mon Apr  9 13:32:57 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SweepDialog(object):
    def setupUi(self, SweepDialog):
        SweepDialog.setObjectName(_fromUtf8("SweepDialog"))
        SweepDialog.resize(421, 609)
        SweepDialog.setWindowTitle(QtGui.QApplication.translate("SweepDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayoutWidget = QtGui.QWidget(SweepDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 401, 571))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.sweep1_groupBox = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.sweep1_groupBox.setTitle(QtGui.QApplication.translate("SweepDialog", "Sweep 1", None, QtGui.QApplication.UnicodeUTF8))
        self.sweep1_groupBox.setObjectName(_fromUtf8("sweep1_groupBox"))
        self.gridLayoutWidget = QtGui.QWidget(self.sweep1_groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 19, 361, 128))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setText(QtGui.QApplication.translate("SweepDialog", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.param_sweep1_start = QtGui.QSpinBox(self.gridLayoutWidget)
        self.param_sweep1_start.setObjectName(_fromUtf8("param_sweep1_start"))
        self.gridLayout.addWidget(self.param_sweep1_start, 1, 1, 1, 1)
        self.param_sweep1 = QtGui.QComboBox(self.gridLayoutWidget)
        self.param_sweep1.setObjectName(_fromUtf8("param_sweep1"))
        self.gridLayout.addWidget(self.param_sweep1, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setText(QtGui.QApplication.translate("SweepDialog", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setText(QtGui.QApplication.translate("SweepDialog", "Step", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.param_sweep1_stop = QtGui.QSpinBox(self.gridLayoutWidget)
        self.param_sweep1_stop.setObjectName(_fromUtf8("param_sweep1_stop"))
        self.gridLayout.addWidget(self.param_sweep1_stop, 2, 1, 1, 1)
        self.param_sweep1_step = QtGui.QSpinBox(self.gridLayoutWidget)
        self.param_sweep1_step.setObjectName(_fromUtf8("param_sweep1_step"))
        self.gridLayout.addWidget(self.param_sweep1_step, 3, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setText(QtGui.QApplication.translate("SweepDialog", "Parameter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.sweep1_groupBox)
        self.param_enable_sweep2 = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.param_enable_sweep2.setText(QtGui.QApplication.translate("SweepDialog", "Enable Sweep 2", None, QtGui.QApplication.UnicodeUTF8))
        self.param_enable_sweep2.setChecked(True)
        self.param_enable_sweep2.setObjectName(_fromUtf8("param_enable_sweep2"))
        self.verticalLayout.addWidget(self.param_enable_sweep2)
        self.sweep2_groupBox = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.sweep2_groupBox.setTitle(QtGui.QApplication.translate("SweepDialog", "Sweep 2", None, QtGui.QApplication.UnicodeUTF8))
        self.sweep2_groupBox.setObjectName(_fromUtf8("sweep2_groupBox"))
        self.gridLayoutWidget_3 = QtGui.QWidget(self.sweep2_groupBox)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(9, 19, 361, 140))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_5.setText(QtGui.QApplication.translate("SweepDialog", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.param_sweep2_start = QtGui.QSpinBox(self.gridLayoutWidget_3)
        self.param_sweep2_start.setObjectName(_fromUtf8("param_sweep2_start"))
        self.gridLayout_3.addWidget(self.param_sweep2_start, 1, 1, 1, 1)
        self.param_sweep2 = QtGui.QComboBox(self.gridLayoutWidget_3)
        self.param_sweep2.setObjectName(_fromUtf8("param_sweep2"))
        self.gridLayout_3.addWidget(self.param_sweep2, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_6.setText(QtGui.QApplication.translate("SweepDialog", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_7.setText(QtGui.QApplication.translate("SweepDialog", "Step", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_3.addWidget(self.label_7, 3, 0, 1, 1)
        self.param_sweep2_stop = QtGui.QSpinBox(self.gridLayoutWidget_3)
        self.param_sweep2_stop.setObjectName(_fromUtf8("param_sweep2_stop"))
        self.gridLayout_3.addWidget(self.param_sweep2_stop, 2, 1, 1, 1)
        self.param_sweep2_step = QtGui.QSpinBox(self.gridLayoutWidget_3)
        self.param_sweep2_step.setObjectName(_fromUtf8("param_sweep2_step"))
        self.gridLayout_3.addWidget(self.param_sweep2_step, 3, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_8.setText(QtGui.QApplication.translate("SweepDialog", "Parameter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.sweep2_groupBox)
        self.groupBox = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setTitle(QtGui.QApplication.translate("SweepDialog", "Actions", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 379, 124))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.addActionButton = QtGui.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addActionButton.sizePolicy().hasHeightForWidth())
        self.addActionButton.setSizePolicy(sizePolicy)
        self.addActionButton.setText(QtGui.QApplication.translate("SweepDialog", "add", None, QtGui.QApplication.UnicodeUTF8))
        self.addActionButton.setObjectName(_fromUtf8("addActionButton"))
        self.gridLayout_2.addWidget(self.addActionButton, 0, 1, 1, 1)
        self.actions_comboBox = QtGui.QComboBox(self.gridLayoutWidget_2)
        self.actions_comboBox.setObjectName(_fromUtf8("actions_comboBox"))
        self.gridLayout_2.addWidget(self.actions_comboBox, 0, 0, 1, 1)
        self.param_actions = QtGui.QTextBrowser(self.gridLayoutWidget_2)
        self.param_actions.setObjectName(_fromUtf8("param_actions"))
        self.gridLayout_2.addWidget(self.param_actions, 1, 0, 1, 1)
        self.clearActionsButton = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.clearActionsButton.setText(QtGui.QApplication.translate("SweepDialog", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.clearActionsButton.setObjectName(_fromUtf8("clearActionsButton"))
        self.gridLayout_2.addWidget(self.clearActionsButton, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(SweepDialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 570, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(SweepDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SweepDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SweepDialog.reject)
        QtCore.QObject.connect(self.param_enable_sweep2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.sweep2_groupBox.setVisible)
        QtCore.QMetaObject.connectSlotsByName(SweepDialog)

    def retranslateUi(self, SweepDialog):
        pass

