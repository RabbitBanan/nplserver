# фреймоворк FLASK
from flask import Flask
# работа с БД
from flask_sqlalchemy import SQLAlchemy

# Настройка фрейворка
app = Flask(__name__)
# строка полдключения к БД
app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:Rabbit8902@localhost:5432/nlpdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# для работы post, get запросов
app.config['SECRET_KEY'] = '00f2b1ead3a0990b818517356cb40280'

# модули, где используется представление
from app import nlpbot
from app import view



