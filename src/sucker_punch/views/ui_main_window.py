# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QMainWindow,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName('MainWindow')
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName('verticalLayout')
        self.frameButton = QFrame(self.centralwidget)
        self.frameButton.setObjectName('frameButton')
        self.frameButton.setMinimumSize(QSize(180, 0))
        self.frameButton.setMaximumSize(QSize(320, 16777215))
        self.frameButton.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameButton.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frameButton)
        self.verticalLayout_2.setObjectName('verticalLayout_2')
        self.push_poin_sale = QPushButton(self.frameButton)
        self.push_poin_sale.setObjectName('push_poin_sale')
        self.push_poin_sale.setMaximumSize(QSize(320, 16777215))
        self.push_poin_sale.setAutoDefault(True)

        self.verticalLayout_2.addWidget(self.push_poin_sale)

        self.push_configuration = QPushButton(self.frameButton)
        self.push_configuration.setObjectName('push_configuration')
        self.push_configuration.setMaximumSize(QSize(320, 16777215))
        self.push_configuration.setAutoDefault(True)

        self.verticalLayout_2.addWidget(self.push_configuration)

        self.verticalLayout.addWidget(
            self.frameButton,
            0,
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter,
        )

        self.frameFooter = QFrame(self.centralwidget)
        self.frameFooter.setObjectName('frameFooter')
        self.frameFooter.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameFooter.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frameFooter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName('menubar')
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName('statusbar')
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate('MainWindow', 'MainWindow', None)
        )
        self.push_poin_sale.setText(
            QCoreApplication.translate('MainWindow', 'Punto de Venta', None)
        )
        self.push_configuration.setText(
            QCoreApplication.translate('MainWindow', 'Configuraci\u00f3n', None)
        )

    # retranslateUi
