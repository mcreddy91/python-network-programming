#!/usr/bin/env python

'doc'

import socket
import traceback
import struct

host = ''
port = 51423

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.AF_INET,socket.SO_REUSEADDR,1)
s.bind((host,port))

while True:
    try:
        message,address = s.recvfrom(8192)
        secs = int(time.time())
        secs -= 60*60*24
        secs += 2208988800
        reply = struct.pack("!I",secs)
        s.sendto(reply,address)
    except(KeyboardInterrupt,SystemExit):
        raise
    except:
        traceback.print_exc()


