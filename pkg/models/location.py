from app import db


class Location(db.Model):
    __tablename__ = "locations"
    pid = db.Column("id", db.Integer, primary_key=True)
    label = db.Column(db.Text)
    street_address = db.Column(db.String)
    city = db.Column(db.String)
    zip = db.Column(db.Integer)

    def __repr__(self):
        return f'Location {self.label}, ID {self.pid}'


