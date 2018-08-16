# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/api')
def index():
    return 'Index Page'


@app.route('/api/hello')
def hello():
    return 'Hello World'


if __name__ == '__main__':
    app.run( host='0.0.0.0' )