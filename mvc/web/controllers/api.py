# -*- coding: utf-8 -*-
from flask import Blueprint,request
import  random
from common.models.User import User
from application import app,db

route_api = Blueprint('api_page', __name__)
@route_api.route('/')
def index():
    list = User.query.all()
    for item in list:
        app.logger.info( item.nickname )
    return 'index_list'


@route_api.route('/info')
def info():
    req = request.values
    id = int(req['id']) if 'id' in req and req['id'] else 0
    info = User.query.filter_by( uid = id ).first()
    nickname = info.nickname if info else ''
    return 'nickname:{0}'.format( nickname )


@route_api.route('/add')
def add():
    model_user = User()
    model_user.nickname = "郭大爷{0}号".format( random.randint( 600,800 ) )
    model_user.mobile = "1312332234"
    model_user.email = "guowei@mgzf.com"
    db.session.add( model_user )
    db.session.commit()
    return 'nickname:{0}'.format( model_user.nickname )


@route_api.route('/update')
def update():
    req = request.values
    id = int(req['id']) if 'id' in req and req['id'] else 0
    info = User.query.filter_by( uid = id ).first()
    info.nickname = "郭大爷{0}号".format( random.randint( 600,800 ) )
    db.session.add( info )
    db.session.commit()
    nickname = info.nickname if info else ''
    return 'nickname:{0}'.format( nickname )


@route_api.route('/del')
def delete():
    req = request.values
    id = int( req['id'] ) if 'id' in req and req['id'] else 0
    info = User.query.filter_by( uid = id ).first()
    if info:
        db.session.delete( info )
        db.session.commit()
    return "ok"
