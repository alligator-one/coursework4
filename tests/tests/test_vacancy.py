import pytest
from src.vacancy import Vacancy


@pytest.fixture
def v():
    v = Vacancy("Системный администратор",
                "Ташкент",
                7000000,
                7000000,
                "Полная занятость",
                "https://hh.ru/vacancy/94487058")
    return v


def test__init__(v):
    assert v.vacancy_title == "Системный администратор"
    assert v.town == "Ташкент"
    assert v.salary_from == 7000000
    assert v.salary_to == 7000000
    assert v.employment == "Полная занятость"
    assert v. url == "https://hh.ru/vacancy/94487058"