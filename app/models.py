from app import db

class Entry(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    owner = db.Column(db.String(20),nullable=False)
    desc = db.Column(db.String(120),nullable=True)

    def __repr__(self):
        return '<Entry {}>'.format(self.date) 
   
# class User(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.String(20))
#     password = db.Column(db.string)

#     def __repr__(self):
#         return '<User {}>'.format(self.name)
    
