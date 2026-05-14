
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from views.console_view import ConsoleView
from controllers.password_controller import PasswordController


class PasswordManagerApp:
    """Главный класс приложения"""
    
    def __init__(self):
        self.controller = PasswordController()
        self.view = ConsoleView()
    
    def run(self):
        """Запуск главного цикла"""
        self.view.show_welcome()
        
        while True:
            self.view.display_menu()
            choice = self.view.get_input("\nВаш выбор: ")
            
            if choice == '1':
                self.add_password()
            elif choice == '2':
                self.view_passwords()
            elif choice == '3':
                self.delete_password()
            elif choice == '4':
                self.generate_password()
            elif choice == '5':
                self.search_passwords()
            elif choice == '6':
                self.view.show_goodbye()
                break
            else:
                self.view.show_error("Неверный выбор")
    
    def add_password(self):
        """Добавление нового пароля"""
        self.view.show_title("ДОБАВЛЕНИЕ ПАРОЛЯ")
        
        service = self.view.get_input("Название сервиса: ")
        if not service:
            self.view.show_error("Название сервиса обязательно")
            return
        
        username = self.view.get_input("Имя пользователя: ")
        if not username:
            self.view.show_error("Имя пользователя обязательно")
            return
        
        generate = self.view.get_input("Сгенерировать пароль? (y/n): ").lower()
        
        if generate == 'y':
            settings = self.view.get_password_settings()
            password = self.controller.generate_password(settings)
            if password:
                print(f"\nСгенерированный пароль: {password}")
                use_it = self.view.get_input("Использовать этот пароль? (y/n): ").lower()
                if use_it != 'y':
                    password = self.view.get_input("Введите свой пароль: ")
            else:
                password = self.view.get_input("Введите пароль: ")
        else:
            password = self.view.get_input("Введите пароль: ")
        
        if self.controller.add_password(service, username, password):
            self.view.show_success(f"Пароль для '{service}' сохранен!")
        else:
            self.view.show_error("Не удалось сохранить пароль")
    
    def view_passwords(self):
        """Просмотр всех паролей"""
        passwords = self.controller.get_all_passwords()
        self.view.display_passwords(passwords)
        
        if passwords:
            show = self.view.get_input("\nПоказать пароль? Введите ID (или Enter): ")
            if show.isdigit():
                idx = int(show) - 1
                if 0 <= idx < len(passwords):
                    self.view.display_password_details(passwords[idx])
    
    def delete_password(self):
        """Удаление пароля"""
        passwords = self.controller.get_all_passwords()
        self.view.display_passwords(passwords)
        
        if passwords:
            delete_id = self.view.get_delete_id(len(passwords))
            if delete_id >= 0:
                confirm = self.view.get_input("Вы уверены? (y/n): ").lower()
                if confirm == 'y':
                    if self.controller.delete_password(delete_id):
                        self.view.show_success("Пароль удален!")
                    else:
                        self.view.show_error("Ошибка при удалении")
    
    def generate_password(self):
        """Генерация пароля"""
        self.view.show_title("ГЕНЕРАТОР ПАРОЛЕЙ")
        settings = self.view.get_password_settings()
        password = self.controller.generate_password(settings)
        
        if password:
            self.view.show_password(password)
            
            save = self.view.get_input("\nСохранить этот пароль? (y/n): ").lower()
            if save == 'y':
                service = self.view.get_input("Название сервиса: ")
                username = self.view.get_input("Имя пользователя: ")
                if service and username:
                    if self.controller.add_password(service, username, password):
                        self.view.show_success("Пароль сохранен!")
                else:
                    self.view.show_error("Сервис и имя пользователя обязательны")
    
    def search_passwords(self):
        """Поиск паролей"""
        term = self.view.get_input("Введите название сервиса для поиска: ")
        if term:
            results = self.controller.search_passwords(term)
            if results:
                self.view.show_success(f"Найдено {len(results)} записей:")
                self.view.display_passwords(results)
            else:
                self.view.show_error(f"Ничего не найдено для '{term}'")


if __name__ == "__main__":
    app = PasswordManagerApp()
    app.run()
