from App.ext import db


class HomeItems(db.Model):
    i_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    i_title = db.Column(db.String(10))

    i_icon = db.Column(db.String(255))




def create_db():

    db.create_all()

    return "create db success"