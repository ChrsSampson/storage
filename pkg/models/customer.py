from app import db

class Customer():
    __tablename__ ="customers"
    id = db.Column(db.Integer, primary_key=True)
    firstname=db.Column(db.Text)
    lastname=db.Column(db.Text)
    email=db.Column(db.String)
    phone=db.Column(db.String)