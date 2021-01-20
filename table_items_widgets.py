from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QCheckBox, QVBoxLayout, QComboBox, QSpinBox


class CheckBoxWidget(QWidget):
    def __init__(self, parent: QWidget = None):
        super(CheckBoxWidget, self).__init__(parent)

        self.checkbox = QCheckBox()

        self.create_gui()

    def create_gui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(5, 3, 5, 3)
        layout.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.checkbox)

        self.setLayout(layout)

    def get_value(self):
        return self.checkbox.isChecked()


class SpinBoxWidget(QWidget):

    def __init__(self, parent: QWidget = None):
        super(SpinBoxWidget, self).__init__(parent)

        self.spinbox = QSpinBox()

        self.create_gui()

    def create_gui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(5,  # left
                                  3,  # top
                                  5,  # right
                                  3)  # bottom
        layout.setAlignment(Qt.AlignCenter)

        self.spinbox.setMinimum(1)
        self.spinbox.setMaximum(5)
        self.spinbox.setSingleStep(1)
        layout.addWidget(self.spinbox)

        self.setLayout(layout)

    def get_value(self):
        return self.spinbox.value()


class ComboOrderWidget(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.combo = QComboBox()

        self.create_gui()

    def create_gui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(5,  # left
                                  3,  # top
                                  5,  # right
                                  3)  # bottom
        layout.setAlignment(Qt.AlignCenter)

        self.combo.addItem("Ascending", 1)
        self.combo.addItem("Descending", 2)
        layout.addWidget(self.combo)

        self.setLayout(layout)

    def get_value(self):
        return self.combo.currentData()
