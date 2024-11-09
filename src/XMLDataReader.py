# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from Types import DataType
from DataReader import DataReader


class XMLDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        """
        Парсит XML файл и возвращает данные о студентах.
        Формат XML предполагает, что каждый студент представлен элементом <student> с атрибутом name
        и вложенными элементами для каждого предмета с оценками.
        """
        try:
            tree = ET.parse(path)  # парсим XML файл
            root = tree.getroot()  # получаем корень XML документа

            # Обрабатываем каждого студента
            for student_elem in root.findall("student"):
                name_elem = student_elem.get("name")  # имя студента
                if name_elem:
                    self.key = name_elem.strip()
                else:
                    continue  # если нет имени, пропускаем этого студента
                
                self.students[self.key] = []

                # Обрабатываем каждый предмет и оценку
                for subject_elem in student_elem:
                    subject_name = subject_elem.tag.strip()  # название предмета
                    score_text = subject_elem.text.strip() if subject_elem.text else None
                    
                    if score_text is not None:
                        try:
                            score = int(score_text)  # оценка (конвертируем в целое число)
                            self.students[self.key].append((subject_name, score))
                        except ValueError:
                            continue  # если ошибка преобразования, пропускаем
            return self.students

        except ET.ParseError as e:
            print(f"Ошибка при парсинге XML файла: {e}")
        except FileNotFoundError:
            print(f"Файл {path} не найден.")
        except Exception as e:
            print(f"Ошибка при чтении XML файла: {e}")
        
        return {}
