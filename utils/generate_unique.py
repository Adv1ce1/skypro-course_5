import random
import string


def generate_unique_four_letter_value(existing_values) -> str:
    alphabet = string.ascii_uppercase  # Получаем алфавит в верхнем регистре

    while True:
        value = ''.join(random.choice(alphabet) for _ in range(4))  # Генерируем случайное четырехсимвольное значение
        if value not in existing_values:  # Проверяем, есть ли значение в списке существующих значений
            existing_values.append(value)  # Добавляем уникальное значение в список существующих
            return value  # Возвращаем уникальное значение
