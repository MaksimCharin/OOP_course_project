import json
import os

from config import DATA
from src.abstract_json_saver import AbstractJsonSaver

class JsonSaver(AbstractJsonSaver):
    """Класс для сохранения данных в JSON"""

    def __init__(self, file_path: str = DATA):
        self._file_path = file_path

    def save_file(self, data: list):
        """Сохранение файла"""
        with open(self._file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def read_file(self) -> list:
        """Чтение файл"""
        if not os.path.exists(self._file_path):
            return []
        with open(self._file_path, encoding='utf-8') as file:
            return json.load(file)

    def add_vacancy_to_file(self, data: list):
        """Добавление вакансии в файл"""
        old_list = self.read_file()
        new_list = data + old_list
        self.save_file(new_list)

    def delete_vacancy(self, vacancy: str):
        """Удаление вакансии из файла"""
        new_list = []
        old_list = self.read_file()
        for params in old_list:
            if params['name'] != vacancy:
                new_list.append(params)
        self.save_file(new_list)