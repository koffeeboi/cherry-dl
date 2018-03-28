# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/CherryDesigner/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(706, 581)
        MainWindow.setMinimumSize(QtCore.QSize(706, 0))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.home)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.progressBar = QtWidgets.QProgressBar(self.home)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_3.addWidget(self.progressBar, 1, 0, 1, 2)
        self.run = QtWidgets.QPushButton(self.home)
        self.run.setObjectName("run")
        self.gridLayout_3.addWidget(self.run, 0, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.home)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 652, 446))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.title = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 0, 0, 1, 1)
        self.description = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.description.setObjectName("description")
        self.gridLayout.addWidget(self.description, 2, 0, 1, 1)
        self.image = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.image.setObjectName("image")
        self.gridLayout.addWidget(self.image, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 2, 0, 1, 2)
        self.url = QtWidgets.QLineEdit(self.home)
        self.url.setObjectName("url")
        self.gridLayout_3.addWidget(self.url, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.home)
        self.progress = QtWidgets.QWidget()
        self.progress.setObjectName("progress")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.progress)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listView = QtWidgets.QListView(self.progress)
        self.listView.setObjectName("listView")
        self.gridLayout_2.addWidget(self.listView, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.progress)
        self.history = QtWidgets.QWidget()
        self.history.setObjectName("history")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.history)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.listView_2 = QtWidgets.QListView(self.history)
        self.listView_2.setObjectName("listView_2")
        self.gridLayout_4.addWidget(self.listView_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.history)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 706, 20))
        self.menuBar.setObjectName("menuBar")
        self.menuCherry = QtWidgets.QMenu(self.menuBar)
        self.menuCherry.setObjectName("menuCherry")
        self.menuOptions = QtWidgets.QMenu(self.menuBar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.menuCherry.addSeparator()
        self.menuCherry.addAction(self.actionQuit)
        self.menuOptions.addAction(self.actionPreferences)
        self.menuBar.addAction(self.menuCherry.menuAction())
        self.menuBar.addAction(self.menuOptions.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.run.setText(_translate("MainWindow", "Run"))
        self.title.setText(_translate("MainWindow", "Title here"))
        self.description.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">More information here....</p></body></html>"))
        self.image.setText(_translate("MainWindow", "Image here"))
        self.menuCherry.setTitle(_translate("MainWindow", "File"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
