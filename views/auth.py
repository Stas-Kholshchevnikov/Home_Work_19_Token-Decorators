from flask_restx import Resource, Namespace
from flask import request
from implemented import auth_service

auth_ns = Namespace("auth")


@auth_ns.route("/")
class AuthView(Resource):
    def post(self):
        data = request.json
        result = auth_service.get_token(data)
        return result

    def put(self):
        data = request.headers
        result = auth_service.refresh_token(data)
        return result
