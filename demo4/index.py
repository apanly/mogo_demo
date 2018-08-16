# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

from api  import route_api
app.register_blueprint(route_api, url_prefix="/api" )

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@127.0.0.1/test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBUG'] = True
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run( host='0.0.0.0' ,use_debugger = True)