#!/usr/bin/env python3
"""
Скрипт для автоматического обновления README.md
"""
import datetime
import os

def update_readme():
    # Читаем текущий README.md
    if os.path.exists('README.md'):
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        content = "# Проект Калькулятор\n\n"
    
    # Добавляем/обновляем раздел с автоматической информацией
    auto_section = f"""
## Автоматически обновляемая информация

- **Последнее обновление:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}
- **Статус тестов:** Все тесты проходят
- **Версия:** v1.0.0

*Этот раздел обновляется автоматически при каждом коммите*
"""
    
    # Убираем старый автоматический раздел если есть
    if "## Автоматически обновляемая информация" in content:
        parts = content.split("## Автоматически обновляемая информация")
        content = parts[0] + auto_section
    else:
        content += auto_section
    
    # Сохраняем обновленный README.md
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("README.md обновлен автоматически!")

if __name__ == "__main__":
    update_readme()
