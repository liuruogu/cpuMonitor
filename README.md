# cpuMonitor documentation
This is a simple Python tornado websocket server that use Tornado websocket handler. Please install tornado with python version of 2.7.9 or greater.


Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed. By using non-blocking network I/O, Tornado can scale to tens of thousands of open connections, making it ideal for long polling, WebSockets, and other applications that require a long-lived connection to each user.
```
pip install tornado 
```

Twisted is an event-driven network programming framework written in Python and licensed under the MIT License. Twisted projects variously support TCP, UDP, SSL/TLS, IP multicast, Unix domain sockets, a large number of protocols,

```
pip install twisted
```

Autobahn|Python is part of the Autobahn project and provides open-source implementations of the WebSocket Protocol and the Web Application Messaging Protocol (WAMP)

```
pip install autobahn
```


Psutil is a  Cross-platform lib for process and system monitoring in Python.
```
pip install 
```

## Functionality
The monitor server run upon a tornado websocket handler. It open a websocket connection and collect all the clients' CPU usages data. The collected date will be printed on terminal and also be virtualized on a Web interface(TBD). The server can have multiple websockets connection and monitor all the clients at the same time. The clients have very high CPU usages can be filtered.

The client will connect to websocket server and send its CPU usages data in percentage to the server. The data will be sent in real-time with an interval of 1 second.


## Useful notes
1. Highly recommend to use virtualenv to setup virtual environment to manage python packages for this websocket project.
http://docs.python-guide.org/en/latest/dev/virtualenvs/

2. Since these codes only tested on a local environment, Please change the IP address inside the  client file when you are trying to connect to websocket server.
```   
factory = WebSocketClientFactory("ws://127.0.0.1:8080/webservices/cpu/")
```