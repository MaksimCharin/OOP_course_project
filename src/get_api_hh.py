import json
import requests
from src.abstract_api_hh import AbstractApiHh

class GetApiHh(AbstractApiHh):
    """Класс для работы с API hh.ru"""

    def __init__(self):
        self._all_vacancy = []

    def __repr__(self):
        return f"{self._all_vacancy}"

    @classmethod
    def _connect_to_api(cls, params: dict) -> list:
        """Подключение к API и получение данных"""
        response = requests.get('https://api.hh.ru/vacancies', params=params)
        if response.status_code == 200:
            return response.json()['items']
        else:
            return []

    def get_vacancy_from_api(self, name_vacancy: str) -> list:
        """Получение информации о вакансиях для пользователя"""
        params = {'text': name_vacancy, 'area': 113, 'per_page': 100}
        self._all_vacancy = self._connect_to_api(params)
        return self._all_vacancy

    def get_all_vacancies(self) -> list:
        """Возвращает все вакансии"""
        return self._all_vacancy
