import os

basedir = os.path.abspath(os.path.dirname(__file__)) #дл опредления местоположения

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')  #проверка на наличае файла , либо его создание
    SQLALCHEMY_TRACK_MODIFICATIONS = False