from flask_login import UserMixin,AnonymousUserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Api(db.Model):
    __tablename__ = 'Api'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    status = db.Column(db.String(1))
    description = db.Column(db.String(200))
    createTime = db.Column(db.DateTime, nullable=False)
    lastUpdateTime = db.Column(db.DateTime, nullable=False)
    userId = db.Column(db.Integer)
    projectId = db.Column(db.Integer)
    method = db.Column(db.String(255))
    httpType = db.Column(db.String(255))
    url = db.Column(db.String(255))

    def to_json(self):
        return{
        'id':self.id,
        'name':self.name,
        'status':self.status,
        'description':self.description,
        'createTime':self.createTime,
        'lastUpdateTime':self.lastUpdateTime,
        'projectId':self.projectId,
        'method':self.method,
        'httpType':self.httpType,
        'url':self.url
        }


class ApiHead(db.Model):
    __tablename__ = 'ApiHead'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    value = db.Column(db.String(1))
    projectId = db.Column(db.ForeignKey('Project.id'), index=True)

    Project = db.relationship('Project', primaryjoin='ApiHead.projectId == Project.id', backref='api_heads')

    def to_json(self):
        return{
        'id':self.id,
        'name':self.name,
        'value':self.status,
        'projectId':self.projectId
        }


class ApiParameter(db.Model):
    __tablename__ = 'ApiParameter'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    value = db.Column(db.String(1000))
    type = db.Column(db.String(100))
    required = db.Column(db.String(1), nullable=False)
    projectId = db.Column(db.ForeignKey('Project.id'), index=True)

    Project = db.relationship('Project', primaryjoin='ApiParameter.projectId == Project.id', backref='api_parameters')

    def to_json(self):
        return{
        'id':self.id,
        'name':self.name,
        'value':self.value,
        'type':self.type,
        'required':self.required,
        'projectId':self.projectId
        }


class ApiResponse(db.Model):
    __tablename__ = 'ApiResponse'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    value = db.Column(db.String(1000))
    description = db.Column(db.String(200))
    type = db.Column(db.String(100), nullable=False)
    projectId = db.Column(db.ForeignKey('Project.id'), index=True)

    Project = db.relationship('Project', primaryjoin='ApiResponse.projectId == Project.id', backref='api_responses')

    def to_json(self):
        return{
        'id':self.id,
        'name':self.name,
        'value':self.value,
        'description':self.description,
        'createTime':self.createTime,
        'type':self.type,
        'projectId':self.projectId
        }


class Project(db.Model):
    __tablename__ = 'Project'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    status = db.Column(db.String(1))
    description = db.Column(db.String(200))
    createTime = db.Column(db.DateTime, nullable=False)
    lastUpdateTime = db.Column(db.DateTime, nullable=False)
    userId = db.Column(db.ForeignKey('User.id'), index=True)

    User = db.relationship('User', primaryjoin='Project.userId == User.id', backref='projects')

    def to_json(self):
        return{
        'id':self.id,
        'name':self.name,
        'status':self.status,
        'description':self.description,
        'createTime':self.createTime,
        'lastUpdateTime':self.lastUpdateTime,
        'userId':self.userId
        }


class ProjectCase(db.Model):
    __tablename__ = 'ProjectCase'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    status = db.Column(db.String(1))
    description = db.Column(db.String(200))
    createTime = db.Column(db.DateTime, nullable=False)
    lastUpdateTime = db.Column(db.DateTime, nullable=False)
    userId = db.Column(db.ForeignKey('User.id'), index=True)
    hostId = db.Column(db.ForeignKey('ProjectHost.id'), index=True)

    ProjectHost = db.relationship('ProjectHost', primaryjoin='ProjectCase.hostId == ProjectHost.id', backref='project_cases')
    User = db.relationship('User', primaryjoin='ProjectCase.userId == User.id', backref='project_cases')

    def to_json(self):
        return{
        'id':self.id,
        'name':self.name,
        'status':self.status,
        'description':self.description,
        'createTime':self.createTime,
        'lastUpdateTime':self.lastUpdateTime,
        'userId':self.userId,
        'hostId':self.hostId
        }


class ProjectCaseApi(db.Model):
    __tablename__ = 'ProjectCaseApi'

    id = db.Column(db.Integer, primary_key=True)
    ApiId = db.Column(db.ForeignKey('Api.id'), index=True)
    timeout = db.Column(db.Float(10))
    description = db.Column(db.String(200))
    createTime = db.Column(db.DateTime, nullable=False)
    lastUpdateTime = db.Column(db.DateTime, nullable=False)
    userId = db.Column(db.ForeignKey('User.id'), index=True)

    Api = db.relationship('Api', primaryjoin='ProjectCaseApi.ApiId == Api.id', backref='project_case_apis')
    User = db.relationship('User', primaryjoin='ProjectCaseApi.userId == User.id', backref='project_case_apis')

    def to_json(self):
        return{
        'id':self.id,
        'ApiId':self.ApiId,
        'timeout':self.timeout,
        'description':self.description,
        'createTime':self.createTime,
        'lastUpdateTime':self.lastUpdateTime,
        'userId':self.userId
        }


class ProjectCaseResult(db.Model):
    __tablename__ = 'ProjectCaseResult'

    id = db.Column(db.Integer, primary_key=True)
    caseId = db.Column(db.ForeignKey('ProjectCase.id'), index=True)
    httpStatus = db.Column(db.String(10))
    httpResponse = db.Column(db.Text(collation='utf8_bin'))
    createTime = db.Column(db.DateTime, nullable=False)
    costTime = db.Column(db.Float(10))

    ProjectCase = db.relationship('ProjectCase', primaryjoin='ProjectCaseResult.caseId == ProjectCase.id', backref='project_case_results')

    def to_json(self):
        return{
        'id':self.id,
        'caseId':self.caseId,
        'httpStatus':self.httpStatus,
        'httpResponse':self.httpResponse,
        'createTime':self.createTime,
        'costTime':self.costTime
        }


class ProjectHost(db.Model):
    __tablename__ = 'ProjectHost'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    host = db.Column(db.String(15))
    status = db.Column(db.String(1))
    description = db.Column(db.String(200))
    createTime = db.Column(db.DateTime, nullable=False)
    lastUpdateTime = db.Column(db.DateTime, nullable=False)
    userId = db.Column(db.ForeignKey('User.id'), index=True)

    User = db.relationship('User', primaryjoin='ProjectHost.userId == User.id', backref='project_hosts')

    def to_json(self):
        return{
        'id':self.id,
        'name':self.name,
        'status':self.status,
        'description':self.description,
        'createTime':self.createTime,
        'lastUpdateTime':self.lastUpdateTime,
        'host':self.host
        }


class ProjectLog(db.Model):
    __tablename__ = 'ProjectLog'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    status = db.Column(db.String(1))
    description = db.Column(db.String(200))
    createTime = db.Column(db.DateTime, nullable=False)
    lastUpdateTime = db.Column(db.DateTime, nullable=False)
    userId = db.Column(db.Integer)

    def to_json(self):
        return{
        'id':self.id,
        'name':self.name,
        'status':self.status,
        'description':self.description,
        'createTime':self.createTime,
        'lastUpdateTime':self.lastUpdateTime,
        'userId':self.userId
        }


class ProjectMember(db.Model):
    __tablename__ = 'ProjectMember'

    id = db.Column(db.Integer, primary_key=True)
    projectId = db.Column(db.ForeignKey('Project.id'), index=True)
    memberId = db.Column(db.ForeignKey('User.id'), index=True)
    roleId = db.Column(db.ForeignKey('Role.id'), index=True)
    createTime = db.Column(db.DateTime, nullable=False)

    User = db.relationship('User', primaryjoin='ProjectMember.memberId == User.id', backref='project_members')
    Project = db.relationship('Project', primaryjoin='ProjectMember.projectId == Project.id', backref='project_members')
    Role = db.relationship('Role', primaryjoin='ProjectMember.roleId == Role.id', backref='project_members')

    def to_json(self):
        return{
        'id':self.id,
        'description':self.description,
        'createTime':self.createTime,
        'projectId':self.projectId,
        'memberId':self.memberId,
        'roleId':self.roleId
        }


class Role(db.Model):
    __tablename__ = 'Role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(100))
    createTime = db.Column(db.DateTime, nullable=False)

    def to_json(self):
        return{
        'id':self.id,
        'name':self.name,
        'status':self.status,
        'description':self.description,
        'createTime':self.createTime
        }


class SystemLog(db.Model):
    __tablename__ = 'SystemLog'

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50))
    userId = db.Column(db.ForeignKey('User.id'), index=True)
    remark = db.Column(db.String(200))
    createTime = db.Column(db.DateTime, nullable=False)

    User = db.relationship('User', primaryjoin='SystemLog.userId == User.id', backref='system_logs')

    def to_json(self):
        return{
        'id':self.id,
        'model':self.model,
        'userId':self.userId,
        'remark':self.remark,
        'createTime':self.createTime
        }


class User(db.Model,UserMixin):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    role_id = db.Column(db.ForeignKey('Role.id'), index=True)
    email = db.Column(db.String(50))
    realname = db.Column(db.String(50))
    createTime = db.Column(db.DateTime, nullable=False)

    role = db.relationship('Role', primaryjoin='User.role_id == Role.id', backref='users')

    def get_id(self):
        return str(self.id)
    def is_authenticated(self):
        return True
    def is_active(self): # line 37
        return True
    def is_anonymous(self):
        return False

    def to_json(self):
        return{
        'id':self.id,
        'username':self.username,
        'password':self.password,
        'role_id':self.role_id,
        'createTime':self.createTime,
        'realname':self.realname,
        'email':self.email
        }
