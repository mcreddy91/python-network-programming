#!/usr/bin/env python

import socket
import sys
import struct
import time

hostname = 'time.nist.gov'
port = 37

host = socket.gethostbyname(hostname)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto('',(host,port))

print "Looking for replies;press Ctrl-C to stop"

buf = s.recvfrom(2048)[0]
if len(buf) != 4:
	print "Wrong-size reply %d:%s" % (len(buf),buf)
	sys.exit(1)

secs = struct.unpack("!I",buf)[0]
secd -= 2208988800
print time.ctime(int(secs))

