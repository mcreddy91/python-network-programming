#!/usr/bin/env python

import sys
import socket

try:
    result = socket.gethostbyaddr(sys.argv[1])

    print "Primary hostname:"
    print " " + result[0]

    for item in result[2]:
        print " " + item
except socket.herror,e:
    print "couldn't look up name:",e

