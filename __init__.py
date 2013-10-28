import time
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
            f = open('data', 'w')
            json.dump([], f)
            f.close()

        self.putKey('status', 0)

        self.server = Server()
        host = input('Host to connect to: ')
        port = input('Port to connect to: ')
        self.client = Client(host, port)
        
        self.putKey('status', 1)
        while not int(self.client.get('status')):
            time.sleep(0.1)

    def getData(self):
        f = open('data', 'r')
        data = json.load(f)
        f.close()
        return data[1:]

    def putData(self, data):
        f = open('data', 'r')
        oData = json.load(f)
        f.close()
        data.insert(0, oData[0])

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
        f = open('data', 'r')
        data = json.load(f)
        f.close()
        f = open('data', 'w')

        for x,i in enumerate(data):
            if i[0] == key:
                break
        try:
            if i[0] == key:
                data[x] = [key, value]
            else:
                 data.append([key, value])
        except:
            data.append([key, value])

        json.dump(data, f)
        f.close()
