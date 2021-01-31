from PySide2.QtCore import QCoreApplication, QMetaObject
from PySide2.QtGui import QResizeEvent
from PySide2.QtWidgets import QAbstractItemView, QFrame, QTableWidget, QWidget, QVBoxLayout


class CsvTable(QTableWidget):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.horizontalHeader().setCascadingSectionResizes(True)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        self.resizeColumnToContents(0)  # column with primers should always fit to content

        new_width = event.size().width() - self.columnWidth(0)
        new_width /= (self.columnCount() - 1)

        for index in range(1, self.columnCount()):
            self.setColumnWidth(index, new_width)


class Ui_CSV_Viewer(object):
    def setupUi(self, CSV_Viewer):
        if not CSV_Viewer.objectName():
            CSV_Viewer.setObjectName(u"CSV_Viewer")
        CSV_Viewer.resize(800, 600)
        self.csv_table = CsvTable(CSV_Viewer)
        self.csv_table.setObjectName(u"csv_table")
        self.csv_table.setFrameShape(QFrame.StyledPanel)
        self.csv_table.setFrameShadow(QFrame.Sunken)
        self.csv_table.setColumnCount(6)
        self.retranslateUi(CSV_Viewer)

        QMetaObject.connectSlotsByName(CSV_Viewer)

        layout = QVBoxLayout()
        layout.addWidget(self.csv_table)
        CSV_Viewer.setLayout(layout)

    def retranslateUi(self, CSV_Viewer):
        CSV_Viewer.setWindowTitle(QCoreApplication.translate("CSV_Viewer", u"CSV_Viewer", None))
