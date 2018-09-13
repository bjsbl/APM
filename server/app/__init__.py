from flask import Flask,request,g,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cache import Cache
from config import config
import time,logging
from logging.handlers import RotatingFileHandler
from app.model import db
from flask_login import LoginManager,current_user

cache = Cache()
login_manager = LoginManager()
login_manager.session_protection='strong'

def create_log(log_level):
  logging.basicConfig(level=log_level)
  file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
  formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
  file_log_handler.setFormatter(formatter)
  logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):
    create_log(logging.INFO)
    logger = logging.getLogger(__name__)
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    # cache.init_app(app,{'CACHE_TYPE':'simple'})
    login_manager.init_app(app)

    from app.project import project_blueprint
    from app.api import api_blueprint
    from app.member import member_blueprint
    from app.case import case_blueprint
    from app.auth import auth
    
    app.register_blueprint(auth,url_prefix='/auth')
    app.register_blueprint(project_blueprint,url_prefix='/project')
    app.register_blueprint(api_blueprint,url_prefix='/api')
    app.register_blueprint(member_blueprint,url_prefix ='/member')
    app.register_blueprint(case_blueprint,url_prefix ='/case')
  
    @app.errorhandler(404)
    def not_found404(err):
      return jsonify({'code':0,'msg':'data not found'})

    @app.before_request
    def before_request():
      g.startTime = time.time()

    @app.after_request
    def after_request(response):
      if current_user is None:
        userId = 'GUEST'
      else:
        # userId = current_user.id
        userId = 'GUEST'
      data={
            'status_code':response.status_code,
            'method':request.method,
            'userId':userId,
            'ip': request.headers.get('X-Real-Ip', request.remote_addr),
            'url': request.url,
            'referer': request.headers.get('Referer'),
            'agent': request.headers.get('User-Agent'),
            'TimeInterval': '%0.2fs' %float(time.time() - g.startTime)
      }
      logger.info(data)
      return response
  
    return app

