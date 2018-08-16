# -*- coding: utf-8 -*-
from application import app
import  requests

class JobTask():
    def __init__(self):
        pass

    def run( self,params ):
        url = "http://www.mgzf.com/list"
        r = requests.get( url = url )
        app.logger.info( r.text )