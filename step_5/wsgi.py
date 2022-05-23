import flask
import flask_sqlalchemy
import flask_migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '1234'
db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)
admin = Admin(app)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)


admin.add_view(ModelView(UserModel, db.session))


@app.route('/set')
def set_view():
    if flask.request.method == 'GET':
        return flask.render_template('set.html')

    flask.session['test_task'] = 'mavar' # записываем в куки
    return flask.redirect(flask.url_for('display_view'))

@app.route('/display')
def display_view():
    test_task = flask.session.get('test_task', 'Not found') # получаем куки
    return test_task

@app.route('/reset')
def reset_view():
    flask.session.pop('test_task', None)  # удаляем куки
    return 'Удалено'      


if __name__ == '__main__':
    app.run(debug=True)