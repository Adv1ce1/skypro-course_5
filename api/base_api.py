from abc import ABC, abstractmethod


class BaseAPI(ABC):
    def __init__(self, base_url: str, number_of_vacancies: int = 100) -> None:

        # Инициализация базового класса для API.
      
        self._base_url = base_url
        self._number_of_vacancies = number_of_vacancies

    @abstractmethod
    def _search_vacancies(self, employer_id) -> list:
      
        # Поиск вакансий на HeadHunter API.
      
        pass
