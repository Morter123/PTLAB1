# -*- coding: utf-8 -*-
from Types import DataType
import pytest


class CalcRating:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def find_students_with_perfect_scores(self) -> list:
        """
        Находит студентов, у которых все оценки равны 100.
        Возвращает список имен таких студентов.
        """
        perfect_students = []

        for name, subjects in self.data.items():
            # Проверяем, что все оценки равны 100
            if all(score >= 100 for _, score in subjects):
                perfect_students.append(name)

        return perfect_students
