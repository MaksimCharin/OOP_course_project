from typing import Any

import requests

from src.abstract_api_hh import AbstractApiHh


class ApiHH(AbstractApiHh):
    """Класс для работы с API hh.ru"""

    def __init__(self) -> None:
        self._all_vacancy = []
        self._base_url = "https://api.hh.ru/vacancies"
        self._params = {"text": "", "area": 113, "per_page": 100}

    def __repr__(self) -> str:
        return f"{self._all_vacancy}"

    def _connect_to_api(self, params: dict) -> Any:
        """Подключение к API и получение данных"""
        try:
            response = requests.get(self._base_url, params=params)
            response.raise_for_status()  # Проверка статус-кода
            return response.json()["items"]
        except requests.RequestException as e:
            print(f"Ошибка при запросе к API: {e}")
            return []
        except KeyError:
            print("Ошибка: неверный формат данных от API")
            return []

    def get_vacancy_from_api(self, name_vacancy: str) -> list:
        """Получение информации о вакансиях для пользователя"""
        params = self._params.copy()
        params["text"] = name_vacancy
        self._all_vacancy = self._connect_to_api(params)
        return self._all_vacancy

    def get_all_vacancies(self) -> Any:
        """Возвращает все вакансии"""
        return self._all_vacancy
