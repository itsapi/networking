import socket

class Client(object):
    def __init__(self, ip, port, stop):
        self.stop = stop
        self.port = int(port)
        self.ip = ip

    def get(self, data):
        data = str(data)

        # Open connection to ip with port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((self.ip, self.port))
        except:
            self.stop()
        try:
            # Atempt to send message to server
            sock.sendall(bytes(data, 'ascii'))
            return str(sock.recv(1024), 'ascii')
        finally:
            sock.close()
