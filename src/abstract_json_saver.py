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
