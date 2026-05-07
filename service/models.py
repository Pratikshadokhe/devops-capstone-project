from service import db

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(63))
    email = db.Column(db.String(63))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }