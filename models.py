from app import db

class User(db.Model):
    id = db.Column(db.Integer, Primary_key= True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
