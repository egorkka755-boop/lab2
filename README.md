# Проект Калькулятор

Простой калькулятор на Python с базовыми математическими операциями.

## Функциональность

- **Сложение** - `add(a, b)`
- **Вычитание** - `subtract(a, b)`  
- **Умножение** - `multiply(a, b)`
- **Деление** - `divide(a, b)`
- **Возведение в степень** - `power(base, exponent)`
- **Факториал** - `factorial(n)`
- **Процент** - `percentage(part, whole)`

## Использование 

from src.calculator import Calculator

calc = Calculator()
result = calc.add(5, 3)  # 8
print(result)

## Тестирование

python -m pytest tests/ -v

## Структура проекта

project/
├── src/calculator.py           # Основной код
├── tests/test_calculator.py    # Тесты
├── requirements.txt            # Зависимости
└── README.md                   # Документация


## Автоматически обновляемая информация

- **Последнее обновление:** 2025-10-27 21:20
- **Статус тестов:** Все тесты проходят
- **Версия:** v1.0.0

*Этот раздел обновляется автоматически при каждом коммите*

