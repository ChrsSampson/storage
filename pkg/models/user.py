from app import db

class User(db.Model):
    __tablename__ = "users"
    pid = db.Column("id", db.Integer, primary_key=True, nullable=False, autoincrement=True)
    username = db.Column(db.Text)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.email}, ID {self.pid}'

 