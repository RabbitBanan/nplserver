from app import db
import hashlib
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    first_name = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"<user {self.id}>"

class Tematika(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(500), nullable=True)
    type_discernment = db.Column(db.String(50), nullable=True)
    path = db.Column(db.String(500), unique=True)
    # Foreign Key
    creater = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"<tematika {self.id}>"

class Discernment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_discernment = db.Column(db.DateTime, default=datetime.utcnow())
    input_data = db.Column(db.String(500), nullable=True)
    result = db.Column(db.String(500), nullable=True)
    # Foreign Key
    tematika = db.Column(db.Integer, db.ForeignKey('tematika.id'))

    def __repr__(self):
        return f"<discernment {self.id}>"

# создание новой пользователя
def create_user(login: str, psw: str, last_name: str, first_name: str):
    try:
        hash = hashlib.md5(psw.encode()).hexdigest()
        new_user = User(
            login=login,
            psw=hash,
            last_name=last_name,
            first_name=first_name
        )
        db.session.add(new_user)
        db.session.commit()
        print("Успешно")
    except:
        print("Ошибка")
        db.session.rollback()


def edit_user(id_user: int, login: str, last_name: str, first_name: str):
    try:
        User.query.filter_by(id=id_user).update(
            {
                'login': login,
                'last_name': last_name,
                'first_name': first_name
            }
        )
        db.session.commit()
        print("Успешно")
    except:
        print("Ошибка")
        db.session.rollback()

def delete_user():
    pass

# создание новой тематики
def create_tematika(name: str, description: str, path: str, creater: int, type_discernment = 'Без МО'):
    try:

        new_tematika = Tematika (
            name=name,
            description=description,
            type_discernment=type_discernment,
            path=path,
            creater=creater
        )
        db.session.add(new_tematika)
        db.session.commit()
        print("Успешно")
    except:
        print("Ошибка")
        db.session.rollback()

# измененение тематики
def edit_tematika(id_tematika: int, name: str, description: str,  type_discernment: str):
    try:
        Tematika.query.filter_by(id=id_tematika).update(
            {
                'name': name,
                'description':description,
                'type_discernment': type_discernment
            }
        )
        db.session.commit()
        print("Успешно")
    except:
        print("Ошибка")
        db.session.rollback()

def select_path_tematika(id_tematika:int) -> str:
    return Tematika.query.get(id_tematika).path

def delete_tematika():
    pass

# создание новой записи о распозновании
def create_discernment(tematika: int, input_data: str, result:str):
    try:
        new_discernment = Discernment(
            input_data=input_data,
            result=result,
            tematika=tematika
        )
        db.session.add(new_discernment)
        db.session.commit()
        print("Успешно")
    except:
        print("Ошибка")
        db.session.rollback()

def edit_discernment():
    pass

def delete_discernment():
    pass

