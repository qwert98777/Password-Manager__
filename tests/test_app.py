"""
Модульные тесты для приложения
"""

import unittest
import os
import tempfile
from models.password_record import PasswordRecord
from utils.password_generator import PasswordGenerator


class TestPasswordRecord(unittest.TestCase):
    """Тесты для модели PasswordRecord"""
    
    def test_create_valid_record(self):
        """Позитивный тест: создание записи"""
        record = PasswordRecord("Google", "user@mail.com", "pass123")
        self.assertEqual(record.service, "Google")
        self.assertEqual(record.username, "user@mail.com")
        self.assertEqual(record.password, "pass123")
    
    def test_empty_service_raises_error(self):
        """Негативный тест: пустое название сервиса"""
        record = PasswordRecord("test", "user", "pass")
        with self.assertRaises(ValueError):
            record.service = ""
    
    def test_empty_username_raises_error(self):
        """Негативный тест: пустое имя пользователя"""
        record = PasswordRecord("test", "user", "pass")
        with self.assertRaises(ValueError):
            record.username = ""
    
    def test_empty_password_raises_error(self):
        """Негативный тест: пустой пароль"""
        record = PasswordRecord("test", "user", "pass")
        with self.assertRaises(ValueError):
            record.password = ""
    
    def test_to_dict(self):
        """Тест конвертации в словарь"""
        record = PasswordRecord("Test", "user", "pass")
        data = record.to_dict()
        self.assertEqual(data['service'], "Test")
        self.assertEqual(data['username'], "user")
        self.assertEqual(data['password'], "pass")
        self.assertIn('created_at', data)
    
    def test_from_dict(self):
        """Тест создания из словаря"""
        data = {'service': 'GitHub', 'username': 'coder', 'password': '123456'}
        record = PasswordRecord.from_dict(data)
        self.assertEqual(record.service, "GitHub")
        self.assertEqual(record.username, "coder")
        self.assertEqual(record.password, "123456")


class TestPasswordGenerator(unittest.TestCase):
    """Тесты для генератора паролей"""
    
    def test_generate_default_length(self):
        """Позитивный тест: длина по умолчанию 12"""
        password = PasswordGenerator.generate()
        self.assertEqual(len(password), 12)
    
    def test_generate_custom_length(self):
        """Позитивный тест: заданная длина"""
        password = PasswordGenerator.generate(length=20)
        self.assertEqual(len(password), 20)
    
    def test_generate_only_digits(self):
        """Тест: только цифры"""
        password = PasswordGenerator.generate(
            use_uppercase=False, 
            use_lowercase=False, 
            use_symbols=False, 
            use_digits=True
        )
        self.assertTrue(password.isdigit())
    
    def test_generate_only_letters(self):
        """Тест: только буквы"""
        password = PasswordGenerator.generate(use_digits=False, use_symbols=False)
        self.assertTrue(password.isalpha())
    
    def test_generate_too_short(self):
        """Граничный тест: слишком короткий пароль"""
        with self.assertRaises(ValueError):
            PasswordGenerator.generate(length=3)
    
    def test_generate_too_long(self):
        """Граничный тест: слишком длинный пароль"""
        with self.assertRaises(ValueError):
            PasswordGenerator.generate(length=100)
    
    def test_generate_no_char_types(self):
        """Негативный тест: нет типов символов"""
        with self.assertRaises(ValueError):
            PasswordGenerator.generate(
                use_uppercase=False, 
                use_lowercase=False, 
                use_digits=False, 
                use_symbols=False
            )


if __name__ == '__main__':
    unittest.main()
