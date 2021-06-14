from app import app
from flask import request, abort
# модуль с базой данных
from app.db_pg import *
# модуль с работы файловой системой
from app.file_work import *
import random
import nltk



@app.route('/send_messages', methods=['POST', 'GET'])
def send_messages():
    # Основной метод Post
    if request.method == 'POST':
        #rint(request.form['text'])
        #data = request.json
        #if not isinstance(data, dict):
        #    return abort(400)
        #if 'name' not in data or 'text' not in data:
        #    return abort(400)
        name = request.form['name']
        text = request.form['text']
        if not isinstance(name, str) or not isinstance(text, str):
            abort(400)
        if name == '' or text == '':
            abort(400)
    # Метод Get для тестирования
    else:
        text = request.args.get('text')
        name = request.args.get('name')
        if not isinstance(name, str) or not isinstance(text, str):
           abort(400)
        if name == '' or text == '':
           abort(400)
    # Начинается распознование
    answer = bot(name, text)
    # записываем входной запрос и результат распознование в БД
    create_discernment(name, text, answer)
    return {
        'answer': answer
    }

#NLP
def clear_phrase(phrase):
    phrase = phrase.lower()
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя- '
    result = ''.join(symbol for symbol in phrase if symbol in alphabet)
    return result

def classify_intent(data_set ,replica):
    replica = clear_phrase(replica)
    distances = []
    intents = []
    for intent, intent_data in data_set['intents'].items():
        for example in intent_data['examples']:
            example = clear_phrase(example)
            # Растояние Левештейна
            distance = nltk.edit_distance(replica, example)
            # print(intent, distance / len(example))
            if example and distance / len(example) < 0.4:
                distances.append(str(distance / len(example)))
                intents.append(intent)
    if distances:
        return intents[distances.index(str(min(distances)))]

def get_answer_by_intent(data_set,intent):
    if intent in data_set['intents']:
        responses = data_set['intents'][intent]['responses']
        return random.choice(responses)

def get_failure_phrase(data_set):
    failure_phrases = data_set['failure_phrases']
    return random.choice(failure_phrases)


def bot(nlp, replica):
    data_set=write_json(select_path_tematika(int(nlp)))
    # NLU
    if (int(nlp) == 1):
        # Без МО
        intent = classify_intent(data_set,replica)
    else:
        # MO
        pass
    # выбор заготовленной реплики
    if intent:
        answer = get_answer_by_intent(data_set,intent)
        if answer:
            return answer
    # берем заглушку
    return get_failure_phrase(data_set)

