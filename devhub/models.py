from devhub import db

class User(db.Model):
    """ User model """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    username = db.Column(db.string(25), unique=True, nullable=False)
    password = db.Column(db.string, nullable=False)

    def __repr__(self):
        return self