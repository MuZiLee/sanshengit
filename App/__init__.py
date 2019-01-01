from flask import Flask

from App.ext import init_ext
from App.settings import dbinfo
from App.views import init_first_blue


def create_app():
    #初始化App
    app = Flask(__name__)

    #添加数据库配置
    app.config.from_object(dbinfo.get("develop"))

    #初始化蓝图 路由
    init_first_blue(app)

    #初始化第三方库：数据库
    init_ext(app)


    return app

