import csv
import json


class MixinFileOperations:
  
    def clear_tables(self) -> None:
       
        # Выполняет запрос на удаление всех таблиц базы данных.
              
        query = self.sql_queries["Удаление всех таблиц"]
        self._execute_query(query)

    def write_vacancies_to_json(self, filename) -> bool:

            # Записывает данные о вакансиях в JSON файл.
      
        vacancies = self._get_all_vacancies()
        if vacancies is None or vacancies.empty:
            print("No vacancies found to write to the JSON file.")
            return False
        try:
            vacancies_list = vacancies.to_dict(orient='records')
            with open(filename, 'w', encoding='utf-8') as json_file:
                json.dump(vacancies_list, json_file, indent=4, ensure_ascii=False)
            print(f"Vacancies are successfully written to {filename}.")
            return True
        except Exception as e:
            print(f"Error occurred while writing vacancies to {filename}: {e}")
            return False

    def write_vacancies_to_csv(self, filename) -> bool:
      
            # Записывает данные о вакансиях в CSV файл.

        vacancies = self._get_all_vacancies()
        if vacancies is None or vacancies.empty:
            print("No vacancies found to write to the CSV file.")
            return False
        try:
            vacancies.to_csv(filename, index=False, quoting=csv.QUOTE_NONNUMERIC, encoding='windows-1251')
            print(f"Vacancies are successfully written to {filename}.")
            return True
        except Exception as e:
            print(f"Error occurred while writing vacancies to {filename}: {e}")
            return False
