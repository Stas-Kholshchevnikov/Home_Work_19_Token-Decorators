import base64

from dao.user import UserDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
import hashlib


class UserService:
    """
    Сервис для обработки операци над таблицей user
    """
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        """
        Функция получения одной записи
        :param uid:
        :return:
        """
        return self.dao.get_one(uid)

    def get_all(self):
        """
        Функция получения всех записей
        :return:
        """
        return self.dao.get_all()

    def create(self, data):
        """
        Функция создания записи
        :param data:
        :return:
        """
        data["password"] = self.get_hash(data["password"])
        return self.dao.create(data)

    def update(self, data, uid):
        """
        Функция обновления данных записи
        :param data:
        :param uid:
        :return:
        """
        try:
            data["password"] = self.get_hash(data["password"])
        except Exception:
            pass
        return self.dao.update(data, uid)

    def delete(self, uid):
        """
        Функция удаления записи
        :param uid:
        :return:
        """
        return self.dao.delete(uid)

    def get_hash(self, password):
        """
        Функция получения хеша пароля
        :param password:
        :return:
        """
        password_digit = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('UTF-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(password_digit)

