# -*- coding: utf-8 -*-

from application import app

@app.errorhandler(404) #捕获应用的异常
def error_404(e):
    return "很抱歉！,您访问的页面不存在 ~~",404

@app.errorhandler(500) #捕获应用的异常
def error_500(e):
    return "服务器错误",500

@app.errorhandler(502) #捕获应用的异常
def error_502(e):
    return "服务器错误",502


