from datetime import datetime

from typing import List
from flask import request
from flask_restful import Resource

from src import api, db
from src.models import Film

class Smoke(Resource):
    def get(self):
        return {"message": "Ok111"}, 200




class FilmListApi(Resource):
    def get(self, uuid=None):
        if not uuid:
            films = db.session.query(Film).all()
            return [f.to_dict() for f in films], 200
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return '', 404
        return film.to_dict(), 200

    def post(self):
        #return request.json
        film_json = request.json
        if not film_json:
            return {'message': 'Wrong data11'}, 400
        try:
            film = Film(
                title=film_json['title'],
                release_date=datetime.strptime(film_json['release_date'], '%B %d, %Y'),
                distributed_by=film_json['distributed_by'],
                description=film_json.get('description'),
                length=film_json.get('length'),
                rating=film_json.get('rating')
            )
            db.session.add(film)
            db.session.commit()
        except (ValueError, KeyError):
            return {'message': 'Wrong data'}, 400
        return {'message': 'Created successfull'}, 201

    def put(self, uuid):
        film_json = request.json
        if not film_json:
            return {'message': 'Wrong data'}, 400
        try:
            db.session.query(Film).filter_by(uuid=uuid).update(
                dict(
                    title=film_json['title'],
                    release_date=datetime.strptime(film_json['release_date'], '%B %d, %Y'),
                    distributed_by=film_json['distributed_by'],
                    description=film_json.get('description'),
                    length=film_json.get('length'),
                    rating=film_json.get('rating')
                )
            )


            db.session.commit()
        except (ValueError, KeyError):
            return {'message': 'Wrong data'}, 400
        return {'message': 'Update successfull'}, 200

    def patch(self, uuid):
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return '', 404
        film_json = request.json
        title=film_json.get('title')
        release_date=datetime.strptime(film_json.get('release_date'), '%B %d, %Y') if film_json.get('release_date') else None,
        distributed_by=film_json.get('distributed_by')
        description=film_json.get('description')
        length=film_json.get('length')
        rating=film_json.get('rating')
        if title:
            film.title = title
        elif release_date:
            film.release_date = release_date
        elif distributed_by:
            film.distributed_by = distributed_by
        elif description:
            film.description = description
        elif length:
            film.length = length
        elif rating:
            film.rating = rating

        db.session.add(film)
        db.session.commit()
        return {'message': 'Update successfull'}, 200
        

    def delete(self, uuid):
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return '', 404
        db.session.delete(film)
        db.session.commit()
        return '', 204


class ActorListApi(Resource):
    def get(self, uuid=None):
        if not uuid:
            pass
        pass

    def post(self):
        pass

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass


api.add_resource(Smoke, '/smoke', strict_slashes=False)
api.add_resource(FilmListApi, '/films', '/films/<uuid>', strict_slashes=False)