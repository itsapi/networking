import json

from networking.server import *
from networking.client import *

class Net(object):
    def __init__(self):
        try:
            f = open('data', 'r')
            data = json.load(f)
            f.close()
        except:
            data = []
        f = open('data', 'w')
        json.dump(data, f)
        f.close()

        host = 'localhost'#input('Host to connect to: ')
        self.server = Server(host)
        port = input('Port to connect to: ')

        self.client = Client(host, port)

    def getData(self):
        f = open('data', 'r')
        data = json.load(f)
        f.close()
        return data

    def putData(self, data):
        f = open('data', 'w')
        json.dump(data, f)
        f.close()
