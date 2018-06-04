from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol, connectWS
import psutil
import time
import re

class EchoClientProtocol(WebSocketClientProtocol):

    # Open websocket connection
	def onConnect(self, response):
		print("Connected to Server: {}".format(response.peer))

	def onOpen(self):
		def hello():
		    # Send the its CPU usage data to the tornado server
		    self.sendMessage("CPU usages from client1: "+str(psutil.cpu_percent(interval=1)))
		    # Send the message again in 1 second
		    self.factory.reactor.callLater(1, hello)
		hello()

    # Receive the message echo back from server
	def onMessage(self, payload, isBinary):
		if isBinary:
			print("Binary message received: {0} bytes".format(len(payload)))
		else:
			print("Text message received: {0}".format(payload.decode('utf8')))

if __name__ == '__main__':
   factory = WebSocketClientFactory("ws://127.0.0.1:8080/webservices/cpu/")
   factory.protocol = EchoClientProtocol
   connectWS(factory)
   reactor.run()