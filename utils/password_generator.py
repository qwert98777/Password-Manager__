"""
Генератор случайных паролей
"""

import random
import string


class PasswordGenerator:
    """Класс для генерации паролей"""
    
    @staticmethod
    def generate(length: int = 12, use_uppercase: bool = True, 
                use_lowercase: bool = True, use_digits: bool = True, 
                use_symbols: bool = True) -> str:
        """
        Генерация случайного пароля
        
        Параметры:
            length: длина пароля (4-50)
            use_uppercase: использовать заглавные буквы
            use_lowercase: использовать строчные буквы
            use_digits: использовать цифры
            use_symbols: использовать символы
        
        Возвращает:
            Сгенерированный пароль
        """
        # Валидация длины
        if length < 4:
            raise ValueError("Пароль слишком короткий (мин 4)")
        if length > 50:
            raise ValueError("Пароль слишком длинный (макс 50)")
        
        # Собираем доступные символы
        chars = ''
        if use_uppercase:
            chars += string.ascii_uppercase
        if use_lowercase:
            chars += string.ascii_lowercase
        if use_digits:
            chars += string.digits
        if use_symbols:
            chars += '!@#$%^&*()_+-=[]{}|;:,.<>?'
        
        if not chars:
            raise ValueError("Выберите хотя бы один тип символов")
        
        # Гарантируем включение каждого выбранного типа
        password = []
        if use_uppercase:
            password.append(random.choice(string.ascii_uppercase))
        if use_lowercase:
            password.append(random.choice(string.ascii_lowercase))
        if use_digits:
            password.append(random.choice(string.digits))
        if use_symbols:
            password.append(random.choice('!@#$%^&*()_+-=[]{}|;:,.<>?'))
        
        # Заполняем остальные символы
        for _ in range(length - len(password)):
            password.append(random.choice(chars))
        
        # Перемешиваем
        random.shuffle(password)
        
        return ''.join(password)
