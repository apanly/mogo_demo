# -*- coding: utf-8 -*-
from application import app

from web.api  import route_api
from web.index  import route_index
app.register_blueprint(route_api, url_prefix="/api" )
app.register_blueprint(route_index, url_prefix="/" )