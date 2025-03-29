import os
import unittest

from src.json_saver import JsonSaver


def test_save_and_read_file():
    file_path = "test_vacancies.json"
    saver = JsonSaver(file_path)

    data = [
        {
            "name": "Test Vacancy",
            "salary_from": 100000,
            "salary_to": 150000,
            "url": "https://hh.ru/vacancy/123456",
            "city": "Moscow",
        }
    ]
    saver.save_file(data)
    read_data = saver.read_file()

    assert data == read_data

    if os.path.exists(file_path):
        os.remove(file_path)


def test_add_vacancy_to_file():
    file_path = "test_vacancies.json"
    saver = JsonSaver(file_path)

    data = [
        {
            "name": "Test Vacancy",
            "salary_from": 100000,
            "salary_to": 150000,
            "url": "https://hh.ru/vacancy/123456",
            "city": "Moscow",
        }
    ]
    saver.add_vacancy_to_file(data)
    read_data = saver.read_file()

    assert data == read_data

    if os.path.exists(file_path):
        os.remove(file_path)


def test_delete_vacancy():
    file_path = "test_vacancies.json"
    saver = JsonSaver(file_path)

    data = [
        {
            "name": "Test Vacancy",
            "salary_from": 100000,
            "salary_to": 150000,
            "url": "https://hh.ru/vacancy/123456",
            "city": "Moscow",
        }
    ]
    saver.add_vacancy_to_file(data)
    saver.delete_vacancy("Test Vacancy")
    read_data = saver.read_file()

    assert read_data == []

    if os.path.exists(file_path):
        os.remove(file_path)


if __name__ == "__main__":
    test_save_and_read_file()
    test_add_vacancy_to_file()
    test_delete_vacancy()
    print("All tests passed.")
