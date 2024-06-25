from app import db

class Customer(db.Model):
    __tablename__ ="customers"
    pid = db.Column("id", db.Integer, primary_key=True)
    firstname=db.Column(db.Text)
    lastname=db.Column(db.Text)
    email=db.Column(db.String)
    phone=db.Column(db.String)
    address=db.Column(db.String)
    active=db.Column(db.Boolean)

    
    def __repr__(self):
        return f'Customer {self.firstname} {self.lastname}, ID {self.pid}'