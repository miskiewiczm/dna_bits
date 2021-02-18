# Primer selector - primer source is a csv cross file.
# Version 0.0.2 with changes in seek_primer function
# needs more testing

import numpy as np
from typing import Dict, List


class PrimerCross:
    def __init__(self, primers: List[str]):
        self.primers = primers

    def seek_primer(self, x, y, max_x, max_val):
        """find minimal coverage for single row"""
        if y >= max_x:
            return -1
        i = y
        while self.cross_matrix[x][i] > max_val:
            i = i + 1
            if i > max_x:
                return -1
        return i

    def check_primer(self, y, chain_pos, value):
        k = chain_pos
        while k > 0:
            if self.cross_matrix[y][self.primers_chain[k]] > value:
                return False
            k = k - 1
        return True

    @staticmethod
    def comparer(primer1: str, primer2: str):
        if not primer1 or not primer2:
            return -1

        primer2 = primer2[::-1]
        p1_tab = '*' * (len(primer1 + primer2) - 2) + primer1
        p2_tab = '*' * (len(primer1) - 1) + primer2
        align = []

        for i in range(len(primer1 + primer2) - 1):
            common = list(zip(p1_tab[i:], p2_tab))
            align.append(
                common.count(("A", "T")) + common.count(("T", "A")) +
                common.count(("C", "G")) + common.count(("G", "C"))
            )
        return max(align)

    def generate_cross(self) -> List[List[float]]:
        """input is file of newline separated chosen primers"""
        count = len(self.primers)
        cross = np.zeros((count, count))

        for i, primer_1 in enumerate(self.primers):
            for j, primer_2 in enumerate(self.primers[i + 1:], start=i + 1):
                cross[i, j] = self.comparer(primer_1, primer_2)

        return cross.tolist()

    def best(self, primers_cross_best: List[List[float]]) -> Dict[int, List[int]]:
        # macierz z csv
        # self.cross_matrix = np.genfromtxt(primers_cross_best)
        self.cross_matrix = np.array(primers_cross_best)
        # print(len(self.cross_matrix[0]))
        self.primers_chain = []

        n_of_primers = len(self.cross_matrix[0])
        max_pos = n_of_primers - 1
        count = 0

        # initial primer selection as its number
        # dowolny wybrany wiersz (primer)
        # wybieramy w csv viewer
        # im dłuższy primer chain tym lepiej
        # każdy primer ma 20 charów
        row = 6
        pos_x = 0
        # maksymalne przekrycie na jakie pozwalamy
        score = 5
        # dołączamy go do łańcucha
        self.primers_chain.append(row)

        while count < n_of_primers:
            # szukam primera który spełnia warunki względem row
            poi = self.seek_primer(row, pos_x, max_pos, score)
            if poi == -1:
                # żaden nie spełnia warunków
                print("==========================")
                print("End of primers line, BREAK")
                break

            if self.check_primer(poi, count, score):
                # ma przekrycie mniejsze niż score
                # nie pokrywa się z żadnym z poprzednich
                print(count, poi, " - ACCEPTED.")
                self.primers_chain.append(poi)
                count = count + 1
            pos_x = poi + 1
        print("==========================")
        print(self.primers_chain)

        # name = "/Users/marek/primers/primers3_selected_best.txt"
        # file = open(name, "r")
        selected_best = []

        for i in range(n_of_primers):
            # line = file.readline()
            if i in self.primers_chain[1:]:
                # print(">")
                # print(line[:-1])
                # print(i)
                selected_best.append(i)
        # file.close()
        return {row: selected_best}

    def best_to_str(self, best: Dict[int, List[int]]) -> Dict[str, List[str]]:
        results = {}
        for key, values in best.items():
            results[self.primers[key]] = list(map(lambda t: self.primers[t], values))

        return results
