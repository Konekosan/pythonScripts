#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

host = ""
port= 0

def netcat(hostname, port, content):
    print "[+] Opening connection to " + host + " -p " + str(port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.sendall(content)
    s.shutdown(socket.SHUT_WR)

    res = ""

    while 1:

        data = s.recv(1024)

        if data == "":
            break

	res += data

        print res

    print "\n[-] Connection closed to " + host + " -p " + str(port)
    s.close()

stage1 = "\x90"
#multistage
stage2 = "\x90"

lenstage1 = len(stage1)
lenstage2 = len(stage2)

payload = stage1 + stage2

print "Len stage 1 : ", lenstage1
print "Len stage 2 : ", lenstage2

netcat(host, port, payload)
