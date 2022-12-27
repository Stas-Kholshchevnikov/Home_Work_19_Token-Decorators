import jwt
from flask import request, abort

from constants import SECRET, ALGO


def auth_required(func):
    """
    Декоратор на проверку наличия access токена
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            jwt.decode(token, SECRET, algorithms=ALGO)
        except Exception:
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    """
    Декоратор на проверку прав доступа пользователя
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            token_info = jwt.decode(token, SECRET, algorithms=ALGO)
        except Exception:
            abort(401)

        role = token_info.get("role")

        if role != "admin":
            abort(401)

        return func(*args, **kwargs)

    return wrapper
