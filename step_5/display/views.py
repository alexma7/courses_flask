import flask


display_blueprint = flask.Blueprint('display_blueprint', __name__)


@display_blueprint.route('/display')
def display_view():
    is_login_successfull = flask.session.get('is_login_successfull', False) # получаем куки
    if is_login_successfull:
        return f'Доступ разрешен'
    return f'Доступ запрещен'
   # return 'Удалено' 
 

@display_blueprint.route('/reset')
def reset_view():
    flask.session.clear()  # удаляем куки
    return 'Удалено'     