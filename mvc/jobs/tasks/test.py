# -*- coding: utf-8 -*-
from application import app

class JobTask():
    def __init__(self):
        pass

    def run( self , params ):
       app.logger.info( "it's over ~~" )