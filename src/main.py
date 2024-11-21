# -*- coding: utf-8 -*-
import argparse
import sys
from XMLDataReader import XMLDataReader
from CalcRating import CalcRating
import random


def get_path_from_arguments(args) -> str:

    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():

    path = get_path_from_arguments(sys.argv[1:])
    reader = XMLDataReader()
    students = reader.read(path)

    if not students:
        print("Нет данных о студентах.")
        return

    # Используем CalcRating для поиска студентов с идеальными оценками
    rating = CalcRating(students)
    perfect_students = rating.find_students_with_perfect_scores()

    if perfect_students:
        print("Студент(ы) с 100 баллами по всем дисциплинам:")
        random_student = random.choice(perfect_students)
        print(random_student)
    else:
        print("Нет студентов с 100 баллами по всем дисциплинам.")


if __name__ == "__main__":
    main()
