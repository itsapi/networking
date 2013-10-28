import socket

class Client(object):
    def __init__(self, ip, port):
        self.port = int(port)
        self.ip = ip

    def get(self, data):
        data = str(data)

        # Open connection to ip with port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.ip, self.port))
        try:
            # Atempt to send message to server
            sock.sendall(bytes(data, 'ascii'))
            response = str(sock.recv(1024), 'ascii')
            print("Received: {}".format(response))
            return response
        finally:
            sock.close()
            return False