from flask_restx import Resource, Namespace
from flask import request
from service.decorators import auth_required, admin_required

from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    """
    Обработка раздичных методов запросов на эндпоинт genre
    """
    @auth_required
    def get(self):
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        data = request.json
        result = genre_service.create(data)
        return genre_schema.dump(result), 201


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    """
    Обработка раздичных методов запросов на эндпоинт genre/*
    """
    @auth_required
    def get(self, rid):
        r = genre_service.get_one(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, rid):
        data = request.json
        result = genre_service.update(data)
        return genre_schema.dump(result), 204

    @admin_required
    def delete(self, rid):
        genre_service.delete(rid)
        return "", 204
