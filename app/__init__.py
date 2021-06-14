from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:Rabbit8902@localhost:5432/nlpdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '00f2b1ead3a0990b818517356cb40280'
db = SQLAlchemy(app)

from app import nlpbot
from app import db_pg
from app import view



