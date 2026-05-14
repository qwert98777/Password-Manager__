
from datetime import datetime
from typing import Dict, Any


class PasswordRecord:
    """Класс для хранения записи пароля"""
    
    def __init__(self, service: str, username: str, password: str, created_at: str = None):
        self._service = service.strip()
        self._username = username.strip()
        self._password = password
        self._created_at = created_at if created_at else datetime.now().isoformat()
    
    @property
    def service(self) -> str:
        return self._service
    
    @service.setter
    def service(self, value: str):
        if not value or not value.strip():
            raise ValueError("Название сервиса не может быть пустым")
        self._service = value.strip()
    
    @property
    def username(self) -> str:
        return self._username
    
    @username.setter
    def username(self, value: str):
        if not value or not value.strip():
            raise ValueError("Имя пользователя не может быть пустым")
        self._username = value.strip()
    
    @property
    def password(self) -> str:
        return self._password
    
    @password.setter
    def password(self, value: str):
        if not value or not value.strip():
            raise ValueError("Пароль не может быть пустым")
        self._password = value
    
    @property
    def created_at(self) -> str:
        return self._created_at
    
    def to_dict(self) -> Dict[str, Any]:
        """Конвертация в словарь для JSON"""
        return {
            'service': self._service,
            'username': self._username,
            'password': self._password,
            'created_at': self._created_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'PasswordRecord':
        """Создание из словаря"""
        return cls(
            service=data['service'],
            username=data['username'],
            password=data['password'],
            created_at=data.get('created_at')
        )
    
    def __str__(self) -> str:
        return f"{self._service} | {self._username} | {self._created_at[:10]}"
