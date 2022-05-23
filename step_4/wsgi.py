import code
import flask
import flask_sqlalchemy
import flask_migrate

app = flask.Flask(__name__)
# Адрес, путь, где находится БД
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///airports.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)


class Airports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String)
    name = db.Column(db.String)
    country = db.Column(db.String)
    city = db.Column(db.String) 
    length = db.Column(db.Integer)


# ADL = Airports(code='ADL', name='Adelali in', country='Australia', city='Adelaide', length=10171)    
# DUS = Airports(code='ADL', name='Dusseldorf Int', country='Germany', city='Dusseldorf', length=9842)   
# ARH = Airports(code='ARH', name='Arkhangelsk Airport', country='Russia', city='Arkhangelsk', length=8202)   
# db.session.add(ADL)
# db.session.add(DUS)
# db.session.add(ARH)

airport = db.session.query(Airports).filter(Airports.id == 2).delete()
db.session.commit()

# if  __name__ == '__main__':
#     app.run(debug=True)
