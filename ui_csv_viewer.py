
from PySide2.QtCore import (
    QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (
    QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette,
    QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import QFrame, QTableWidget, QSizePolicy


class Ui_CSV_Viewer(object):
    def setupUi(self, CSV_Viewer):
        if not CSV_Viewer.objectName():
            CSV_Viewer.setObjectName(u"CSV_Viewer")
        CSV_Viewer.resize(800, 600)
        self.csv_table = QTableWidget(CSV_Viewer)
        self.csv_table.setObjectName(u"csv_table")
        self.csv_table.setGeometry(QRect(15, 15, 766, 571))
        self.csv_table.setFrameShape(QFrame.StyledPanel)
        self.csv_table.setFrameShadow(QFrame.Sunken)
        self.csv_table.setSortingEnabled(True)
        self.csv_table.setRowCount(0)
        self.csv_table.setColumnCount(6)
        self.retranslateUi(CSV_Viewer)

        QMetaObject.connectSlotsByName(CSV_Viewer)
    # setupUi

    def retranslateUi(self, CSV_Viewer):
        CSV_Viewer.setWindowTitle(QCoreApplication.translate(
            "CSV_Viewer", u"CSV_Viewer", None))

    # retranslateUi

