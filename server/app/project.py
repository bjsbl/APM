from app.model import db,Project,Api
from flask import Blueprint,g,request,jsonify,flash
from flask_login import current_user,login_required
import json

project_blueprint = Blueprint("project", __name__)

@project_blueprint.route('/list')
@login_required
def list():
  page = request.form.get('page', 1, type=int)
  rows = request.form.get('rows', 10, type=int)
  pagination = Project.query.order_by(Project.lastUpdateTime).paginate(page,rows)
  listData = pagination.items
  return jsonify({'code':200,'msg':'','result':{'total': Project.query.count(),'data':[data.to_json() for data in listData]}})

@project_blueprint.route('/add', methods=['POST'])
@login_required
def add():
  res = Project()
  res.name = request.form.get('name')
  res.description = request.form.get('description')
  res.userId = 1
  res.status = 'Y'
  db.session.add(res)
  db.session.commit()
  return jsonify({'code':200,'msg':res.to_json()})

@project_blueprint.route('/del/<int:id>')
@login_required
def delete(id):
  res = Project.query.get_or_404(id)
  db.session.delete(res)
  db.session.commit()
  return jsonify({'code':200,'msg':'OK'})

@project_blueprint.route('/get/<int:id>')
@login_required
def get(id):
  res = Project.query.get_or_404(id)
  return jsonify({'code':200,'msg':'','data':res.to_json()})

@project_blueprint.route('/update/<int:id>',methods=['POST'])
@login_required
def update(id):
  res = Project.query.get_or_404(id)
  res.name = request.form.get('name')
  res.description = request.form.get('description')
  db.session.add(res)
  db.session.commit()
  return jsonify({'code':200,'msg':'OK'})
