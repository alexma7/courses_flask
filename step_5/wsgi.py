#from crypt import methods
from enum import unique
import flask
import flask_sqlalchemy
import flask_migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import sqlalchemy


app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '1234'
db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)
admin = Admin(app)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)


admin.add_view(ModelView(UserModel, db.session))


@app.route('/set', methods=['GET', 'POST'])
def set_view():
    #return 'Удалено'  
    if flask.request.method == 'GET':
        return flask.render_template('set.html')
    flask.session['name'] = flask.request.form.get('name') # записываем в куки
    return flask.redirect(flask.url_for('display_view'))


@app.route('/auth')
def get_auth_view():
     flask.session['is_login_successfull'] = True
     return flask.render_template('auth.html')


@app.route('/auth' , methods=['POST'])
def set_auth_view():
    email = flask.request.form.get('email')
    password = flask.request.form.get('password')
    user = db.session.query(UserModel).filter_by(email=email, password=password).first()
    if user is not None:
        flask.session['is_login_successfull'] = True
        return 'Успешная авторизация'
    return 'Неправильный логин или пароль'


@app.route('/register')
def get_register_view():
     return flask.render_template('register.html')


@app.route('/register' , methods=['POST'])
def post_register_view():
    email = flask.request.form.get('email')
    password = flask.request.form.get('password')
    name = flask.request.form.get('name')
    user = UserModel(email=email, password=password, name=name)
    
    db.session.add(user)
    try:
        db.session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        return 'Такой пользователь уже есть'
    return flask.redirect(flask.url_for('get_auth_view'))



     


@app.route('/display')
def display_view():
    is_login_successfull = flask.session.get('is_login_successfull', False) # получаем куки
    if is_login_successfull:
        return f'Доступ разрешен'
    return f'Доступ запрещен'
   # return 'Удалено' 
 

@app.route('/reset')
def reset_view():
    flask.session.clear()  # удаляем куки
    return 'Удалено'      


if __name__ == '__main__':
    app.run(debug=True)