# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Bits(object):
    def setupUi(self, Bits):
        if not Bits.objectName():
            Bits.setObjectName(u"Bits")
        Bits.resize(422, 715)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Bits.sizePolicy().hasHeightForWidth())
        Bits.setSizePolicy(sizePolicy)
        Bits.setDocumentMode(False)
        self.centralwidget = QWidget(Bits)
        self.centralwidget.setObjectName(u"centralwidget")
        self.toolBox = QToolBox(self.centralwidget)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setGeometry(QRect(25, 18, 373, 637))
        self.title_page = QWidget()
        self.title_page.setObjectName(u"title_page")
        self.title_page.setGeometry(QRect(0, 0, 373, 467))
        self.title_up_line = QFrame(self.title_page)
        self.title_up_line.setObjectName(u"title_up_line")
        self.title_up_line.setGeometry(QRect(20, 65, 331, 21))
        self.title_up_line.setFrameShape(QFrame.HLine)
        self.title_up_line.setFrameShadow(QFrame.Sunken)
        self.title_label = QLabel(self.title_page)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(80, 80, 211, 36))
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_down_line = QFrame(self.title_page)
        self.title_down_line.setObjectName(u"title_down_line")
        self.title_down_line.setGeometry(QRect(20, 115, 331, 21))
        self.title_down_line.setFrameShape(QFrame.HLine)
        self.title_down_line.setFrameShadow(QFrame.Sunken)
        self.author_label = QLabel(self.title_page)
        self.author_label.setObjectName(u"author_label")
        self.author_label.setGeometry(QRect(65, 145, 246, 21))
        font1 = QFont()
        font1.setPointSize(15)
        self.author_label.setFont(font1)
        self.author_label.setAlignment(Qt.AlignCenter)
        self.ver_label = QLabel(self.title_page)
        self.ver_label.setObjectName(u"ver_label")
        self.ver_label.setGeometry(QRect(65, 175, 246, 16))
        self.ver_label.setAlignment(Qt.AlignCenter)
        self.toolBox.addItem(self.title_page, u"Title")
        self.genrator_page = QWidget()
        self.genrator_page.setObjectName(u"genrator_page")
        self.genrator_page.setGeometry(QRect(0, 0, 373, 467))
        self.primers_groupBox = QGroupBox(self.genrator_page)
        self.primers_groupBox.setObjectName(u"primers_groupBox")
        self.primers_groupBox.setGeometry(QRect(20, 36, 330, 100))
        self.primers_length_2 = QLabel(self.primers_groupBox)
        self.primers_length_2.setObjectName(u"primers_length_2")
        self.primers_length_2.setGeometry(QRect(25, 35, 59, 21))
        self.numbers_of_primers = QLabel(self.primers_groupBox)
        self.numbers_of_primers.setObjectName(u"numbers_of_primers")
        self.numbers_of_primers.setGeometry(QRect(25, 65, 126, 21))
        self.primers_length_spinBox = QSpinBox(self.primers_groupBox)
        self.primers_length_spinBox.setObjectName(u"primers_length_spinBox")
        self.primers_length_spinBox.setGeometry(QRect(251, 30, 66, 22))
        self.primers_length_spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.primers_length_spinBox.setValue(20)
        self.number_of_primers_spinBox = QSpinBox(self.primers_groupBox)
        self.number_of_primers_spinBox.setObjectName(u"number_of_primers_spinBox")
        self.number_of_primers_spinBox.setGeometry(QRect(251, 60, 66, 22))
        self.number_of_primers_spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.number_of_primers_spinBox.setMaximum(1000000000)
        self.number_of_primers_spinBox.setSingleStep(200)
        self.number_of_primers_spinBox.setValue(1000)
        self.generator_out_file_pushButton = QPushButton(self.genrator_page)
        self.generator_out_file_pushButton.setObjectName(u"generator_out_file_pushButton")
        self.generator_out_file_pushButton.setGeometry(QRect(12, 0, 113, 32))
        self.generator_out_file_lineEdit = QLineEdit(self.genrator_page)
        self.generator_out_file_lineEdit.setObjectName(u"generator_out_file_lineEdit")
        self.generator_out_file_lineEdit.setGeometry(QRect(136, 2, 199, 25))
        self.temp_groupBox = QGroupBox(self.genrator_page)
        self.temp_groupBox.setObjectName(u"temp_groupBox")
        self.temp_groupBox.setGeometry(QRect(20, 145, 330, 100))
        self.temp_groupBox.setCheckable(True)
        self.min_temp = QLabel(self.temp_groupBox)
        self.min_temp.setObjectName(u"min_temp")
        self.min_temp.setGeometry(QRect(25, 35, 59, 21))
        self.max_temp = QLabel(self.temp_groupBox)
        self.max_temp.setObjectName(u"max_temp")
        self.max_temp.setGeometry(QRect(25, 65, 59, 21))
        self.tmmin_doubleSpinBox = QDoubleSpinBox(self.temp_groupBox)
        self.tmmin_doubleSpinBox.setObjectName(u"tmmin_doubleSpinBox")
        self.tmmin_doubleSpinBox.setGeometry(QRect(261, 30, 56, 22))
        self.tmmin_doubleSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.tmmin_doubleSpinBox.setSingleStep(0.050000000000000)
        self.tmmin_doubleSpinBox.setValue(58.000000000000000)
        self.tmmax_doubleSpinBox = QDoubleSpinBox(self.temp_groupBox)
        self.tmmax_doubleSpinBox.setObjectName(u"tmmax_doubleSpinBox")
        self.tmmax_doubleSpinBox.setGeometry(QRect(261, 60, 56, 22))
        self.tmmax_doubleSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.tmmax_doubleSpinBox.setSingleStep(0.050000000000000)
        self.tmmax_doubleSpinBox.setValue(62.000000000000000)
        self.gccontent_groupBox = QGroupBox(self.genrator_page)
        self.gccontent_groupBox.setObjectName(u"gccontent_groupBox")
        self.gccontent_groupBox.setGeometry(QRect(20, 255, 330, 100))
        self.gccontent_groupBox.setCheckable(True)
        self.gc_min = QLabel(self.gccontent_groupBox)
        self.gc_min.setObjectName(u"gc_min")
        self.gc_min.setGeometry(QRect(25, 35, 59, 21))
        self.gc_max = QLabel(self.gccontent_groupBox)
        self.gc_max.setObjectName(u"gc_max")
        self.gc_max.setGeometry(QRect(25, 65, 59, 21))
        self.gcmin_doubleSpinBox = QDoubleSpinBox(self.gccontent_groupBox)
        self.gcmin_doubleSpinBox.setObjectName(u"gcmin_doubleSpinBox")
        self.gcmin_doubleSpinBox.setGeometry(QRect(256, 30, 61, 22))
        self.gcmin_doubleSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gcmin_doubleSpinBox.setMaximum(1.000000000000000)
        self.gcmin_doubleSpinBox.setSingleStep(0.010000000000000)
        self.gcmin_doubleSpinBox.setValue(0.480000000000000)
        self.gcmax_doubleSpinBox = QDoubleSpinBox(self.gccontent_groupBox)
        self.gcmax_doubleSpinBox.setObjectName(u"gcmax_doubleSpinBox")
        self.gcmax_doubleSpinBox.setGeometry(QRect(256, 60, 61, 22))
        self.gcmax_doubleSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gcmax_doubleSpinBox.setMaximum(1.000000000000000)
        self.gcmax_doubleSpinBox.setSingleStep(0.010000000000000)
        self.gcmax_doubleSpinBox.setValue(0.520000000000000)
        self.parameters_groupBox = QGroupBox(self.genrator_page)
        self.parameters_groupBox.setObjectName(u"parameters_groupBox")
        self.parameters_groupBox.setGeometry(QRect(15, 370, 176, 66))
        self.runs_checkBox = QCheckBox(self.parameters_groupBox)
        self.runs_checkBox.setObjectName(u"runs_checkBox")
        self.runs_checkBox.setGeometry(QRect(15, 30, 61, 20))
        self.runs_checkBox.setChecked(True)
        self.repeats_checkBox = QCheckBox(self.parameters_groupBox)
        self.repeats_checkBox.setObjectName(u"repeats_checkBox")
        self.repeats_checkBox.setGeometry(QRect(85, 30, 86, 20))
        self.repeats_checkBox.setChecked(True)
        self.start_pushButton = QPushButton(self.genrator_page)
        self.start_pushButton.setObjectName(u"start_pushButton")
        self.start_pushButton.setGeometry(QRect(220, 390, 113, 32))
        self.generate_progressBar_3 = QProgressBar(self.genrator_page)
        self.generate_progressBar_3.setObjectName(u"generate_progressBar_3")
        self.generate_progressBar_3.setGeometry(QRect(202, 415, 151, 23))
        self.generate_progressBar_3.setValue(24)
        self.toolBox.addItem(self.genrator_page, u"Generator")
        self.formater_page = QWidget()
        self.formater_page.setObjectName(u"formater_page")
        self.formater_page.setGeometry(QRect(0, 0, 373, 467))
        self.csv_preview_pushButton = QPushButton(self.formater_page)
        self.csv_preview_pushButton.setObjectName(u"csv_preview_pushButton")
        self.csv_preview_pushButton.setGeometry(QRect(190, 390, 121, 32))
        self.generate_progressBar = QProgressBar(self.formater_page)
        self.generate_progressBar.setObjectName(u"generate_progressBar")
        self.generate_progressBar.setGeometry(QRect(232, 270, 118, 31))
        self.generate_progressBar.setValue(0)
        self.generate_csv_pushButton = QPushButton(self.formater_page)
        self.generate_csv_pushButton.setObjectName(u"generate_csv_pushButton")
        self.generate_csv_pushButton.setGeometry(QRect(22, 350, 201, 32))
        self.generate_csv_progressBar = QProgressBar(self.formater_page)
        self.generate_csv_progressBar.setObjectName(u"generate_csv_progressBar")
        self.generate_csv_progressBar.setGeometry(QRect(232, 350, 118, 31))
        self.generate_csv_progressBar.setValue(0)
        self.file_in_label = QLabel(self.formater_page)
        self.file_in_label.setObjectName(u"file_in_label")
        self.file_in_label.setGeometry(QRect(152, 10, 191, 31))
        self.file_in_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.run_pr3_pushButton = QPushButton(self.formater_page)
        self.run_pr3_pushButton.setObjectName(u"run_pr3_pushButton")
        self.run_pr3_pushButton.setGeometry(QRect(22, 311, 131, 26))
        self.sequence_id_lineEdit = QLineEdit(self.formater_page)
        self.sequence_id_lineEdit.setObjectName(u"sequence_id_lineEdit")
        self.sequence_id_lineEdit.setGeometry(QRect(117, 80, 236, 21))
        self.sequence_id_label = QLabel(self.formater_page)
        self.sequence_id_label.setObjectName(u"sequence_id_label")
        self.sequence_id_label.setGeometry(QRect(22, 80, 111, 21))
        self.file_out_lineEdit = QLineEdit(self.formater_page)
        self.file_out_lineEdit.setObjectName(u"file_out_lineEdit")
        self.file_out_lineEdit.setGeometry(QRect(172, 45, 181, 21))
        self.file_out_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.file_in_pushButton = QPushButton(self.formater_page)
        self.file_in_pushButton.setObjectName(u"file_in_pushButton")
        self.file_in_pushButton.setGeometry(QRect(12, 10, 113, 32))
        self.generate_pushButton = QPushButton(self.formater_page)
        self.generate_pushButton.setObjectName(u"generate_pushButton")
        self.generate_pushButton.setGeometry(QRect(22, 270, 201, 32))
        self.primer3_param_groupBox = QGroupBox(self.formater_page)
        self.primer3_param_groupBox.setObjectName(u"primer3_param_groupBox")
        self.primer3_param_groupBox.setGeometry(QRect(22, 110, 330, 150))
        self.mv_con_label = QLabel(self.primer3_param_groupBox)
        self.mv_con_label.setObjectName(u"mv_con_label")
        self.mv_con_label.setGeometry(QRect(20, 30, 141, 21))
        self.dv_con_label = QLabel(self.primer3_param_groupBox)
        self.dv_con_label.setObjectName(u"dv_con_label")
        self.dv_con_label.setGeometry(QRect(20, 60, 141, 21))
        self.dntp_con_label = QLabel(self.primer3_param_groupBox)
        self.dntp_con_label.setObjectName(u"dntp_con_label")
        self.dntp_con_label.setGeometry(QRect(20, 90, 141, 21))
        self.dna_con_label = QLabel(self.primer3_param_groupBox)
        self.dna_con_label.setObjectName(u"dna_con_label")
        self.dna_con_label.setGeometry(QRect(20, 120, 141, 21))
        self.mono_salt_doubleSpinBox = QDoubleSpinBox(self.primer3_param_groupBox)
        self.mono_salt_doubleSpinBox.setObjectName(u"mono_salt_doubleSpinBox")
        self.mono_salt_doubleSpinBox.setGeometry(QRect(240, 30, 62, 22))
        self.mono_salt_doubleSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.mono_salt_doubleSpinBox.setSingleStep(0.010000000000000)
        self.mono_salt_doubleSpinBox.setValue(50.000000000000000)
        self.div_salt_doubleSpinBox = QDoubleSpinBox(self.primer3_param_groupBox)
        self.div_salt_doubleSpinBox.setObjectName(u"div_salt_doubleSpinBox")
        self.div_salt_doubleSpinBox.setGeometry(QRect(240, 60, 62, 22))
        self.div_salt_doubleSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.div_salt_doubleSpinBox.setSingleStep(0.010000000000000)
        self.div_salt_doubleSpinBox.setValue(4.000000000000000)
        self.dntp_con_doubleSpinBox = QDoubleSpinBox(self.primer3_param_groupBox)
        self.dntp_con_doubleSpinBox.setObjectName(u"dntp_con_doubleSpinBox")
        self.dntp_con_doubleSpinBox.setGeometry(QRect(240, 90, 62, 22))
        self.dntp_con_doubleSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dntp_con_doubleSpinBox.setSingleStep(0.010000000000000)
        self.dntp_con_doubleSpinBox.setValue(0.500000000000000)
        self.dna_con_doubleSpinBox = QDoubleSpinBox(self.primer3_param_groupBox)
        self.dna_con_doubleSpinBox.setObjectName(u"dna_con_doubleSpinBox")
        self.dna_con_doubleSpinBox.setGeometry(QRect(240, 120, 62, 22))
        self.dna_con_doubleSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dna_con_doubleSpinBox.setSingleStep(0.010000000000000)
        self.dna_con_doubleSpinBox.setValue(50.000000000000000)
        self.file_out_pushButton = QPushButton(self.formater_page)
        self.file_out_pushButton.setObjectName(u"file_out_pushButton")
        self.file_out_pushButton.setGeometry(QRect(12, 40, 113, 31))
        self.load_csv_pushButton = QPushButton(self.formater_page)
        self.load_csv_pushButton.setObjectName(u"load_csv_pushButton")
        self.load_csv_pushButton.setGeometry(QRect(60, 390, 121, 32))
        self.groupBox = QGroupBox(self.formater_page)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(160, 295, 191, 46))
        self.primer3_out_file_name_label = QLabel(self.groupBox)
        self.primer3_out_file_name_label.setObjectName(u"primer3_out_file_name_label")
        self.primer3_out_file_name_label.setGeometry(QRect(5, 20, 171, 21))
        self.primer3_out_file_name_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.toolBox.addItem(self.formater_page, u"Formater")
        self.selector_page = QWidget()
        self.selector_page.setObjectName(u"selector_page")
        self.selector_page.setGeometry(QRect(0, 0, 373, 467))
        self.toolBox.addItem(self.selector_page, u"Selector")
        self.composer_page = QWidget()
        self.composer_page.setObjectName(u"composer_page")
        self.composer_page.setGeometry(QRect(0, 0, 373, 467))
        self.toolBox.addItem(self.composer_page, u"Composer")
        Bits.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Bits)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 422, 22))
        Bits.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Bits)
        self.statusbar.setObjectName(u"statusbar")
        Bits.setStatusBar(self.statusbar)

        self.retranslateUi(Bits)

        self.toolBox.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Bits)
    # setupUi

    def retranslateUi(self, Bits):
        Bits.setWindowTitle(QCoreApplication.translate("Bits", u"Bits", None))
        self.title_label.setText(QCoreApplication.translate("Bits", u"DNA Bits", None))
        self.author_label.setText(QCoreApplication.translate("Bits", u"Marek Mi\u015bkiewicz", None))
        self.ver_label.setText(QCoreApplication.translate("Bits", u"ver. 0.0.1", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.title_page), QCoreApplication.translate("Bits", u"Title", None))
        self.primers_groupBox.setTitle(QCoreApplication.translate("Bits", u"Primers", None))
        self.primers_length_2.setText(QCoreApplication.translate("Bits", u"Length:", None))
        self.numbers_of_primers.setText(QCoreApplication.translate("Bits", u"Number of Primers:", None))
        self.generator_out_file_pushButton.setText(QCoreApplication.translate("Bits", u"Output file", None))
        self.temp_groupBox.setTitle(QCoreApplication.translate("Bits", u"Temperature", None))
        self.min_temp.setText(QCoreApplication.translate("Bits", u"Minimal", None))
        self.max_temp.setText(QCoreApplication.translate("Bits", u"Maximal", None))
        self.gccontent_groupBox.setTitle(QCoreApplication.translate("Bits", u"GC Content", None))
        self.gc_min.setText(QCoreApplication.translate("Bits", u"Minimal", None))
        self.gc_max.setText(QCoreApplication.translate("Bits", u"Maximal", None))
        self.parameters_groupBox.setTitle(QCoreApplication.translate("Bits", u"Parameters", None))
        self.runs_checkBox.setText(QCoreApplication.translate("Bits", u"Runs", None))
        self.repeats_checkBox.setText(QCoreApplication.translate("Bits", u"Repeats", None))
        self.start_pushButton.setText(QCoreApplication.translate("Bits", u"Start", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.genrator_page), QCoreApplication.translate("Bits", u"Generator", None))
        self.csv_preview_pushButton.setText(QCoreApplication.translate("Bits", u"CSV preview", None))
        self.generate_csv_pushButton.setText(QCoreApplication.translate("Bits", u"Generate CSV file", None))
        self.file_in_label.setText(QCoreApplication.translate("Bits", u"input file name", None))
        self.run_pr3_pushButton.setText(QCoreApplication.translate("Bits", u"Run Primer3", None))
        self.sequence_id_label.setText(QCoreApplication.translate("Bits", u"Sequence ID:", None))
        self.file_in_pushButton.setText(QCoreApplication.translate("Bits", u"Input file", None))
        self.generate_pushButton.setText(QCoreApplication.translate("Bits", u"Generate Primer3 input", None))
        self.primer3_param_groupBox.setTitle(QCoreApplication.translate("Bits", u"Primer3 parameters:", None))
        self.mv_con_label.setText(QCoreApplication.translate("Bits", u"Monovalent salt", None))
        self.dv_con_label.setText(QCoreApplication.translate("Bits", u"Divalent salt", None))
        self.dntp_con_label.setText(QCoreApplication.translate("Bits", u"DNTP concentration", None))
        self.dna_con_label.setText(QCoreApplication.translate("Bits", u"DNA concentration", None))
        self.file_out_pushButton.setText(QCoreApplication.translate("Bits", u"Output file", None))
        self.load_csv_pushButton.setText(QCoreApplication.translate("Bits", u"Load CSV", None))
        self.groupBox.setTitle(QCoreApplication.translate("Bits", u"Primer3 output file:", None))
        self.primer3_out_file_name_label.setText(QCoreApplication.translate("Bits", u"output file", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.formater_page), QCoreApplication.translate("Bits", u"Formater", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.selector_page), QCoreApplication.translate("Bits", u"Selector", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.composer_page), QCoreApplication.translate("Bits", u"Composer", None))
    # retranslateUi
