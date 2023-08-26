import requests
from api.base_api import BaseAPI


class HeadHunterAPI(BaseAPI):
  
        # Класс для запроса вакансий на HeadHunter API

    url: str = 'https://api.hh.ru/vacancies'

    def __init__(self, url: str = url):

        # Инициализация класса HeadHunterAPI.

        super().__init__(url)

    def _search_vacancies(self, employer_id, page=1) -> list:

        # Поиск вакансий на HeadHunter API.

        params = {
            'employer_id': employer_id,
            'per_page': self._number_of_vacancies,
            'archived': False,
            'page': page,
        }
        response = requests.get(url=self._base_url, params=params)
        response_json = response.json()
        return response_json.get("items", [])

    def get_vacancies(self, employer_id: int) -> list[dict]:
        vacancies = []  # список с вакансиями
        for page in range(20):
            vacancies_page = self._search_vacancies(employer_id, page)
            if len(vacancies_page) == 0:
                # Если в запросе нет вакансий, завершаем цикл
                break
            vacancies.extend(vacancies_page)
        return vacancies
