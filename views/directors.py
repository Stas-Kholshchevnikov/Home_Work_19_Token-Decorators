from flask_restx import Resource, Namespace
from flask import request
from service.decorators import auth_required, admin_required

from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@director_ns.route('/')
class DirectorsView(Resource):
    """
    Обработка раздичных методов запросов на эндпоинт directors
    """
    @auth_required
    def get(self):
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200
    @admin_required
    def post(self):
        data = request.json
        result = director_service.create(data)
        return director_schema.dump(result), 201


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    """
    Обработка раздичных методов запросов на эндпоинт directors/*
    """
    @auth_required
    def get(self, rid):
        r = director_service.get_one(rid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, rid):
        data = request.json
        result = director_service.update(data)
        return director_schema.dump(result), 204

    @admin_required
    def delete(self, rid):
        director_service.delete(rid)
        return "", 204


