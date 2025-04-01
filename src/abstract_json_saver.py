from abc import ABC, abstractmethod


class AbstractJsonSaver(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def save_file(self, data: list) -> None:
        """Метод для сохранения данных в файл"""
        pass

    @abstractmethod
    def read_file(self) -> None:
        """Метод для чтения данных из файла"""
        pass
    @abstractmethod
    def add_vacancy(self) -> None:
        """Добавление одной вакансии в файл с проверкой на дубликаты"""
        pass

    @abstractmethod
    def add_vacancies(self) -> None:
        """Добавляет вакансии, исключая дубликаты"""
        pass

    @abstractmethod
    def delete_vacancy(self) -> None:
        """Удаление вакансии по URL"""
        pass