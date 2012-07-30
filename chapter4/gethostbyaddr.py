#!/usr/bin/env python

import sys
import socket

def get_ipaddrs(hostname):
    result = socket.getaddinfo(hostname,None,0,
            socket.SOCK_STREAM)
    return [x[4][0] for x in result]

def get_hostname(ipaddr):
    return socket.gethostbyaddr(ipaddr[0])


try:
    hostname = get_hostname(sys.argv[1])
    ipaddrs = get_ipaddrs(hostname)
except socket.herror,e:
    print "No host names available for %s;\
            ;this may be normal." % sys.argv[1]
    sys.exit(0)

except socket.gaierror,e:
    print "Got hostname %s,but it could not be forward-resolved:%s"\
            %(hostname,str(e))
    sys.exit(1)

if not sys.argv[1] in ipaddrs:
    print "Got hostname %s,but on forward lookup," % hostname
    print "original IP %s did not appear in IP address list."\
            % sys.argv[1]
    sys.exit(1)

print "Validates hostname:",hostname
