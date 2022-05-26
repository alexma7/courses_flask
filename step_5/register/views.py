import flask
import sqlalchemy
import werkzeug

from step_5.models import UserModel, db


register_blueprint = flask.Blueprint('register_blueprint', __name__)


@register_blueprint.route('/set', methods=['GET', 'POST'])
def set_view():
    #return 'Удалено'  
    if flask.request.method == 'GET':
        return flask.render_template('set.html')
    flask.session['name'] = flask.request.form.get('name') # записываем в куки
    return flask.redirect(flask.url_for('display_blueprint.get_auth_view')) 


@register_blueprint.route('/auth')
def get_auth_view():
     flask.session['is_login_successfull'] = True
     return flask.render_template('auth.html')


@register_blueprint.route('/auth' , methods=['POST'])
def set_auth_view():
    email = flask.request.form.get('email')
    password = flask.request.form.get('password')
    user = db.session.query(UserModel).filter_by(email=email).first()
    if user is not None and werkzeug.security.check_password_hash(user.password, password):
        flask.session['is_login_successfull'] = True
        return 'Успешная авторизация'
    return 'Неправильный логин или пароль'


@register_blueprint.route('/register')
def get_register_view():
     return flask.render_template('register.html')


@register_blueprint.route('/register' , methods=['POST'])
def post_register_view():
    email = flask.request.form.get('email')
    password = flask.request.form.get('password')
    name = flask.request.form.get('name')
    password_hash = werkzeug.security.generate_password_hash(password)
    user = UserModel(email=email, password=password_hash, name=name)
    
    db.session.add(user)
    try:
        db.session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        return 'Такой пользователь уже есть'
    return flask.redirect(flask.url_for('register_blueprint.get_auth_view'))