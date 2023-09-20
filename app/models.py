from app import db # импорт из папки app 

class Entry(db.Model): #сущность Записи
    id = db.Column(db.Integer,primary_key=True)  #поля таблицы
    date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(10),nullable=False,server_default='CONFIRMED_STATUS')
    owner = db.Column(db.String(20),nullable=False)
    desc = db.Column(db.String(120),nullable=True)

    def __repr__(self):   #для печати класса в стандартном виде (аля toString())
        return '<Entry {}>'.format(self.date) 
   
class User(db.Model): #Сущность Юзеры
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    password = db.Column(db.String(20))
    token = db.Column(db.String(20))
    
    
    def __repr__(self):
        return '<User {}>'.format(self.name)
    
class Post(db.Model): #Сущность постов
    id = db.Column(db.Integer,primary_key=True)
    titul = db.Column(db.String(20),nullable=False)
    postText = db.Column(db.String(300),nullable=False)
    videoUrl = db.Column(db.String(100))
    createData = db.Column(db.DateTime , nullable= False)
    updateData = db.Column(db.DateTime , nullable = False)
    user = db.Column(db.String(20))

    def __repr__(self):
        return '<Post {}>'.format(self.titul)