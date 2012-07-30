#!/usr/bin/env python

import sys
import socket
import time

s = socket.fromfd(sys.stdin.fileno(),socket.AF_INET,socket.SOCK_STREAM)
s.sendall("Welcome.\n")
s.sendall("According to oour records,you are connected from %s.\n"\
        % str(s.getpeername()))
s.sendall("The local time is %s.\n" % time.asctime())
