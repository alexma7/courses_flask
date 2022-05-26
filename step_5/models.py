from enum import unique
import flask
import flask_sqlalchemy
import flask_migrate
import werkzeug.security
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import sqlalchemy


db = flask_sqlalchemy.SQLAlchemy()
migrate = flask_migrate.Migrate()
admin = Admin()


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)


admin.add_view(ModelView(UserModel, db.session))