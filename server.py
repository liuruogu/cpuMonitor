import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import time
import os

# Get the path to the templates and statics files
settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )
class WSHandler(tornado.websocket.WebSocketHandler):

    #open websocket connection
    def open(self):
        print ('New connection')

    #Handling incoming messages
    def on_message(self, message):
        print ('Message received from the clients:  %s' % message)
        #Send message back to client
        self.write_message("Current CPU usage is %s " % message)

    # Close websocket connection
    def on_close(self):
        self.close()
        print ('connection closed')

    def check_origin(self, origin):
        return True

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html" )

application = tornado.web.Application([
    (r'/webservices/cpu/', WSHandler),
    (r'/webservices/gui/', MainHandler ),

],**settings)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8080)
    myIP = socket.gethostbyname(socket.gethostname())
    print ('*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start()