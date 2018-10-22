from flask import Flask, jsonify
from flask import redirect
from flask import url_for
from flask_script import Manager

from apps import recruit_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
manage = Manager(app)
app.register_blueprint(recruit_bp)

@app.route('/', methods=['GET'])
def index():
    print(app.config.get('DEBUG'))
    return 'index'

@app.route('/lagou/<int:position_id>', methods=['GET'])
def lagou(position_id):
    data = {
        'id': position_id,
        'name': '人工智能'
    }

    return jsonify(data=data)

@app.route('/redirect')
def red():
    return redirect(url_for('index'))

@app.route('/redirect/lagou')
def redirectLagou():
    return redirect(url_for('lagou', position_id=100))

if __name__ == '__main__':
    manage.run()

# from flask import Flask, jsonify
# from flask import abort
# from flask import request
# from flask_script import Manager
# from flask_mongoengine import MongoEngine
#
#
# app = Flask(__name__)
# manage = Manager(app)
# app.config['MONGODB_SETTINGS'] = {
#     'db': 'scrapydb',
#     'host': '182.61.60.153',
#     'port': 27017,
#     'username': 'cino',
#     'password': 'cino',
# }
# db = MongoEngine(app)
# app.config['DEBUG'] = True
#
# @app.route('/lagouRecruit', methods=['GET'])
# def get_lagou_recruit():
#     from models import LagouRecruit
#
#
#
#     paginate = LagouRecruit.objects.paginate(page=2, per_page=10)
#     items = paginate.items
#     total_page = paginate.pages
#     current_page = paginate.page
#     recruit_data = {
#         'newsList': items,
#         'current_page': current_page,
#         'total_page': total_page
#     }
#     return jsonify(data=recruit_data), 201
#
#
#
#
#
#
# if __name__ == '__main__':
#     manage.run()