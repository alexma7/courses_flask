import flask
from models import db, migrate, admin
from register.views import register_blueprint
from display.views import display_blueprint


app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '1234'
db.init_app(app)
migrate.init_app(app, db)
admin.init_app(app)


app.register_blueprint(register_blueprint)
app.register_blueprint(display_blueprint)


if __name__ == '__main__': 
    app.run(debug=True)