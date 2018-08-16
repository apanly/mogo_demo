# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

from api  import route_api
app.register_blueprint(route_api, url_prefix="/api" )


if __name__ == '__main__':
    app.run( host='0.0.0.0' )