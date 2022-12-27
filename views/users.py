from flask_restx import Namespace, Resource
from dao.model.user import UserSchema
from flask import request

from implemented import user_service

user_ns = Namespace("users")

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@user_ns.route("/")
class UsersView(Resource):
    """
    Обработка раздичных методов запросов на эндпоинт users
    """
    def get(self):
        result = user_service.get_all()
        return users_schema.dump(result), 200

    def post(self):
        data = request.json
        result = user_service.create(data)
        return user_schema.dump(result), 201

@user_ns.route("/<int:uid>")
class UserView(Resource):
    """
    Обработка раздичных методов запросов на эндпоинт users/*
    """
    def get(self, uid):
        result = user_service.get_one(uid)
        return user_schema.dump(result), 200

    def put(self, uid):
        data = request.json
        result = user_service.update(data, uid)
        return user_schema.dump(result), 204

    def delete(self, uid):
        user_service.delete(uid)
        return "", 204




