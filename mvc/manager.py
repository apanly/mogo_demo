# -*- coding: utf-8 -*-
from application import app,manager
from flask_script import Server
from jobs.launcher import runJob
from www import *

##web server
manager.add_command('runserver', Server( host='0.0.0.0', port = app.config.get('SERVER_PORT'), use_debugger=True) )

#job entrance
manager.add_command('runjob', runJob() )


@manager.command
def testCommand():
    app.logger.info( "test command" )

def main():
    manager.run()

if __name__ == '__main__':
    try:
        import sys
        sys.exit( main() )
    except Exception as e:
        app.logger.info( e )

__all__ = []