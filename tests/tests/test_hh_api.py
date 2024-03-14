import pytest
from src.vacancy import Vacancy
from abc import ABC
from src.abstract import GetVacancies
from src.hh_api import HeadHunterAPI


@pytest.fixture
def v():
    v = Vacancy("Системный администратор",
                "Ташкент",
                7000000,
                8000000,
                "Полная занятость",
                "https://hh.ru/vacancy/94487058")
    return v


def test_issubclass():
    assert issubclass(GetVacancies, ABC)
    assert issubclass(HeadHunterAPI, GetVacancies)
