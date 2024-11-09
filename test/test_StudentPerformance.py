# -*- coding: utf-8 -*-
import pytest
from StudentPerformance import StudentPerformance
from Types import DataType


@pytest.fixture
def student_data():
    return {
        "John Doe": [("Math", 100), ("Physics", 100), ("Chemistry", 100)],
        "Alice Smith": [("Math", 90), ("Physics", 80), ("Chemistry", 85)],
        "Bob Johnson": [("Math", 100), ("Physics", 100), ("Chemistry", 100)],
    }


def test_find_student_with_full_marks(student_data):
    performance = StudentPerformance(student_data)
    
    student_name = performance.find_student_with_full_marks()
    
    assert student_name == "John Doe" or student_name == "Bob Johnson"
    # Ожидаем одного из студентов с полными баллами

def test_no_student_with_full_marks():
    student_data = {
        "Alice Smith": [("Math", 90), ("Physics", 80), ("Chemistry", 85)],
        "Bob Johnson": [("Math", 90), ("Physics", 90), ("Chemistry", 90)],
    }
    
    performance = StudentPerformance(student_data)
    
    student_name = performance.find_student_with_full_marks()
    
    assert student_name is None
