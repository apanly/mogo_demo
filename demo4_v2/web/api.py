# -*- coding: utf-8 -*-
from flask import Blueprint

from common.models.User import User

route_api = Blueprint('api_page', __name__)
@route_api.route('/')
def index():
    list = User.query.all()
    for item in list:
        print( item.nickname )
    return 'index_list'


@route_api.route('/hello')
def hello():
    info = User.query.filter_by( uid = 1 ).first()
    nickname = info.nickname if info else ''
    return 'nickname:{0}'.format( nickname )
