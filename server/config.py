class BaseConfig(object):
  SECRET_KEY = '123456789'
  SQLALCHEMY_POOL_SIZE = 5
  SQLALCHEMY_POOL_TIMEOUT = 10
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_ECHO = True

class DevelopmentConfig(BaseConfig):
  DEBUG = True
  HOST = '127.0.0.1'
  USERNAME = 'root'
  PASSWORD = '1234567'
  PORT = '3306'
  DATABASE = 'AutoApi'
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOST,PORT,DATABASE)
  

class ProductionConfig(BaseConfig):
  DEBUG = True
  HOST = '192.168.245.127'
  USERNAME = 'root'
  PASSWORD = 'adminsbl'
  PORT = '3306'
  DATABASE = 'AutoApi'
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}@{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOST,PORT,DATABASE)

config = {
    'dev': DevelopmentConfig,
    'pro': ProductionConfig,
}