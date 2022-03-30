import random
import flask #, request, render_template, jsonify

#from flask.wrappers import Response
#from py.prime import makePrime
#from galton import galtonboard
#import git # GitPython library
#import os

app = flask.Flask(__name__)

#Route for the GitHub webhook
# @app.route('/git_update', methods=['POST'])
# def git_update():
#   repo = git.Repo('./flask_app')
#   origin = repo.remotes.origin
#   repo.create_head('main', 
#   origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
#   origin.pull()
#   return '', 200

@app.route("/")
def main_view():
    return flask.render_template('main.html')

@app.route("/galaxies")
def galaxies_view():
    nearby_galaxies = {
        1: {"galaxy": "Карликовая галактика в Большом Псе",
            "distance_trillionkm": 241248.627051,
            "distance_ly": 25500,
            "description": "Галактика Местной группы, находящаяся в созвездии Большого Пса..."},
        2: {"galaxy": "Большое Магелланово Облако",
            "distance_trillionkm": 1542099.06703,
            "distance_ly": 163000,
            "description": "Спутник Млечного Пути, расположенная на расстоянии около 163 тыс. св. лет..."},
        3: {"galaxy": "Карликовая эллиптическая галактика в Стрельце",
            "distance_trillionkm": 662251.133081,
            "distance_ly": 70000,
            "description": "Эллиптическая галактика-спутник Млечного Пути. Проме обычного..."}
    }
    return flask.render_template('galaxies.html', nearby_galaxies=nearby_galaxies)

@app.route("/about")
def about_view():
    return flask.render_template('about.html')

@app.route("/index")
def index_view():
    night = random.random()
    return flask.render_template('index.html', night=night)

@app.route("/students")
def students_view():
    students = {
      'Петров Иван Иванович',
      'Иванов Иван Иванович',
      'Сидоров Иван Иванович',
      'Кукухин Иван Иванович',
     }
    return flask.render_template('students.html', students=students)

@app.route("/roses")
def roses_view():
    roses = {
      'Red': ['Freedom', 'Forever young', 'dfdf'],
      'White': ['dsd', 'sdsd gfds', 'fgfg'],
      'Other': ['asdf', 'gdgf young', 'dfdf'],
     }
    return flask.render_template('roses.html', roses=roses)

#1 урок
# @app.route("/about")
# def about():
#     return flask.render_template('about.html')

# @app.route("/welcome")
# def welcome():
#     weeks = 5
#     course = 'Flask'
#     group = 'ПО-09'
#     return flask.render_template(
#         'welcome.html', 
#         weeks=weeks,  
#         course=course, 
#         group=group
#     )

# @app.route('/students/<int:student_id>')
# def students(student_id):
#     students = {
#       1: 'Петров Иван Иванович',
#       2: 'Иванов Иван Иванович',
#       3: 'Сидоров Иван Иванович',
#       4: 'Кукухин Иван Иванович',
#     }
#     student_name = students.get(student_id)
#     if student_name is None:
#         flask.abort(404)
#     return flask.render_template('students.html', student_name=student_name)



if __name__ == '__main__':
  app.run(debug=True)
 
