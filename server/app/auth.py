# coding:utf-8
from app.model import db,User
from flask import Blueprint,g,request,jsonify
from flask_login import login_user,logout_user,login_required
import hashlib
from . import login_manager

auth = Blueprint("auth", __name__)

@auth.route('/login',methods = ['POST'])
def login():
  user = User.query.filter_by(username=request.form.get('username')).first()
  if user is not None:
    md = hashlib.md5()
    md.update(request.form.get('password').encode('utf-8'))
    if md.hexdigest() == user.password:
      login_user(user)
      return jsonify({'code':200,'msg':''})
    return jsonify({'code':100,'msg':'密码错误'})
  return jsonify({'code':100,'msg':'未找到用户'})

@auth.route('/logout',methods = ['GET'])
@login_required
def logout():
  logout_user()
  return jsonify({'code':200,'msg':''})


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(id == user_id).first()


  