import time
import json

from networking.server import *
from networking.client import *

class Net(object):
    def __init__(self):
        # 
        try:
            f = open('data', 'r')
            data = json.load(f)
            f.close()
        except:
            data = [['status', False]]
        f = open('data', 'w')
        json.dump(data, f)
        f.close()

        self.server = Server()
        host = input('Host to connect to: ')
        port = input('Port to connect to: ')

        self.client = Client(host, port)
        
        self.putKey('status', True)
        while not self.client.get('status'):
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