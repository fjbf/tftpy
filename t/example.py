#!/usr/bin/env python3
import tftpy
import os

def evaluate(path,raddress,rport):
	print("%s:%s requested %s" % (str(raddress),str(rport),str(path)))
	if os.path.exists(path):
		return open(path,'r')
	else:
		raise tftpy.TftpException("File not found: %s" % path)

server = tftpy.TftpServer('/srv/tftp', dyn_file_func=evaluate)
#server = tftpy.TftpServer('/srv/tftp')
server.listen('0.0.0.0')
