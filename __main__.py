import time
import json

from server import *
from client import *

if __name__ == '__main__':
    f = open('data', 'r')
    try:
        data = json.load(f)
    except:
        data = []
    data += [['b', 10]]
    f.close()
    f = open('data', 'w')
    json.dump(data, f)
    f.close()

    host = 'localhost'#input('Host to connect to: ')
    server = Server(host)
    port = input('Port to connect to: ')

    client = Client(host, port)

    while True:
        client.get('b')
        time.sleep(1)

    server.stop()
