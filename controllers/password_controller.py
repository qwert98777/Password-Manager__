
import json
import os
from typing import List, Optional
from models.password_record import PasswordRecord
from utils.password_generator import PasswordGenerator


class PasswordController:
    """Контроллер управления паролями"""
    
    def __init__(self, data_file: str = "data/passwords.json"):
        self._data_file = data_file
        self._passwords: List[PasswordRecord] = []
        self._load_data()
    
    def _load_data(self):
        """Загрузка из JSON"""
        try:
            if os.path.exists(self._data_file):
                with open(self._data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self._passwords = [PasswordRecord.from_dict(item) for item in data]
        except (json.JSONDecodeError, FileNotFoundError):
            self._passwords = []
    
    def _save_data(self):
        """Сохранение в JSON"""
        try:
            os.makedirs(os.path.dirname(self._data_file), exist_ok=True)
            with open(self._data_file, 'w', encoding='utf-8') as f:
                json.dump([p.to_dict() for p in self._passwords], f, indent=2, ensure_ascii=False)
            return True
        except Exception:
            return False
    
    def add_password(self, service: str, username: str, password: str) -> bool:
        """Добавление пароля с валидацией"""
        try:
            if not service or not service.strip():
                raise ValueError("Сервис обязателен")
            if not username or not username.strip():
                raise ValueError("Имя пользователя обязательно")
            if not password or not password.strip():
                raise ValueError("Пароль обязателен")
            
            # Проверка на дубликат
            for p in self._passwords:
                if p.service.lower() == service.lower() and p.username.lower() == username.lower():
                    raise ValueError("Такая запись уже существует")
            
            record = PasswordRecord(service, username, password)
            self._passwords.append(record)
            self._save_data()
            return True
        except ValueError:
            return False
    
    def get_all_passwords(self) -> List[PasswordRecord]:
        """Получить все пароли"""
        return self._passwords.copy()
    
    def delete_password(self, index: int) -> bool:
        """Удаление по индексу"""
        if 0 <= index < len(self._passwords):
            self._passwords.pop(index)
            self._save_data()
            return True
        return False
    
    def search_passwords(self, term: str) -> List[PasswordRecord]:
        """Поиск по названию сервиса"""
        term_lower = term.lower()
        return [p for p in self._passwords if term_lower in p.service.lower()]
    
    def generate_password(self, settings: dict) -> Optional[str]:
        """Генерация пароля"""
        try:
            return PasswordGenerator.generate(
                length=settings['length'],
                use_uppercase=settings['use_uppercase'],
                use_lowercase=settings['use_lowercase'],
                use_digits=settings['use_digits'],
                use_symbols=settings['use_symbols']
            )
        except ValueError:
            return None
