# flask_app
Установка virtualenv
pip install virtualenv

Создание виртуалки
python -m virtualenv env

Активация 
env\Scripts\activate.bat

Скачать фласк
pip install flask

Установим restful
pip install flask-restful 

Установим sqlalchemy и migrate
install flask-sqlalchemy 
pip install flask-migrate 

config.py должен быть в корне проекта

Создать репозиторий миграций
flask db init

Создать директорию data для базы данных

в фале init добавить models
from . import routes, models

Можно начинать миграцию
flask db migrate -m "add film model"

Применяем миграцию
flask db upgrade


Для пост запроса пишем команду в повершел
$url = 'http://localhost:5000/films'
$data = '{  "title": "Ready Play", 
            "release_date": "November 3, 2016", 
            "rating": 7.5, 
            "description": "fignya opisanie", 
            "length": 140, 
            "distributed_by": "Warner Bros" }'
Invoke-RestMethod $url -Method Post -Body $data -ContentType 'application/json'

Для обновления
$url = 'http://localhost:5000/films/81ea788e-b82e-4821-843c-637b0eb51fae'
$data = '{  "title": "Ready Play New" }'
Invoke-RestMethod $url -Method Patch -Body $data -ContentType 'application/json'

Для обновления всех строк PUT 
$url = 'http://localhost:5000/films/81ea788e-b82e-4821-843c-637b0eb51fae'
$data = '{  "title": "Ready Play Patch", 
            "release_date": "November 3, 2016", 
            "rating": 7.5, 
            "description": "fignya opisanie", 
            "length": 140, 
            "distributed_by": "Warner Bros" }'
Invoke-RestMethod $url -Method Put -Body $data -ContentType 'application/json'

Для удаления Delete
$url = 'http://localhost:5000/films/81ea788e-b82e-4821-843c-637b0eb51fae'
Invoke-RestMethod $url -Method Delete -Body $data -ContentType 'application/json'