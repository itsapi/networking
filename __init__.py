import sys
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

        # Set status to not ready
        self.putKey('status', 0)

        # Start server and client processes
        self.server = Server()
        host = input('Host to connect to: ')
        valid = False
        while not valid:
            try:
                port = int(input('Port to connect to: '))
                valid = True
            except ValueError:
                print('Invalid port')
                valid = False
        self.client = Client(host, port)

        # Set status to ready and wait until other connection is ready
        self.putKey('status', 1)
        print('\nWaiting for connection...')
        while not int(self.client.get('status')):
            time.sleep(0.1)
        print('Connected\n')

    def getData(self):
        # Return contents of file
        f = open('data', 'r')
        data = json.load(f)
        f.close()
        return data[1:]

    def putData(self, data):
        # Replace contents of file with given object
        f = open('data', 'r')
        oData = json.load(f)
        f.close()
        data.insert(0, oData[0])

        f = open('data', 'w')
        json.dump(data, f)
        f.close()

    def getKey(self, key):
        # Return value of particular key from file
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
        # Replace value of particular key or append to file
        f = open('data', 'r')
        data = json.load(f)
        f.close()

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

        f = open('data', 'w')
        json.dump(data, f)
        f.close()
