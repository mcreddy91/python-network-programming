#!/usr/bin/env python
'doc'

import socket
solist = [x for x in dir(socket) if x.startswith('SO_')]
solist.sort()
for x in solist:
    print x
