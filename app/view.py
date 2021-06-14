from flask import render_template
from app import app
# модуль с базой данных
from app.db_pg import *
# модуль с работы файловой системой
from app.file_work import *

@app.route('/')
def index():
    return "Hello World!"

@app.route('/messenger', methods=['POST', 'GET'])
def calulator():
    return render_template('messenger.html')
