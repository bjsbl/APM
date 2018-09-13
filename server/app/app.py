import time,logging
from flask import Flask,request,g
from flask_sqlalchemy import SQLAlchemy
import sys
sys.path.append('..')
from config import config
from api import api_blueprint
from member import member_blueprint
from case import case_blueprint

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(config['dev'])
db = SQLAlchemy(app)

from project import project_blueprint
app.register_blueprint(project_blueprint,url_prefix='/project')
app.register_blueprint(api_blueprint,url_prefix='/api')
app.register_blueprint(member_blueprint,url_prefix ='/member')
app.register_blueprint(case_blueprint,url_prefix ='/case')


@app.before_request
def before_request():
  g.startTime = time.time()

@app.after_request
def after_request(response):
  data={
    'status_code':response.status_code,
    'method':request.method,
    'ip': request.headers.get('X-Real-Ip', request.remote_addr),
    'url': request.url,
    'referer': request.headers.get('Referer'),
    'agent': request.headers.get('User-Agent'),
    'TimeInterval': '%0.2fs' %float(time.time() - g.startTime)
  }
  logger.info(data)
  return response

if __name__ == '__main__':
  db.init_app(app)
  app.run(debug=True)