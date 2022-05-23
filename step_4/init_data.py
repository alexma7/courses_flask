import json
from wsgi import Airports, db


def seed(data):
    airports = []
    for airport_data in data:
        airport = Airports(
            code=airport_data['code'],
            name=airport_data['name'],
            country=airport_data['country'],
            city=airport_data['city'],
            length=airport_data['runway_length']
        )
        #db.session.add(airport)  #Для одиночного добавления
        airports.append(airport)
    db.session.bulk_save_objects(airports)    # используем для вставки большого кол-ва строк из файла
    db.session.commit()


def main():
    with open('.\\step_4\\airports.json') as f:
        airports = json.load(f)
    seed(airports)

if __name__ == '__main__':
    main()