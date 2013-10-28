import json

from networking.server import *
from networking.client import *

class Net(object):
    def __init__(self):
        # Extract data from file
        try:
            f = open('data', 'r')
            data = json.load(f)
            f.close()
        except:
            data = []
        f = open('data', 'w')
        json.dump(data, f)
        f.close()

        self.server = Server()
        host = input('Host to connect to: ')
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

    def getKey(self, key):        
        f = open('data', 'r')
        data = json.load(f)
        f.close()

        for i in data:
            if i[0] == key:
                break
        if i[0] != key:
            i[1] = False

        return i[1]

    def putKey(self, key, value):        
        f = open('data', 'w')
        data = json.load(f)

        for x,i in enumerate(data):
            if i[0] == key:
                break
        if i[0] == key:
            data[x] = [key, value]
        else:
            data.append([key, value])

        json.dump(data, f)
        f.close()
