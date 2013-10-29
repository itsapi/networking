import sys
import time
import json

from networking.server import *
from networking.client import *

class Net(object):
    def __init__(self):
        # Extract data from file
        try:
            with open('data', 'r') as f:
                data = json.load(f)
        except:
            with open('data', 'w') as f:
                json.dump([], f)

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
        with open('data', 'r') as f:
            data = json.load(f)
        return data[1:]

    def putData(self, data):
        # Replace contents of file with given object
        with open('data', 'r') as f:
            oData = json.load(f)
        data.insert(0, oData[0])

        with open('data', 'w') as f:
            json.dump(data, f)

    def getKey(self, key):
        # Return value of particular key from file
        with open('data', 'r') as f:
            data = json.load(f)

        for i in data:
            if i[0] == key:
                break
        if i[0] != key:
            i[1] = False

        return i[1]

    def putKey(self, key, value):
        # Replace value of particular key or append to file
        with open('data', 'r') as f:
            data = json.load(f)

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

        with open('data', 'w') as f:
            json.dump(data, f)
