import requests
from src.vacancy import Vacancy
from src.abstract import GetVacancies


class HeadHunterAPI(GetVacancies):
    """ Класс для подключения к сайту hh.ru"""

    def init(self, name):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__name = name
        self.__params = {
            'text': self.__name,
            'per_page': 100,  # количество вакансий
            'area': '113'  # Регион. Необходимо передавать id из справочника /areas.
        }

    def get_vacancies(self, name_job, pages):
        hh_list = []
        for i in range(pages):
            params = {
                'text': name_job,
                'per_page': 99,
                'pege': i
            }
            response = requests.get('https://api.hh.ru/vacancies', params=params)
            response_json = response.json()
            for j in response_json['items']:
                hh_title = j['name']
                if not (j['area']) is None:
                    hh_town = j['area']['name']
                else:
                    hh_town = None
                if not ((j['salary'] is None) or j['salary']['from'] is None):
                    salary_from = j['salary']['from']
                    salary_to = j['salary']['to']
                else:
                    salary_from = 0
                    salary_to = 0
                hh_employment = j['employment']['name']
                hh_url = j['alternate_url']
                hh_vacancy = Vacancy(hh_title, hh_town, salary_from, salary_to, hh_employment, hh_url)
                hh_list.append(hh_vacancy)
        return hh_list