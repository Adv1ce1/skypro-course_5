from config import QUERIES_PATH


def read_sql() -> dict:
    sql_queries = {}
    current_query_name = None
    current_query = ""

    with open(QUERIES_PATH, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith("--"):
                if current_query_name and current_query:
                    sql_queries[current_query_name] = current_query.strip()
                current_query_name = line.lstrip("--").strip()
                current_query = ""
            else:
                current_query += line

    # Добавляем последний запрос, если он есть
    if current_query_name and current_query:
        sql_queries[current_query_name] = current_query.strip()

    return sql_queries
