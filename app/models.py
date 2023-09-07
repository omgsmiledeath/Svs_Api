from app import db # импорт из папки app 

class Entry(db.Model): #сущность Записи
    id = db.Column(db.Integer,primary_key=True)  #поля таблицы
    date = db.Column(db.DateTime, nullable=False)
    owner = db.Column(db.String(20),nullable=False)
    desc = db.Column(db.String(120),nullable=True)

    def __repr__(self):   #для печати класса в стандартном виде (аля toString())
        return '<Entry {}>'.format(self.date) 
   
class User(db.Model): #Сущность Юзеры
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    password = db.Column(db.String)

    def __repr__(self):
        return '<User {}>'.format(self.name)
    
