import sys
import time
import random
from multiprocessing import Process
import socket

IP = '2.2.2.102'
PORT = random.randint(8000, 9000)

global cons
cons = ['hello']

def checker():
    global cons
    cons.append('gsdgsdgsdrg')
    print cons
    while True:
        so = socket.socket()
        try:
            so.connect((IP, PORT))
            cons.append(so.recv(1024))
            print(cons[-1])
        except socket.error:
            pass
        so.close

def main():
    p = Process(target=checker)
    p.start()

    si = socket.socket()
    si.bind(('', PORT))
    si.listen(5)
    while True:
        c, addr = si.accept()

        #print(addr[0])
        print cons
        c.send(raw_input('Msg: '))
        c.close()

if __name__ == '__main__':
    main()
