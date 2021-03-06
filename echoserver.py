#!/usr/bin/env python

import socket
import traceback

host = ''
port = 51423

s = socket.socket(socket.AF_INET,
        socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,
        socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(1)

while True:
    try:
        clientsock,clientaddr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue

    try:
        print 'Got connection from',clientsock.getpeername()
        while True:
            data = clientsock.recv(4096)
            if not len(data):
                break
            clientsock.sendall(data)
    except(KeyboardInterrupt,SystemExit):
        raise
    except:
        traceback.print_exc()


    try:
        clientsock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()

