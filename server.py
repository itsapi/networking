import threading
import socketserver
import json

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # Processes data and returns response to sender
        key = str(self.request.recv(1024), 'ascii')
        f = open('data', 'r')
        data = json.load(f)
        f.close()
        for i in data:
            if i[0] == key:
                break
        try:
            if i[0] != key:
                i[1] = False
        except:
            i = ['', False]
        response = bytes(str(i[1]), 'ascii')
        self.request.sendall(response)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class Server(object):
    def __init__(self):
        # Port 0 means to select an arbitrary unused port
        # IP '' means to listen on all interfaces
        self.server = ThreadedTCPServer(('', 0), ThreadedTCPRequestHandler)
        ip, port = self.server.server_address

        print('Port: ' + str(port) + '\n')

        # Start a thread with the server -- that thread will then start one
        # more thread for each request
        server_thread = threading.Thread(target=self.server.serve_forever)
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()

    def stop(self):
        self.server.shutdown()
