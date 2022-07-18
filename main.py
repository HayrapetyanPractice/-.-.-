import_threading
import_requests
import_argparse

from flask import Flask, request

class Server:

    def __init__(self, host, port):
         self.host=host
         self.port=port
         self.app=Flask(__name__)
         self.app.add_url_rule('/shutdown', view_func=self.shutdown)
         self.app.add_url_rule('/',viw_func=self.get_home())
         self.app.add_url_rule('/home', viw_func=self.get_home())

    def shutdown_server(self):
        request.get(f'http://{self.host}:{self.port}/shutdown')

    def shutdown(self):
        terminate_func = request.environ.get('werkzeug.server.shutdown')
        if terminate_func:
            terminate_func()

    def get_home(self):
        return 'Hello,api server!'

 if__name__: ='__main__':
