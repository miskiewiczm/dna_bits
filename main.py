#!/usr/local/bin/python3
#
import os
import random
import sys
from typing import Dict, Callable, List, Union

import primer3
from PySide2.QtCore import QProcess, QSize
from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog, QTableWidgetItem
from PySide2.QtWidgets import QWidget

from table_items_widgets import ComboOrderWidget, SpinBoxWidget, CheckBoxWidget
from ui_bits import Ui_Bits
from ui_csv_viewer import Ui_CSV_Viewer

# Generator variables
# Global variables for primers
number_of_primers = 1000  # number of primers
length_of_primer = 20  # length of primer

gen_file_name = ""  # where to store generated primers
path = os.getcwd()  # ...
tm_trigger = True
tm_min = 58.0
tm_max = 62.0
gc_trigger = True
gc_min = 0.47
gc_max = 0.53
runs_trigger = True
rpts_trigger = True

# ## Formater variables
primer_input_file_name = ""
primer_output_file_name = ""
end = "\n"
seq_id = "sample_30.03.2020"
task = "check_primers"
psm = 50.0
psd = 4.0
pdc = 0.5
pnc = 50.0

number_of_lines = 0


class FileSelectHelper:
    data: Dict = {}

    def __init__(self, bits: "Bits"):
        self.bits = bits

    def select_file(self, name: str) -> None:
        d = self.data[name]

        d['text'], _ = QFileDialog.getOpenFileName(
            self.bits,
            "Generator Load File", "",
            ";;".join([f"{t} files (*.{t})" for t in d['types']]) + ";;All Files (*)"
        )

        d['label'].setText(d['text'])
        if d['f']:
            d['f']()

    def add_file_handler(self, name: str, button, label, types: Union[str, List[str]] = None, f: Callable = None):
        if isinstance(types, str):
            types = [types]

        self.data[name] = {'label': label, 'text': "", 'f': f, 'types': types or []}
        button.clicked.connect(lambda: self.select_file(name))

    def __getitem__(self, item):
        return self.data[item]['text']


class CSV_Viewer(QWidget, Ui_CSV_Viewer):
    def __init__(self):
        super(CSV_Viewer, self).__init__()
        self.setupUi(self)


class Bits(QMainWindow, Ui_Bits):
    def __init__(self):
        super(Bits, self).__init__()
        self.setupUi(self)
        self.setFixedSize(QSize(422, 715))

        self.primers_length_spinBox.valueChanged.connect(self.primers_length)
        self.number_of_primers_spinBox.valueChanged.connect(
            self.numbers__primers)

        self.temp_groupBox.toggled.connect(self.temp_set)
        self.tmmin_doubleSpinBox.valueChanged.connect(self.value_change_tmmi)
        self.tmmax_doubleSpinBox.valueChanged.connect(self.value_change_tmma)

        self.gccontent_groupBox.toggled.connect(self.gc_content_set)
        self.gcmin_doubleSpinBox.valueChanged.connect(self.value_change_gcmi)
        self.gcmax_doubleSpinBox.valueChanged.connect(self.value_change_gcma)

        self.runs_checkBox.stateChanged.connect(self.runs_set)
        self.repeats_checkBox.stateChanged.connect(self.repeats_set)

        self.generator_start_button.clicked.connect(self.start_generate)

        self.sequence_id_lineEdit.textChanged.connect(self.sequenceID_edit)
        self.generate_pushButton.clicked.connect(self.primer3_input_generator)
        self.run_pr3_pushButton.clicked.connect(primer3_run)
        self.generate_csv_pushButton.clicked.connect(csv_generator)

        self.prepare_selector_sorter_table()
        self.selector_preview_button.clicked.connect(self.csv_preview)

        # file selectors
        self.fsh = FileSelectHelper(self)
        self.fsh.add_file_handler("generator_output", self.generator_output_button, self.generator_output_edit, 'txt')
        self.fsh.add_file_handler("formatter_input", self.formatter_input_button, self.formatter_input_edit)
        self.fsh.add_file_handler("formatter_output", self.formatter_output_button, self.formatter_output_edit)
        self.fsh.add_file_handler("selector_input", self.selector_input_button, self.selector_input_edit, 'csv')
        self.fsh.add_file_handler("composer_output", self.composer_output_button, self.composer_output_edit)

    def gen_file_name_changed(self):
        global gen_file_name
        gen_file_name = str(self.generator_out_file_lineEdit.text())

    def gen_file_name_choose(self):
        global gen_file_name
        global primer_input_file_name
        gen_file_name, _ = QFileDialog.getOpenFileName(
            self, "Generator Load File", "",
            "All Files (*);; Text filex (*.txt)")
        self.generator_out_file_lineEdit.setText(gen_file_name.split('/')[-1])
        primer_input_file_name = gen_file_name
        self.file_in_label.setText(primer_input_file_name)

    def primers_length(self):
        global length_of_primer
        length_of_primer = self.primers_length_spinBox.value()

    def numbers__primers(self):
        global number_of_primers
        number_of_primers = self.number_of_primers_spinBox.value()

    @staticmethod
    def runs_set():
        global runs_trigger
        runs_trigger = not runs_trigger

    @staticmethod
    def repeats_set():
        global rpts_trigger
        rpts_trigger = not rpts_trigger

    def gc_content_set(self):
        global gc_trigger
        gc_trigger = self.gccontent_groupBox.isChecked()

    def temp_set(self):
        global tm_trigger
        tm_trigger = self.temp_groupBox.isChecked()

    def value_change_tmmi(self):
        global tm_min
        tm_min = self.tmmin_doubleSpinBox.value()

    def value_change_tmma(self):
        global tm_max
        tm_max = self.tmmax_doubleSpinBox.value()

    def value_change_gcmi(self):
        global gc_min
        gc_min = self.gcmin_doubleSpinBox.value()

    def value_change_gcma(self):
        global gc_max
        gc_max = self.gcmax_doubleSpinBox.value()

    @staticmethod
    def start_generate():
        window.generate_progressBar.reset()
        randomizer()

    # --- formatter methods ---

    def load_file(self):
        global primer_input_file_name
        primer_input_file_name, _ = QFileDialog.getOpenFileName(
            self, "Reformater Load File", "",
            "All Files (*);;Python Files (*.py)")
        self.file_in_label.setText(primer_input_file_name.split('/')[-1])
        window.statusBar().showMessage(
            str(lines_counter(
                primer_input_file_name)
                ) + " primers in input file.", 10000
        )

    def save_file(self):
        global primer_output_file_name
        primer_output_file_name, _ = QFileDialog.getOpenFileName(
            self, "Formatter Load File", "",
            "All Files (*);;Python Files (*.py)")
        self.file_out_lineEdit.setText(primer_output_file_name.split('/')[-1])

    def save_lineEdit(self):
        global primer_output_file_name
        primer_output_file_name = str(self.file_out_lineEdit.text())

    def sequenceID_edit(self):
        global seq_id
        seq_id = str(self.sequence_id_lineEdit.text())

    def primer3_input_generator(self):
        window.generate_pri_progressBar.reset()
        primer3_input()

    def csv_preview(self):
        with open(self.fsh['selector_input'], "r") as csv:
            header = csv.readline().split(",")
            header[-1] = header[-1][0:-1]
            column = 0
            for item in header:
                csv_window.csv_table.setHorizontalHeaderItem(
                    column, QTableWidgetItem(item))
                column += 1
            for line in csv:
                column = 0
                data = line.split(',')
                rowPosition = csv_window.csv_table.rowCount()
                csv_window.csv_table.insertRow(rowPosition)
                for item in data:
                    csv_window.csv_table.setItem(
                        rowPosition, column, QTableWidgetItem(item))
                    column += 1
            csv_window.show()

    def prepare_selector_sorter_table(self):
        parameters = ["any_th", "3p_th", "hairpin_th", "gc_per", "tm"]
        self.selector_sorter_table.setRowCount(len(parameters))
        self.selector_sorter_table.setVerticalHeaderLabels(parameters)

        for i in range(len(parameters)):
            self.selector_sorter_table.setCellWidget(i, 0, CheckBoxWidget(self))
            self.selector_sorter_table.setCellWidget(i, 1, SpinBoxWidget(self))
            self.selector_sorter_table.setCellWidget(i, 2, ComboOrderWidget(self))

        self.selector_sorter_table.resizeColumnToContents(0)


# --- * ---


def lines_counter(file_name):
    with open(file_name, "r") as file:
        tmp = sum(1 for _ in file)
        return tmp


# --- primers randomizer functions ---

def check_runs(prim, trigger_runs):
    if not trigger_runs:
        return True
    else:
        return not (
                'AAAAA' in prim or 'CCCCC' in prim
                or 'TTTTT' in prim or 'GGGGG' in prim)


def check_temp(prim, tmin, tmax, trigger_temp):
    if not trigger_temp:
        return True
    else:
        tm = primer3.calcTm(prim, mv_conc=psm, dv_conc=psd,
                            dntp_conc=pdc, dna_conc=pnc)
        return tmin < tm < tmax


def check_gc(prim, gcmin, gcmax, trigger_gccn):
    if not trigger_gccn:
        return True
    else:
        c = (prim.count('C') + prim.count('G')) / float(length_of_primer)
        return gcmin < c < gcmax


def check_repeats(prim, trigger_rept):
    if not trigger_rept:
        return True
    else:
        repeats = ["ATATATAT", "ACACACAC", "AGAGAGAG", "CACACACA",
                   "CGCGCGCG", "CTCTCTCT", "TATATATA", "TCTCTCTC",
                   "TGTGTGTG", "GAGAGAGA", "GCGCGCGC", "GTGTGTGT"]
        for repeat in repeats:
            if bool(prim.find(repeat) + 1):
                # print(prime, " --- ", repeat)
                return False
        return True


# --- primer randomizer main function


def randomizer():
    n = 0
    counter = 0
    window.generate_progressBar.setValue(0)
    with open(f"{path}/{gen_file_name}", "w") as f:
        while counter < number_of_primers:
            primer = "".join(
                random.choice('ACTG') for _ in range(length_of_primer)
            )
            if check_runs(primer, runs_trigger):
                if check_gc(primer, gc_min, gc_max, gc_trigger):
                    if check_temp(primer, tm_min, tm_max, tm_trigger):
                        if check_repeats(primer, rpts_trigger):
                            f.write(primer + '\n')
                            counter += 1
                            app.processEvents()
                            window.generate_progressBar.setValue(
                                int(100 * counter / number_of_primers))
            n += 1

    window.statusBar().showMessage(str(n) + " primers tested, ratio: " + str(number_of_primers / n), 10000)


# --- primer3 input generator function


def primer3_input():
    counter = 0
    number_of_lines = lines_counter(primer_input_file_name)
    with open(primer_input_file_name, "r") as input_file, open(primer_output_file_name, "w") as output_file:
        output_file.write("SEQUENCE_ID=" + seq_id + end)
        output_file.write("PRIMER_TASK=" + task + end)
        output_file.write("PRIMER_SALT_MONOVALENT=" + str(psm) + end)
        output_file.write("PRIMER_SALT_DIVALENT=" + str(psd) + end)
        output_file.write("PRIMER_DNTP_CONC=" + str(pdc) + end)
        output_file.write("PRIMER_DNA_CONC=" + str(pnc) + end)
        for primer in input_file:
            output_file.write("SEQUENCE_PRIMER=" + primer)
            output_file.write("=\n")
            app.processEvents()
            window.generate_pri_progressBar.setValue(int(counter / number_of_lines * 100))
            counter += 1


def primer3_run():
    input_file_name = primer_output_file_name
    print(os.getcwd())
    output_file_name = primer_output_file_name.split('/')[-1] + "_out"
    window.primer3_out_file_name_label.setText(output_file_name)
    proc: QProcess = QProcess()
    proc.execute("primer3_core", [input_file_name, "--format_output", f"--output={output_file_name}"])
    window.statusBar().showMessage("Primer3 finished.", 3000)


def csv_generator():
    window.generate_csv_progressBar.setValue(0)
    counter = 0
    input_file_name = primer_output_file_name.split('/')[-1] + "_out"
    output_file_name = input_file_name.split('.')[0] + ".csv"
    number_of_lines = lines_counter(input_file_name)
    with open(input_file_name, "r") as file_in:
        with open(output_file_name, "w") as file_out:
            header = "sequence,tm,gc_per,any_th,3p_th,hairpin_th\n"
            file_out.write(header)
            for line in file_in:
                if line[0:5] == "OLIGO":
                    line = file_in.readline().split()
                    tm = line[3]
                    gc = line[4]
                    any_th = line[5]
                    p3_th = line[6]
                    hairpin = line[7]
                    sequence = line[8]
                    file_out.write(
                        sequence + "," + tm + "," + gc + "," + any_th + ","
                        + p3_th + "," + hairpin + "\n")
                window.generate_csv_progressBar.setValue(
                    int(counter / number_of_lines * 100))
                counter += 1
                app.processEvents()


# --- MAIN LOOP ---


if __name__ == "__main__":
    app = QApplication([])
    window = Bits()
    csv_window = CSV_Viewer()
    window.show()
    sys.exit(app.exec_())
