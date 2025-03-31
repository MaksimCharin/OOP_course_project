import json
import os
from typing import List, Dict

from config import DATA
from src.abstract_json_saver import AbstractJsonSaver


class JsonSaver(AbstractJsonSaver):
    """Класс для сохранения данных в JSON"""

    def __init__(self, file_path: str = DATA):
        self._file_path = file_path

        if not os.path.exists(self._file_path):
            with open(self._file_path, 'w', encoding='utf-8') as file:
                json.dump([], file)

    def save_file(self, data: List[Dict]) -> None:
        """Сохранение данных в файл (полная перезапись)"""
        with open(self._file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def read_file(self) -> List[Dict]:
        """Чтение данных из файла"""
        with open(self._file_path, encoding="utf-8") as file:
            return json.load(file)

    def add_vacancy(self, vacancy: Dict) -> None:
        """Добавление одной вакансии в файл с проверкой на дубликаты"""
        vacancies = self.read_file()

        # Проверка на дубликаты по URL (как уникальному идентификатору)
        if not any(v['url'] == vacancy['url'] for v in vacancies):
            vacancies.append(vacancy)
            self.save_file(vacancies)

    def add_vacancies(self, vacancies: List[Dict]) -> None:
        """Добавляет вакансии, исключая дубликаты"""
        existing = self.read_file()
        existing_urls = {v['url'] for v in existing}

        new_vacancies = [
            v for v in vacancies
            if v['url'] not in existing_urls
               and all(k in v for k in ['name', 'salary_from', 'salary_to', 'url', 'requirements'])
        ]

        self.save_file(existing + new_vacancies)

    def delete_vacancy(self, vacancy_url: str) -> None:
        """Удаление вакансии по URL"""
        vacancies = self.read_file()
        updated_vacancies = [v for v in vacancies if v['url'] != vacancy_url]
        self.save_file(updated_vacancies)
