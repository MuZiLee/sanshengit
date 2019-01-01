
#数据库配置
def get_db_uri(dbinfo):
    ENGINE = dbinfo.get("ENGINE") or 'mysql'
    DRIVER = dbinfo.get("DRIVER") or 'pymysql'
    USER = dbinfo.get("USER") or 'root'
    PASSWORD = dbinfo.get("PASSWORD") or 'root'
    HOST = dbinfo.get("HOST") or 'localhost'
    PORT = dbinfo.get("PORT") or '3306'
    NAME = dbinfo.get("NAME") or 'develop'

    return "{}+{}://{}:{}@{}:{}/{}".format(ENGINE, DRIVER, USER, PASSWORD, HOST, PORT, NAME)


# 默认配置
class Config:
    # 默认不打开debu
    DEBUT = False
    #默认不打开测试
    TESTING = False
    #默认密钥
    SECRET_KEY = 'JERRY'
    #默认SQLALCHEMY不跟踪不修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False



### 开发环境
class DevelopConfig(Config):
    ##打开dubut模式
    DEBUT = True

    DATABASE = {
        "DEGINE": 'mysql',
        "DRIVER": 'pymysql',
        "USER": 'root',
        "PASSWORD": 'jerrylee2019',
        "HOST": 'localhost',
        "PORT": '3306',
        "NAME": 'Python2019Flask01_DEBUT'
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


### 测试环境
class TestingConfig(Config):
    ##打开dubut模式
    TESTING = True

    DATABASE = {
        "DEGINE": 'mysql',
        "DRIVER": 'pymysql',
        "USER": 'root',
        "PASSWORD": 'jerrylee2019',
        "HOST": 'localhost',
        "PORT": '3306',
        "NAME": 'Python2019Flask01_TESTING'
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


### 演示环境
class StagingConfig(Config):

    DATABASE = {
        "DEGINE": 'mysql',
        "DRIVER": 'pymysql',
        "USER": 'root',
        "PASSWORD": 'jerrylee2019',
        "HOST": 'localhost',
        "PORT": '3306',
        "NAME": 'Python2019Flask01_STAGING'
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


### 生产环境
class ProductConfig(Config):

    DATABASE = {
        "DEGINE": 'mysql',
        "DRIVER": 'pymysql',
        "USER": 'root',
        "PASSWORD": 'jerrylee2019',
        "HOST": 'localhost',
        "PORT": '3306',
        "NAME": 'Python2019Flask01_PRODUCT'
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


dbinfo = {
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "default": DevelopConfig
}