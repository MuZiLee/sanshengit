import uuid

from flask import Blueprint, render_template

from App.ext import db
from App.models import HomeItems

blue = Blueprint("first_blue", __name__)

def init_first_blue(app):
    app.register_blueprint(blueprint=blue)






@blue.route("/")
def add_persion():

    #人事部
    hr = HomeItems()
    hr.i_icon = "http://g.hiphotos.baidu.com/image/h%3D300/sign=f6a79e887f0e0cf3bff748fb3a44f23d/adaf2edda3cc7cd9ebe507433401213fb90e915b.jpg"
    hr.i_id = uuid.uuid4()
    hr.i_title = "人事部"



    #业务部
    sd = HomeItems()
    sd.i_icon = "http://g.hiphotos.baidu.com/image/h%3D300/sign=f6a79e887f0e0cf3bff748fb3a44f23d/adaf2edda3cc7cd9ebe507433401213fb90e915b.jpg"
    sd.i_id = uuid.uuid4()
    sd.i_title = "业务部"




    #账务部
    ac = HomeItems()
    ac.i_icon = "http://g.hiphotos.baidu.com/image/h%3D300/sign=f6a79e887f0e0cf3bff748fb3a44f23d/adaf2edda3cc7cd9ebe507433401213fb90e915b.jpg"
    ac.i_id = uuid.uuid4()
    ac.i_title = "账务部"

    group = [hr, sd, ac]

    # db.session.add(group)
    # db.session.commint()

    return "Hello flask"

@blue.route("/additem/")
def add_item():
    item = HomeItems();

    item.i_title = "环保部 %d" % float
    item.i_icon = float


    db.session.add(item)
    db.session.commit()

    return "Add Item Success"

@blue.route("getItems")
def get_items():
    items = HomeItems.query.all()

    return render_template("ItemList.html",items = items)