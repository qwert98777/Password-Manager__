

from typing import List
from models.password_record import PasswordRecord


class ConsoleView:
    """Класс для консольного ввода/вывода"""
    
    @staticmethod
    def show_welcome():
        print("\n" + "=" * 50)
        print("     МЕНЕДЖЕР ПАРОЛЕЙ v1.0")
        print("=" * 50)
    
    @staticmethod
    def show_goodbye():
        print("\n" + "=" * 50)
        print("До свидания! Ваши пароли в безопасности.")
        print("=" * 50)
    
    @staticmethod
    def show_title(title: str):
        print("\n" + "-" * 40)
        print(title)
        print("-" * 40)
    
    @staticmethod
    def display_menu():
        print("\n" + "=" * 50)
        print("ГЛАВНОЕ МЕНЮ")
        print("=" * 50)
        print("1. Добавить пароль")
        print("2. Просмотреть все пароли")
        print("3. Удалить пароль")
        print("4. Сгенерировать пароль")
        print("5. Поиск паролей")
        print("6. Выход")
        print("=" * 50)
    
    @staticmethod
    def get_input(prompt: str) -> str:
        return input(prompt)
    
    @staticmethod
    def show_success(message: str):
        print(f"[OK] {message}")
    
    @staticmethod
    def show_error(message: str):
        print(f"[ERROR] {message}")
    
    @staticmethod
    def show_password(password: str):
        print("\n" + "=" * 50)
        print("СГЕНЕРИРОВАННЫЙ ПАРОЛЬ:")
        print("=" * 50)
        print(password)
        print("=" * 50)
    
    @staticmethod
    def display_passwords(passwords: List[PasswordRecord]):
        if not passwords:
            print("\nНет сохраненных паролей.")
            return
        
        print("\n" + "=" * 80)
        print(f"{'ID':<4} {'СЕРВИС':<25} {'ПОЛЬЗОВАТЕЛЬ':<30} {'ДАТА':<15}")
        print("-" * 80)
        
        for idx, record in enumerate(passwords, 1):
            service = record.service[:25]
            username = record.username[:30]
            date = record.created_at[:10]
            print(f"{idx:<4} {service:<25} {username:<30} {date:<15}")
        
        print("=" * 80)
    
    @staticmethod
    def display_password_details(record: PasswordRecord):
        print("\n" + "=" * 50)
        print("ДЕТАЛИ ПАРОЛЯ")
        print("=" * 50)
        print(f"Сервис:    {record.service}")
        print(f"Логин:     {record.username}")
        print(f"Пароль:    {record.password}")
        print(f"Создан:    {record.created_at}")
        print("=" * 50)
    
    @staticmethod
    def get_password_settings() -> dict:
        print("\nНАСТРОЙКИ ГЕНЕРАЦИИ")
        print("-" * 40)
        
        try:
            length_input = input("Длина (8-50, по умолчанию 12): ")
            length = int(length_input) if length_input else 12
            length = max(8, min(50, length))
        except ValueError:
            length = 12
        
        use_upper = input("Заглавные буквы? (y/n, по умолчанию y): ").lower() != 'n'
        use_lower = input("Строчные буквы? (y/n, по умолчанию y): ").lower() != 'n'
        use_digits = input("Цифры? (y/n, по умолчанию y): ").lower() != 'n'
        use_symbols = input("Символы? (y/n, по умолчанию y): ").lower() != 'n'
        
        return {
            'length': length,
            'use_uppercase': use_upper,
            'use_lowercase': use_lower,
            'use_digits': use_digits,
            'use_symbols': use_symbols
        }
    
    @staticmethod
    def get_delete_id(max_id: int) -> int:
        try:
            delete_id = int(input(f"Введите ID для удаления (1-{max_id}): "))
            if 1 <= delete_id <= max_id:
                return delete_id - 1
        except ValueError:
            pass
        return -1
