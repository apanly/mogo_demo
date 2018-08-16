# -*- coding: utf-8 -*-
from flask import Blueprint
route_api = Blueprint('api', __name__)
@route_api.route('/')
def index():
    return 'Index Page'


@route_api.route('/hello')
def hello():
    return 'Hello World'
