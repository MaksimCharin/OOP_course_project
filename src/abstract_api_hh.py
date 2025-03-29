from abc import ABC, abstractmethod


class AbstractApiHh(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def get_vacancy_from_api(self, name_vacancy):
        """Метод для получения вакансий с API"""
        pass
