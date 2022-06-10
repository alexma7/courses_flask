


 [Настройка окружения](#Настройка_окружения)

Создание виртуалки venv (имя произвольное)
```
python -m venv env 
```

Активация 
```
.\env\Scripts\activate.bat
```

Скачать все нужные пакеты можно поместив их в файл. В нашем примере путь ```.\.vscode\requirements\requirements.txt```. Пакеты указываем простым перечисленим одна строка один пакет \
Далее можно использовать команду ```pip install``` с ключом ```-r``` и путем до нашего файла. Запустится установка нужных нам пакетов.

Проверка интерпритатора
```
Ctrl+Shift+P -> Python Select Interpreter
```




config.py  должен быть в корне проекта

[Настройка БД](#Настройка_БД)

Описываем таблицы в классе главного файла
```
class Airports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String)
    name = db.Column(db.String)
    country = db.Column(db.String)
    city = db.Column(db.String) 
    length = db.Column(db.Integer)
```    
Создать репозиторий миграций, что бы появилась папка migration
```
flask db init
```

Создает файл в котором описаны миграции
```
# надо вствить этот год в главный файл, что бы db migrate не выводил ошибку
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# А это, что бы мы могли видеть сконфигурированный запрос
app.config['SQLALCHEMY_ECHO'] = True

# после пишем в консоли...
flask db migrate 
```

После это можно создать файл и провести миграцию
```
flask db upgrade
```

Если у нас будут какие-то изменения в структуре таблицы, то после изменения класса, надо сделать опять migrate и upgrate

Для добавления данных в таблицу прописываем все поля в класс с наименованием столбцов таблицы. Далее открываем сессию и добавляем. А в конце комитим, что бы данные подтвердились.
```
ADL = Airports(code='ADL', name='Adelali in', country='Australia', city='Adelaide', length=10171)     
db.session.add(ADL)
db.session.commit()
```

Получить поля 
```
airport = db.session.query(Airports).get_or_404(2)
print(airport.id, airport.name)
```

Обновить поля
Простое обновлени, мы пожем взять наше поле из селекта и просто поменять любой столбце. Сессия у нас открыта, поэтому заново открывать ее не надо. В самом конце делаем комит.
```
airport.name = 'New name'
db.session.commit()
```

Массловое обновление через словарь
```
airport = db.session.query(Airports).filter(Airports.country == 'Russia').update({'length': Airports.length+100})
db.session.commit()
```

Удалить строку
```
airport = db.session.query(Airports).filter(Airports.id == 2).delete()
db.session.commit()
```
Создать директорию data для базы данных

в фале init добавить models
```
from . import routes, models
```

Можно начинать миграцию
```
flask db migrate -m "add film model"
```
Применяем миграцию
```
flask db upgrade
```

Для пост запроса пишем команду в повершел
```
$url = 'http://localhost:5000/films'
$data = '{  "title": "Ready Play", 
            "release_date": "November 3, 2016", 
            "rating": 7.5, 
            "description": "fignya opisanie", 
            "length": 140, 
            "distributed_by": "Warner Bros" }'
Invoke-RestMethod $url -Method Post -Body $data -ContentType 'application/json'
```
<a name="Настройка_окружения"></a> 
Для обновления
```
$url = 'http://localhost:5000/films/81ea788e-b82e-4821-843c-637b0eb51fae'
$data = '{  "title": "Ready Play New" }'
Invoke-RestMethod $url -Method Patch -Body $data -ContentType 'application/json'
```

Для обновления всех строк PUT 
```
$url = 'http://localhost:5000/films/81ea788e-b82e-4821-843c-637b0eb51fae'
$data = '{  "title": "Ready Play Patch", 
            "release_date": "November 3, 2016", 
            "rating": 7.5, 
            "description": "fignya opisanie", 
            "length": 140, 
            "distributed_by": "Warner Bros" }'
Invoke-RestMethod $url -Method Put -Body $data -ContentType 'application/json'
```
Для удаления Delete
```
$url = 'http://localhost:5000/films/81ea788e-b82e-4821-843c-637b0eb51fae'
Invoke-RestMethod $url -Method Delete -Body $data -ContentType 'application/json'
```



