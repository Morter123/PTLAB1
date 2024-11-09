# -*- coding: utf-8 -*-
from Types import DataType


class StudentPerformance:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def find_student_with_full_marks(self):
        """
        Возвращает студента с 100 баллами по всем дисциплинам.
        Если таких студентов несколько, возвращает любого из них.
        Если таких студентов нет, выводит сообщение.
        """
        for student_name, subjects in self.data.items():
            if all(score == 100 for _, score in subjects):
                return student_name
        print("Нет студентов с 100 баллами по всем дисциплинам.")
        return None
