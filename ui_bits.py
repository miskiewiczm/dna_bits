# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
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
        self.title_page.setGeometry(QRect(0, 0, 373, 497))
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
        self.genrator_page.setGeometry(QRect(0, 0, 373, 497))
        self.temp_groupBox = QGroupBox(self.genrator_page)
        self.temp_groupBox.setObjectName(u"temp_groupBox")
        self.temp_groupBox.setGeometry(QRect(20, 180, 330, 90))
        self.temp_groupBox.setCheckable(True)
        self.min_temp = QLabel(self.temp_groupBox)
        self.min_temp.setObjectName(u"min_temp")
        self.min_temp.setGeometry(QRect(20, 30, 59, 21))
        self.max_temp = QLabel(self.temp_groupBox)
        self.max_temp.setObjectName(u"max_temp")
        self.max_temp.setGeometry(QRect(20, 60, 59, 21))
        self.tmmin_doubleSpinBox = QDoubleSpinBox(self.temp_groupBox)
        self.tmmin_doubleSpinBox.setObjectName(u"tmmin_doubleSpinBox")
        self.tmmin_doubleSpinBox.setGeometry(QRect(250, 30, 61, 22))
        self.tmmin_doubleSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.tmmin_doubleSpinBox.setSingleStep(0.050000000000000)
        self.tmmin_doubleSpinBox.setValue(58.000000000000000)
        self.tmmax_doubleSpinBox = QDoubleSpinBox(self.temp_groupBox)
        self.tmmax_doubleSpinBox.setObjectName(u"tmmax_doubleSpinBox")
        self.tmmax_doubleSpinBox.setGeometry(QRect(250, 60, 61, 22))
        self.tmmax_doubleSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.tmmax_doubleSpinBox.setSingleStep(0.050000000000000)
        self.tmmax_doubleSpinBox.setValue(62.000000000000000)
        self.gccontent_groupBox = QGroupBox(self.genrator_page)
        self.gccontent_groupBox.setObjectName(u"gccontent_groupBox")
        self.gccontent_groupBox.setGeometry(QRect(20, 280, 330, 90))
        self.gccontent_groupBox.setCheckable(True)
        self.gc_min = QLabel(self.gccontent_groupBox)
        self.gc_min.setObjectName(u"gc_min")
        self.gc_min.setGeometry(QRect(20, 30, 59, 21))
        self.gc_max = QLabel(self.gccontent_groupBox)
        self.gc_max.setObjectName(u"gc_max")
        self.gc_max.setGeometry(QRect(20, 60, 59, 21))
        self.gcmin_doubleSpinBox = QDoubleSpinBox(self.gccontent_groupBox)
        self.gcmin_doubleSpinBox.setObjectName(u"gcmin_doubleSpinBox")
        self.gcmin_doubleSpinBox.setGeometry(QRect(250, 30, 61, 22))
        self.gcmin_doubleSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gcmin_doubleSpinBox.setMaximum(1.000000000000000)
        self.gcmin_doubleSpinBox.setSingleStep(0.010000000000000)
        self.gcmin_doubleSpinBox.setValue(0.480000000000000)
        self.gcmax_doubleSpinBox = QDoubleSpinBox(self.gccontent_groupBox)
        self.gcmax_doubleSpinBox.setObjectName(u"gcmax_doubleSpinBox")
        self.gcmax_doubleSpinBox.setGeometry(QRect(250, 60, 61, 22))
        self.gcmax_doubleSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gcmax_doubleSpinBox.setMaximum(1.000000000000000)
        self.gcmax_doubleSpinBox.setSingleStep(0.010000000000000)
        self.gcmax_doubleSpinBox.setValue(0.520000000000000)
        self.parameters_groupBox = QGroupBox(self.genrator_page)
        self.parameters_groupBox.setObjectName(u"parameters_groupBox")
        self.parameters_groupBox.setGeometry(QRect(20, 380, 331, 61))
        self.runs_checkBox = QCheckBox(self.parameters_groupBox)
        self.runs_checkBox.setObjectName(u"runs_checkBox")
        self.runs_checkBox.setGeometry(QRect(20, 30, 61, 20))
        self.runs_checkBox.setChecked(True)
        self.repeats_checkBox = QCheckBox(self.parameters_groupBox)
        self.repeats_checkBox.setObjectName(u"repeats_checkBox")
        self.repeats_checkBox.setGeometry(QRect(90, 30, 86, 20))
        self.repeats_checkBox.setChecked(True)
        self.primers_groupBox = QGroupBox(self.genrator_page)
        self.primers_groupBox.setObjectName(u"primers_groupBox")
        self.primers_groupBox.setGeometry(QRect(20, 80, 330, 90))
        self.primers_length_2 = QLabel(self.primers_groupBox)
        self.primers_length_2.setObjectName(u"primers_length_2")
        self.primers_length_2.setGeometry(QRect(20, 30, 59, 21))
        self.numbers_of_primers = QLabel(self.primers_groupBox)
        self.numbers_of_primers.setObjectName(u"numbers_of_primers")
        self.numbers_of_primers.setGeometry(QRect(20, 60, 126, 21))
        self.primers_length_spinBox = QSpinBox(self.primers_groupBox)
        self.primers_length_spinBox.setObjectName(u"primers_length_spinBox")
        self.primers_length_spinBox.setGeometry(QRect(250, 30, 61, 22))
        self.primers_length_spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.primers_length_spinBox.setValue(20)
        self.number_of_primers_spinBox = QSpinBox(self.primers_groupBox)
        self.number_of_primers_spinBox.setObjectName(u"number_of_primers_spinBox")
        self.number_of_primers_spinBox.setGeometry(QRect(250, 60, 61, 22))
        self.number_of_primers_spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.number_of_primers_spinBox.setMaximum(1000000000)
        self.number_of_primers_spinBox.setSingleStep(200)
        self.number_of_primers_spinBox.setValue(1000)
        self.formLayoutWidget_3 = QWidget(self.genrator_page)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(20, 10, 331, 62))
        self.formLayout = QFormLayout(self.formLayoutWidget_3)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.generator_output_button = QPushButton(self.formLayoutWidget_3)
        self.generator_output_button.setObjectName(u"generator_output_button")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.generator_output_button)

        self.generator_output_edit = QLineEdit(self.formLayoutWidget_3)
        self.generator_output_edit.setObjectName(u"generator_output_edit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.generator_output_edit)

        self.gen_input_button = QPushButton(self.formLayoutWidget_3)
        self.gen_input_button.setObjectName(u"gen_input_button")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.gen_input_button)

        self.gen_input_edit = QLineEdit(self.formLayoutWidget_3)
        self.gen_input_edit.setObjectName(u"gen_input_edit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.gen_input_edit)

        self.formLayoutWidget_4 = QWidget(self.genrator_page)
        self.formLayoutWidget_4.setObjectName(u"formLayoutWidget_4")
        self.formLayoutWidget_4.setGeometry(QRect(20, 450, 331, 31))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_4)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.generator_start_button = QPushButton(self.formLayoutWidget_4)
        self.generator_start_button.setObjectName(u"generator_start_button")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.generator_start_button)

        self.generate_progress_bar = QProgressBar(self.formLayoutWidget_4)
        self.generate_progress_bar.setObjectName(u"generate_progress_bar")
        self.generate_progress_bar.setValue(0)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.generate_progress_bar)

        self.toolBox.addItem(self.genrator_page, u"Generator")
        self.formater_page = QWidget()
        self.formater_page.setObjectName(u"formater_page")
        self.formater_page.setGeometry(QRect(0, 0, 373, 497))
        self.primer3_param_groupBox = QGroupBox(self.formater_page)
        self.primer3_param_groupBox.setObjectName(u"primer3_param_groupBox")
        self.primer3_param_groupBox.setGeometry(QRect(20, 110, 330, 150))
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
        self.formLayoutWidget_5 = QWidget(self.formater_page)
        self.formLayoutWidget_5.setObjectName(u"formLayoutWidget_5")
        self.formLayoutWidget_5.setGeometry(QRect(20, 10, 331, 94))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_5)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formatter_input_button = QPushButton(self.formLayoutWidget_5)
        self.formatter_input_button.setObjectName(u"formatter_input_button")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.formatter_input_button)

        self.formatter_output_button = QPushButton(self.formLayoutWidget_5)
        self.formatter_output_button.setObjectName(u"formatter_output_button")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.formatter_output_button)

        self.formatter_output_edit = QLineEdit(self.formLayoutWidget_5)
        self.formatter_output_edit.setObjectName(u"formatter_output_edit")
        self.formatter_output_edit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.formatter_output_edit)

        self.sequence_id_label = QLabel(self.formLayoutWidget_5)
        self.sequence_id_label.setObjectName(u"sequence_id_label")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.sequence_id_label)

        self.sequence_id_lineEdit = QLineEdit(self.formLayoutWidget_5)
        self.sequence_id_lineEdit.setObjectName(u"sequence_id_lineEdit")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.sequence_id_lineEdit)

        self.formatter_input_edit = QLineEdit(self.formLayoutWidget_5)
        self.formatter_input_edit.setObjectName(u"formatter_input_edit")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.formatter_input_edit)

        self.formLayoutWidget_6 = QWidget(self.formater_page)
        self.formLayoutWidget_6.setObjectName(u"formLayoutWidget_6")
        self.formLayoutWidget_6.setGeometry(QRect(20, 270, 331, 95))
        self.formLayout_4 = QFormLayout(self.formLayoutWidget_6)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.generate_pushButton = QPushButton(self.formLayoutWidget_6)
        self.generate_pushButton.setObjectName(u"generate_pushButton")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.generate_pushButton)

        self.generate_progressBar = QProgressBar(self.formLayoutWidget_6)
        self.generate_progressBar.setObjectName(u"generate_progressBar")
        self.generate_progressBar.setValue(0)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.generate_progressBar)

        self.run_pr3_pushButton = QPushButton(self.formLayoutWidget_6)
        self.run_pr3_pushButton.setObjectName(u"run_pr3_pushButton")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.run_pr3_pushButton)

        self.generate_csv_pushButton = QPushButton(self.formLayoutWidget_6)
        self.generate_csv_pushButton.setObjectName(u"generate_csv_pushButton")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.generate_csv_pushButton)

        self.generate_csv_progressBar = QProgressBar(self.formLayoutWidget_6)
        self.generate_csv_progressBar.setObjectName(u"generate_csv_progressBar")
        self.generate_csv_progressBar.setValue(0)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.generate_csv_progressBar)

        self.lineEdit = QLineEdit(self.formLayoutWidget_6)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setReadOnly(True)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.lineEdit)

        self.toolBox.addItem(self.formater_page, u"Formatter")
        self.selector_page = QWidget()
        self.selector_page.setObjectName(u"selector_page")
        self.selector_page.setGeometry(QRect(0, 0, 373, 497))
        self.formLayoutWidget_2 = QWidget(self.selector_page)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(0, 10, 361, 451))
        self.selector_form_layout = QFormLayout(self.formLayoutWidget_2)
        self.selector_form_layout.setObjectName(u"selector_form_layout")
        self.selector_form_layout.setVerticalSpacing(10)
        self.selector_form_layout.setContentsMargins(0, 0, 0, 0)
        self.selector_input_button = QPushButton(self.formLayoutWidget_2)
        self.selector_input_button.setObjectName(u"selector_input_button")

        self.selector_form_layout.setWidget(0, QFormLayout.LabelRole, self.selector_input_button)

        self.selector_input_edit = QLineEdit(self.formLayoutWidget_2)
        self.selector_input_edit.setObjectName(u"selector_input_edit")

        self.selector_form_layout.setWidget(0, QFormLayout.FieldRole, self.selector_input_edit)

        self.selector_sorter_table = QTableWidget(self.formLayoutWidget_2)
        if (self.selector_sorter_table.columnCount() < 3):
            self.selector_sorter_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.selector_sorter_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.selector_sorter_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.selector_sorter_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.selector_sorter_table.setObjectName(u"selector_sorter_table")
        self.selector_sorter_table.setMinimumSize(QSize(0, 175))
        self.selector_sorter_table.setRowCount(0)
        self.selector_sorter_table.setColumnCount(3)
        self.selector_sorter_table.horizontalHeader().setStretchLastSection(True)

        self.selector_form_layout.setWidget(1, QFormLayout.SpanningRole, self.selector_sorter_table)

        self.selector_info_label = QLabel(self.formLayoutWidget_2)
        self.selector_info_label.setObjectName(u"selector_info_label")
        self.selector_info_label.setAlignment(Qt.AlignCenter)
        self.selector_info_label.setWordWrap(True)

        self.selector_form_layout.setWidget(2, QFormLayout.SpanningRole, self.selector_info_label)

        self.selector_preview_button = QPushButton(self.formLayoutWidget_2)
        self.selector_preview_button.setObjectName(u"selector_preview_button")
        self.selector_preview_button.setEnabled(False)

        self.selector_form_layout.setWidget(3, QFormLayout.SpanningRole, self.selector_preview_button)

        self.selector_chosen_primer_list = QListWidget(self.formLayoutWidget_2)
        self.selector_chosen_primer_list.setObjectName(u"selector_chosen_primer_list")
        font2 = QFont()
        font2.setFamily(u"Monospace")
        font2.setPointSize(12)
        self.selector_chosen_primer_list.setFont(font2)

        self.selector_form_layout.setWidget(4, QFormLayout.FieldRole, self.selector_chosen_primer_list)

        self.selector_chosen_primer_label = QLabel(self.formLayoutWidget_2)
        self.selector_chosen_primer_label.setObjectName(u"selector_chosen_primer_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.selector_chosen_primer_label.sizePolicy().hasHeightForWidth())
        self.selector_chosen_primer_label.setSizePolicy(sizePolicy1)
        self.selector_chosen_primer_label.setAlignment(Qt.AlignCenter)

        self.selector_form_layout.setWidget(4, QFormLayout.LabelRole, self.selector_chosen_primer_label)

        self.toolBox.addItem(self.selector_page, u"Selector")
        self.composer_page = QWidget()
        self.composer_page.setObjectName(u"composer_page")
        self.composer_page.setGeometry(QRect(0, 0, 373, 497))
        self.formLayoutWidget = QWidget(self.composer_page)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 20, 351, 466))
        self.composer_form_layout = QFormLayout(self.formLayoutWidget)
        self.composer_form_layout.setObjectName(u"composer_form_layout")
        self.composer_form_layout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.composer_form_layout.setVerticalSpacing(10)
        self.composer_form_layout.setContentsMargins(0, 0, 0, 0)
        self.composer_input_button = QPushButton(self.formLayoutWidget)
        self.composer_input_button.setObjectName(u"composer_input_button")

        self.composer_form_layout.setWidget(0, QFormLayout.LabelRole, self.composer_input_button)

        self.composer_input_edit = QLineEdit(self.formLayoutWidget)
        self.composer_input_edit.setObjectName(u"composer_input_edit")

        self.composer_form_layout.setWidget(0, QFormLayout.FieldRole, self.composer_input_edit)

        self.composer_bits_label = QLabel(self.formLayoutWidget)
        self.composer_bits_label.setObjectName(u"composer_bits_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.composer_bits_label.sizePolicy().hasHeightForWidth())
        self.composer_bits_label.setSizePolicy(sizePolicy2)

        self.composer_form_layout.setWidget(1, QFormLayout.LabelRole, self.composer_bits_label)

        self.composer_bits_content = QPlainTextEdit(self.formLayoutWidget)
        self.composer_bits_content.setObjectName(u"composer_bits_content")

        self.composer_form_layout.setWidget(1, QFormLayout.FieldRole, self.composer_bits_content)

        self.composer_search_button = QPushButton(self.formLayoutWidget)
        self.composer_search_button.setObjectName(u"composer_search_button")

        self.composer_form_layout.setWidget(2, QFormLayout.SpanningRole, self.composer_search_button)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.composer_save_button = QPushButton(self.formLayoutWidget)
        self.composer_save_button.setObjectName(u"composer_save_button")

        self.horizontalLayout.addWidget(self.composer_save_button)

        self.composer_select_button = QPushButton(self.formLayoutWidget)
        self.composer_select_button.setObjectName(u"composer_select_button")

        self.horizontalLayout.addWidget(self.composer_select_button)


        self.composer_form_layout.setLayout(3, QFormLayout.SpanningRole, self.horizontalLayout)

        self.composer_output_button = QPushButton(self.formLayoutWidget)
        self.composer_output_button.setObjectName(u"composer_output_button")

        self.composer_form_layout.setWidget(4, QFormLayout.LabelRole, self.composer_output_button)

        self.composer_output_edit = QLineEdit(self.formLayoutWidget)
        self.composer_output_edit.setObjectName(u"composer_output_edit")

        self.composer_form_layout.setWidget(4, QFormLayout.FieldRole, self.composer_output_edit)

        self.title_down_line_2 = QFrame(self.formLayoutWidget)
        self.title_down_line_2.setObjectName(u"title_down_line_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.title_down_line_2.sizePolicy().hasHeightForWidth())
        self.title_down_line_2.setSizePolicy(sizePolicy3)
        self.title_down_line_2.setMinimumSize(QSize(36, 19))
        self.title_down_line_2.setFrameShape(QFrame.HLine)
        self.title_down_line_2.setFrameShadow(QFrame.Sunken)

        self.composer_form_layout.setWidget(5, QFormLayout.SpanningRole, self.title_down_line_2)

        self.composer_manual_s_label = QLabel(self.formLayoutWidget)
        self.composer_manual_s_label.setObjectName(u"composer_manual_s_label")

        self.composer_form_layout.setWidget(6, QFormLayout.LabelRole, self.composer_manual_s_label)

        self.composer_manual_s_combo = QComboBox(self.formLayoutWidget)
        self.composer_manual_s_combo.setObjectName(u"composer_manual_s_combo")
        self.composer_manual_s_combo.setEnabled(False)

        self.composer_form_layout.setWidget(6, QFormLayout.FieldRole, self.composer_manual_s_combo)

        self.composer_manual_e_label = QLabel(self.formLayoutWidget)
        self.composer_manual_e_label.setObjectName(u"composer_manual_e_label")

        self.composer_form_layout.setWidget(7, QFormLayout.LabelRole, self.composer_manual_e_label)

        self.composer_manual_e_combo = QComboBox(self.formLayoutWidget)
        self.composer_manual_e_combo.setObjectName(u"composer_manual_e_combo")
        self.composer_manual_e_combo.setEnabled(False)

        self.composer_form_layout.setWidget(7, QFormLayout.FieldRole, self.composer_manual_e_combo)

        self.composer_manual_0_label = QLabel(self.formLayoutWidget)
        self.composer_manual_0_label.setObjectName(u"composer_manual_0_label")

        self.composer_form_layout.setWidget(8, QFormLayout.LabelRole, self.composer_manual_0_label)

        self.composer_manual_0_combo = QComboBox(self.formLayoutWidget)
        self.composer_manual_0_combo.setObjectName(u"composer_manual_0_combo")
        self.composer_manual_0_combo.setEnabled(False)

        self.composer_form_layout.setWidget(8, QFormLayout.FieldRole, self.composer_manual_0_combo)

        self.composer_manual_1_label = QLabel(self.formLayoutWidget)
        self.composer_manual_1_label.setObjectName(u"composer_manual_1_label")

        self.composer_form_layout.setWidget(9, QFormLayout.LabelRole, self.composer_manual_1_label)

        self.composer_manual_1_combo = QComboBox(self.formLayoutWidget)
        self.composer_manual_1_combo.setObjectName(u"composer_manual_1_combo")
        self.composer_manual_1_combo.setEnabled(False)

        self.composer_form_layout.setWidget(9, QFormLayout.FieldRole, self.composer_manual_1_combo)

        self.composer_run_button = QPushButton(self.formLayoutWidget)
        self.composer_run_button.setObjectName(u"composer_run_button")

        self.composer_form_layout.setWidget(11, QFormLayout.SpanningRole, self.composer_run_button)

        self.composer_output2_button = QPushButton(self.formLayoutWidget)
        self.composer_output2_button.setObjectName(u"composer_output2_button")

        self.composer_form_layout.setWidget(10, QFormLayout.LabelRole, self.composer_output2_button)

        self.composer_output2_edit = QLineEdit(self.formLayoutWidget)
        self.composer_output2_edit.setObjectName(u"composer_output2_edit")

        self.composer_form_layout.setWidget(10, QFormLayout.FieldRole, self.composer_output2_edit)

        self.toolBox.addItem(self.composer_page, u"Composer")
        Bits.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Bits)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 422, 19))
        Bits.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Bits)
        self.statusbar.setObjectName(u"statusbar")
        Bits.setStatusBar(self.statusbar)

        self.retranslateUi(Bits)

        self.toolBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Bits)
    # setupUi

    def retranslateUi(self, Bits):
        Bits.setWindowTitle(QCoreApplication.translate("Bits", u"Bits", None))
        self.title_label.setText(QCoreApplication.translate("Bits", u"DNA Bits", None))
        self.author_label.setText(QCoreApplication.translate("Bits", u"Marek Mi\u015bkiewicz", None))
        self.ver_label.setText(QCoreApplication.translate("Bits", u"ver. 0.0.1", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.title_page), QCoreApplication.translate("Bits", u"Title", None))
        self.temp_groupBox.setTitle(QCoreApplication.translate("Bits", u"Temperature", None))
        self.min_temp.setText(QCoreApplication.translate("Bits", u"Minimal:", None))
        self.max_temp.setText(QCoreApplication.translate("Bits", u"Maximal:", None))
        self.gccontent_groupBox.setTitle(QCoreApplication.translate("Bits", u"GC Content", None))
        self.gc_min.setText(QCoreApplication.translate("Bits", u"Minimal:", None))
        self.gc_max.setText(QCoreApplication.translate("Bits", u"Maximal:", None))
        self.parameters_groupBox.setTitle(QCoreApplication.translate("Bits", u"Parameters", None))
        self.runs_checkBox.setText(QCoreApplication.translate("Bits", u"Runs", None))
        self.repeats_checkBox.setText(QCoreApplication.translate("Bits", u"Repeats", None))
        self.primers_groupBox.setTitle(QCoreApplication.translate("Bits", u"Primers", None))
        self.primers_length_2.setText(QCoreApplication.translate("Bits", u"Length:", None))
        self.numbers_of_primers.setText(QCoreApplication.translate("Bits", u"Number of Primers:", None))
        self.generator_output_button.setText(QCoreApplication.translate("Bits", u"Output file", None))
        self.gen_input_button.setText(QCoreApplication.translate("Bits", u"Input file", None))
#if QT_CONFIG(tooltip)
        self.gen_input_edit.setToolTip(QCoreApplication.translate("Bits", u"If any file is chosen, primers will not be generated.", None))
#endif // QT_CONFIG(tooltip)
        self.gen_input_edit.setPlaceholderText(QCoreApplication.translate("Bits", u"Alternative primers source file...", None))
        self.generator_start_button.setText(QCoreApplication.translate("Bits", u"Start", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.genrator_page), QCoreApplication.translate("Bits", u"Generator", None))
        self.primer3_param_groupBox.setTitle(QCoreApplication.translate("Bits", u"Primer3 parameters:", None))
        self.mv_con_label.setText(QCoreApplication.translate("Bits", u"Monovalent salt", None))
        self.dv_con_label.setText(QCoreApplication.translate("Bits", u"Divalent salt", None))
        self.dntp_con_label.setText(QCoreApplication.translate("Bits", u"DNTP concentration", None))
        self.dna_con_label.setText(QCoreApplication.translate("Bits", u"DNA concentration", None))
        self.formatter_input_button.setText(QCoreApplication.translate("Bits", u"Input file", None))
        self.formatter_output_button.setText(QCoreApplication.translate("Bits", u"Output file", None))
        self.sequence_id_label.setText(QCoreApplication.translate("Bits", u"Sequence ID:", None))
        self.generate_pushButton.setText(QCoreApplication.translate("Bits", u"Generate Primer3 input", None))
        self.run_pr3_pushButton.setText(QCoreApplication.translate("Bits", u"Run Primer3", None))
        self.generate_csv_pushButton.setText(QCoreApplication.translate("Bits", u"Generate CSV file", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Bits", u"Output file...", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.formater_page), QCoreApplication.translate("Bits", u"Formatter", None))
        self.selector_input_button.setText(QCoreApplication.translate("Bits", u"Input file", None))
        ___qtablewidgetitem = self.selector_sorter_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Bits", u"Include", None));
        ___qtablewidgetitem1 = self.selector_sorter_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Bits", u"Priority", None));
        ___qtablewidgetitem2 = self.selector_sorter_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Bits", u"Order", None));
        self.selector_info_label.setText(QCoreApplication.translate("Bits", u"Select primers and close the preview window", None))
        self.selector_preview_button.setText(QCoreApplication.translate("Bits", u"Preview", None))
        self.selector_chosen_primer_label.setText(QCoreApplication.translate("Bits", u"Chosen primers:", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.selector_page), QCoreApplication.translate("Bits", u"Selector", None))
        self.composer_input_button.setText(QCoreApplication.translate("Bits", u"Input file", None))
        self.composer_bits_label.setText(QCoreApplication.translate("Bits", u"Bits:", None))
        self.composer_bits_content.setPlaceholderText(QCoreApplication.translate("Bits", u"01011011", None))
        self.composer_search_button.setText(QCoreApplication.translate("Bits", u"Search", None))
        self.composer_save_button.setText(QCoreApplication.translate("Bits", u"Save", None))
        self.composer_select_button.setText(QCoreApplication.translate("Bits", u"Select", None))
        self.composer_output_button.setText(QCoreApplication.translate("Bits", u"Output file", None))
        self.composer_manual_s_label.setText(QCoreApplication.translate("Bits", u"S:", None))
        self.composer_manual_e_label.setText(QCoreApplication.translate("Bits", u"E:", None))
        self.composer_manual_0_label.setText(QCoreApplication.translate("Bits", u"Bit \"0\":", None))
        self.composer_manual_1_label.setText(QCoreApplication.translate("Bits", u"Bit \"1\":", None))
        self.composer_run_button.setText(QCoreApplication.translate("Bits", u"Compose", None))
        self.composer_output2_button.setText(QCoreApplication.translate("Bits", u"Output file", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.composer_page), QCoreApplication.translate("Bits", u"Composer", None))
    # retranslateUi

