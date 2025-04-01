import json
import os

from src.json_saver import JsonSaver


def test_json_saver(temp_file):
    # Тестируем сохранение и чтение
    saver = JsonSaver(temp_file)
    test_data = [{"name": "Test"}]

    saver.save_file(test_data)
    assert os.path.exists(temp_file)

    loaded = saver.read_file()
    assert loaded == test_data


def test_add_vacancy(temp_file, sample_vacancies_2):

    saver = JsonSaver(temp_file)

    # Добавляем первую вакансию
    saver.add_vacancy(sample_vacancies_2[0])
    assert os.path.exists(temp_file)

    # Проверяем содержимое файла
    with open(temp_file, "r") as f:
        data = json.load(f)
        assert len(data) == 1
        assert data[0]["name"] == "Python Developer"

    # Пробуем добавить дубликат
    saver.add_vacancy(sample_vacancies_2[0])
    with open(temp_file, "r") as f:
        assert len(json.load(f)) == 1  # Дубликат не добавился

    # Добавляем вторую вакансию
    saver.add_vacancy(sample_vacancies_2[1])
    with open(temp_file, "r") as f:
        assert len(json.load(f)) == 2


def test_add_vacancies(temp_file, sample_vacancies_2):

    saver = JsonSaver(temp_file)

    # Добавляем список вакансий
    saver.add_vacancies(sample_vacancies_2)

    with open(temp_file, "r") as f:
        data = json.load(f)
        assert len(data) == 2
        assert data[0]["url"] == "https://hh.ru/vacancy/1"
        assert data[1]["url"] == "https://hh.ru/vacancy/2"

    # Пробуем добавить дубликаты и новую вакансию
    new_vacancies = [
        sample_vacancies_2[0],  # Дубликат
        {
            "name": "Data Scientist",
            "salary_from": 120000,
            "salary_to": 180000,
            "url": "https://hh.ru/vacancy/3",
            "requirements": "Опыт работы с ML",
        },
    ]
    saver.add_vacancies(new_vacancies)

    with open(temp_file, "r") as f:
        data = json.load(f)
        assert len(data) == 3  # Добавилась только новая вакансия
        assert data[2]["name"] == "Data Scientist"


def test_add_incomplete_vacancy(temp_file):

    saver = JsonSaver(temp_file)
    incomplete_vacancy = {
        "name": "Incomplete",
        "url": "https://hh.ru/vacancy/4",
        # Нет обязательных полей
    }

    saver.add_vacancies([incomplete_vacancy])
    with open(temp_file, "r") as f:
        assert len(json.load(f)) == 0  # Неполная вакансия не добавилась


def test_delete_vacancy(temp_file, sample_vacancies_2):

    saver = JsonSaver(temp_file)
    saver.add_vacancies(sample_vacancies_2)

    # Удаляем одну вакансию
    saver.delete_vacancy("https://hh.ru/vacancy/1")

    with open(temp_file, "r") as f:
        data = json.load(f)
        assert len(data) == 1
        assert data[0]["url"] == "https://hh.ru/vacancy/2"

    # Пробуем удалить несуществующую вакансию
    saver.delete_vacancy("https://hh.ru/vacancy/999")
    with open(temp_file, "r") as f:
        assert len(json.load(f)) == 1  # Ничего не изменилось


def test_read_empty_file(temp_file):

    saver = JsonSaver(temp_file)
    assert saver.read_file() == []  # Для несуществующего файла

    # Создаем пустой файл
    with open(temp_file, "w") as f:
        json.dump([], f)
    assert saver.read_file() == []  # Для существующего пустого файла


def test_save_file(temp_file, sample_vacancies_2):

    saver = JsonSaver(temp_file)
    saver.save_file(sample_vacancies_2)

    with open(temp_file, "r") as f:
        data = json.load(f)
        assert len(data) == 2
        assert data[0]["name"] == "Python Developer"
