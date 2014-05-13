# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Sun Apr 27 21:26:23 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(847, 649)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/pyqode.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = TabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 847, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuModes = QtGui.QMenu(self.menubar)
        self.menuModes.setObjectName(_fromUtf8("menuModes"))
        self.menuPanels = QtGui.QMenu(self.menubar)
        self.menuPanels.setObjectName(_fromUtf8("menuPanels"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.interactiveConsole = InteractiveConsole(self.dockWidgetContents)
        self.interactiveConsole.setObjectName(_fromUtf8("interactiveConsole"))
        self.gridLayout_2.addWidget(self.interactiveConsole, 0, 0, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget)
        self.actionNew = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/document-new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon1)
        self.actionNew.setIconVisibleInMenu(True)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/document-open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon2)
        self.actionOpen.setIconVisibleInMenu(True)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/document-save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setIconVisibleInMenu(True)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_as = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/document-save-as.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as.setIcon(icon4)
        self.actionSave_as.setIconVisibleInMenu(True)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        self.actionClose_tab = QtGui.QAction(MainWindow)
        self.actionClose_tab.setIconVisibleInMenu(True)
        self.actionClose_tab.setObjectName(_fromUtf8("actionClose_tab"))
        self.actionClose_other_tabs = QtGui.QAction(MainWindow)
        self.actionClose_other_tabs.setIconVisibleInMenu(True)
        self.actionClose_other_tabs.setObjectName(_fromUtf8("actionClose_other_tabs"))
        self.actionClose_all_tabs = QtGui.QAction(MainWindow)
        self.actionClose_all_tabs.setIconVisibleInMenu(True)
        self.actionClose_all_tabs.setObjectName(_fromUtf8("actionClose_all_tabs"))
        self.actionQuit = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon5)
        self.actionQuit.setIconVisibleInMenu(True)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionAbout = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/about.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon6)
        self.actionAbout.setIconVisibleInMenu(True)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionRun = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Gnome-Media-Playback-Start.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun.setIcon(icon7)
        self.actionRun.setIconVisibleInMenu(True)
        self.actionRun.setObjectName(_fromUtf8("actionRun"))
        self.actionConfigure_run = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Gnome-System-Run.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConfigure_run.setIcon(icon8)
        self.actionConfigure_run.setIconVisibleInMenu(True)
        self.actionConfigure_run.setObjectName(_fromUtf8("actionConfigure_run"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionConfigure_run)
        self.menuFile.addAction(self.actionRun)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_tab)
        self.menuFile.addAction(self.actionClose_other_tabs)
        self.menuFile.addAction(self.actionClose_all_tabs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menu.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuModes.menuAction())
        self.menubar.addAction(self.menuPanels.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionSave_as)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionConfigure_run)
        self.toolBar.addAction(self.actionRun)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Qidle", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuModes.setTitle(_translate("MainWindow", "Modes", None))
        self.menuPanels.setTitle(_translate("MainWindow", "Panels", None))
        self.menu.setTitle(_translate("MainWindow", "?", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.toolBar.setToolTip(_translate("MainWindow", "Configure run action for current editor", None))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Run output", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionSave_as.setText(_translate("MainWindow", "Save as", None))
        self.actionSave_as.setShortcut(_translate("MainWindow", "Ctrl+Shift+S", None))
        self.actionClose_tab.setText(_translate("MainWindow", "Close tab", None))
        self.actionClose_other_tabs.setText(_translate("MainWindow", "Close other tabs", None))
        self.actionClose_all_tabs.setText(_translate("MainWindow", "Close all tabs", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionAbout.setShortcut(_translate("MainWindow", "F1", None))
        self.actionRun.setText(_translate("MainWindow", "Run", None))
        self.actionRun.setToolTip(_translate("MainWindow", "Run current script", None))
        self.actionConfigure_run.setText(_translate("MainWindow", "Configure run", None))

from pyqode.core.frontend.widgets.tabs import TabWidget
from pyqode.core.frontend.widgets.interactive import InteractiveConsole
from . import resources_rc