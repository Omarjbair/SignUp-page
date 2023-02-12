from app import db


class Signup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(30), nullable=False)

    # def __repr__(self):
    #     return f"name:{self.name} email:{self.email} password:{self.password}"
