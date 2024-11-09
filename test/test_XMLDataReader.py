import pytest
from unittest.mock import patch, mock_open
from XMLDataReader import XMLDataReader
from Types import DataType


@pytest.fixture
def xml_data():
    return """<?xml version="1.0" encoding="UTF-8"?>
              <root>
                <student name="Иванов Иван Иванович">
                    <математика>100</математика>
                    <литература>100</литература>
                    <программирование>101</программирование>
                </student>
                <student name="Петров Петр Петрович">
                    <математика>100</математика>
                    <химия>100</химия>
                    <социология>99</социология>
                </student>
                <student name="Андреев Андрей Андреевич">
                    <математика>100</математика>
                    <химия>100</химия>
                    <социология>100</социология>
                </student>
              </root>"""


def test_xml_data_reader(xml_data):
    # Используем mock_open для имитации чтения файла
    with patch("builtins.open", mock_open(read_data=xml_data)):
        reader = XMLDataReader()
        students = reader.read("fake_path.xml")
        
        # Проверяем, что студенты правильно загружены
        assert "Иванов Иван Иванович" in students
        assert "Петров Петр Петрович" in students
        assert "Андреев Андрей Андреевич" in students
        
        # Проверяем количество предметов для каждого студента
        assert len(students["Иванов Иван Иванович"]) == 3
        assert len(students["Петров Петр Петрович"]) == 3
        assert len(students["Андреев Андрей Андреевич"]) == 3
        
        # Проверяем, что оценки правильные
        assert students["Иванов Иван Иванович"][0] == ("математика", 100)
        assert students["Иванов Иван Иванович"][1] == ("литература", 100)
        assert students["Иванов Иван Иванович"][2] == ("программирование", 101)
        
        assert students["Петров Петр Петрович"][0] == ("математика", 100)
        assert students["Петров Петр Петрович"][1] == ("химия", 100)
        assert students["Петров Петр Петрович"][2] == ("социология", 99)
        
        assert students["Андреев Андрей Андреевич"][0] == ("математика", 100)
        assert students["Андреев Андрей Андреевич"][1] == ("химия", 100)
        assert students["Андреев Андрей Андреевич"][2] == ("социология", 100)
