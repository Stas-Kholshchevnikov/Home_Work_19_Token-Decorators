from flask_restx import abort
from dao.user import UserDAO

from constants import SECRET, ALGO
import datetime
import calendar
import jwt

from service.user import UserService


class AuthService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_token(self, data):
        """
        функция получения пары токенов
        :param data:
        :return:
        """
        user_name = data.get("username")
        password_user = data.get("password")
        try:
            user = self.dao.get_by_name(user_name)
        except Exception:
            abort(401)

        if user.password != UserService.get_hash(user, password_user):
            abort(401)

        token_data = {
            "username": user.username,
            "role": user.role
                    }

        result = self.create_token(token_data)
        return result

    def refresh_token(self, data):
        """
        Функция обновления пары токенов
        :param data:
        :return:
        """
        if "Authorization" not in data:
            abort(401)

        info_auth = data['Authorization']
        refresh_token = info_auth.split('Bearer ')[-1]

        try:
            token_info = jwt.decode(refresh_token, SECRET, algorithms=ALGO)
        except Exception:
            abort(401)

        user_name = token_info.get("username")
        user = self.dao.get_by_name(user_name)

        token_data = {
            "username": user.username,
            "role": user.role
        }

        result = self.create_token(token_data)
        return result

    def create_token(self, token_data):
        """
        Создание пары токенов
        :param token_data:
        :return:
        """
        min10 = datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
        token_data["exp"] = calendar.timegm(min10.timetuple())
        access_token = jwt.encode(token_data, SECRET, algorithm=ALGO)
        day10 = datetime.datetime.utcnow() + datetime.timedelta(days=10)
        token_data["exp"] = calendar.timegm(day10.timetuple())
        refresh_token = jwt.encode(token_data, SECRET, algorithm=ALGO)

        tokens = {
            "access_token": access_token,
            "refresh_token": refresh_token
                }

        return tokens


