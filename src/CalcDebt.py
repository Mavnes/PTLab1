# -*- coding: utf-8 -*-
from Types import DataType


class CalcDebt:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.debt: int = 0

    def marks_tolist(self, marks):
        list = []
        for mark in marks:
            list.append(mark[1])
        return list

    def calc(self) -> int:
        for _, marks in self.data.items():
            list = self.marks_tolist(marks)
            if any(mark < 61 for mark in list):
                self.debt += 1
        return self.debt
