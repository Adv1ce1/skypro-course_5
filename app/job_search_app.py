import sys

from api.hh_api import HeadHunterAPI
from config import EMPLOYEERS_VACANCY_ID
from database.db_manager import DBManager
from app.mixin_menu_app import MixinMenuAPP
from utils.сurrency_сonverter import get_currency_data
from app.job_search_meta import JobSearchAppMeta
from utils.loading_progress import show_loading_progress
from utils.generate_unique import generate_unique_four_letter_value


class JobSearchApp(MixinMenuAPP, metaclass=JobSearchAppMeta):
  
    hh_api = HeadHunterAPI()
    db_manager = DBManager()
    existing_values = []

    @classmethod
    def _interact_with_user(cls) -> None:
       
            # Взаимодействие с пользователем.

        cls.db_manager.connect()
        cls.db_manager.clear_tables()
        cls.__get_for_database_all_vacancies()
        cls.main_menu()
        cls.db_manager.disconnect()

    @classmethod
    def __get_for_database_all_vacancies(cls):
      
            # Получение всех вакансий из API и запись в базу данных.
      
        total_employers = len(EMPLOYEERS_VACANCY_ID)
        completed_employers = 0
        for employeer_name, employeer_id in EMPLOYEERS_VACANCY_ID.items():
            company_name = employeer_name
            company_vacancies = cls.hh_api.get_vacancies(employeer_id)
            for vacancy in company_vacancies:
                vacancy_name = vacancy["name"]
                vacancy_url = vacancy["alternate_url"]
                vacancy_from = int(vacancy["salary"]["from"]) if vacancy.get("salary") is not None and vacancy[
                    "salary"].get("from") is not None else 0
                vacancy_to = int(vacancy["salary"]["to"]) if vacancy.get("salary") is not None and vacancy[
                    "salary"].get("to") is not None else 0
                if vacancy.get("salary") and vacancy["salary"]["currency"] not in ["RUR", "RUB"]:
                    vacancy_from *= get_currency_data(vacancy["salary"]["currency"])
                    vacancy_to *= get_currency_data(vacancy["salary"]["currency"])
                vacancy_currency = "RUR"
                vacancy_id = generate_unique_four_letter_value(cls.existing_values)
                cls.db_manager.insert_vacancy_to_all(vacancy_id, company_name, vacancy_name, vacancy_from,
                                                     vacancy_to,
                                                     vacancy_currency,
                                                     vacancy_url)

                cls.db_manager.insert_vacancy_company(vacancy_id, company_name, vacancy_name, vacancy_from,
                                                      vacancy_to,
                                                      vacancy_currency,
                                                      vacancy_url)
            completed_employers += 1
            show_loading_progress(completed_employers, total_employers)
        sys.stdout.write("\rЗагрузка завершена!\n")

    @classmethod
    def _get_vacancies_with_keyword(cls, keyword):
      
            # Получение списка вакансий с заданным ключевым словом.
      
        result_df = cls.db_manager.get_vacancies_with_keyword(keyword)
        result_str = result_df.to_string(index=False)
        print(result_str)

    @classmethod
    def _get_avg_salary(cls):
      
          # Получение средней зарплаты по вакансиям.

        print(cls.db_manager.get_avg_salary())

    @classmethod
    def _get_vacancies_with_higher_salary(cls):
      
          # Получение списка вакансий с зарплатой выше средней.

        result_df = cls.db_manager.get_vacancies_with_higher_salary()
        result_str = result_df.to_string(index=False)
        print(result_str)

    @classmethod
    def _get_companies_and_vacancies_count(cls):
      
        # Получение списка всех компаний и количества вакансий у каждой компании.

        result_df = cls.db_manager.get_companies_and_vacancies_count()
        result_str = result_df.to_string(index=False)
        print(result_str)

    @classmethod
    def _get_top_vacancies(cls):
      
        # Получение списка топ-300 вакансий.

        result_df = cls.db_manager.get_top_vacancies()
        result_str = result_df.to_string(index=False)
        print(result_str)
