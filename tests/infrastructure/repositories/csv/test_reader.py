from types import GeneratorType

import pytest

from infrastructure.repositories.csv.reader import CSVReader


@pytest.fixture
def file_path():
    return "tests/infrastructure/assets/test_csv.csv"


def test_open_file(file_path):
    reader = CSVReader(file_path)
    file = reader.open_file()

    assert isinstance(file, GeneratorType)
    assert next(file) is not None


def test_get_headers(file_path):
    reader = CSVReader(file_path)
    headers = reader.get_headers()

    assert headers == ["First Name", "Last Name", "Birthdate", "Grade"]


def test_get_lenght(file_path):
    reader = CSVReader(file_path)
    file_lenght = reader.get_lenght()

    assert file_lenght == 21


def test_read(file_path):
    reader = CSVReader(file_path)
    read_generator = reader.read(chunk_size=7)
    data_content = []

    for data in read_generator:
        headers = data["headers"]
        data_gen = data["data"]
        for row in data_gen:
            data_content.append(row)

    assert headers == ["First Name", "Last Name", "Birthdate", "Grade"]
    assert isinstance(data_gen, GeneratorType)
    assert data_content[0] == [
        ["First Name", "Last Name", "Birthdate", "Grade"],
        ["Alice", "Smith", "1992-05-14", "88.24"],
        ["Bob", "Johnson", "1988-09-03", "75.89"],
        ["Charlie", "Davis", "1990-12-20", "92.47"],
        ["David", "Clark", "1985-07-28", "78.61"],
        ["Emma", "Miller", "1993-03-10", "86.75"],
        ["Frank", "Moore", "1987-11-05", "95.12"],
    ]
