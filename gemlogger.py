#!/usr/bin/python

import socket
import sys
import argparse

parser = argparse.ArgumentParser(description='%(prog) will connect to a Brultech Green Eye Monitor and log the data output from the GEM.')
parser.add_argument('-H', '--host', default='gem.home.local', help='GEM FQDN to connect to')
parser.add_argument('-p', '--port', type=int, default=5000, help='Port number to connect to')
parser.add_argument('-o', '--output', default='gemlogger.out', help='Output file')


output_file = '/var/log/gemlogger/' + host

try:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  print "Socket successfully created"
except socket.error as err:
  print "Socket creation failed with error %s" %(err)

try:
  host_ip = socket.gethostbyname(host)
except socket.gaierror:
  print "There was an error resolving the host"
  sys.exit()

try:
  of = open(output_file,'ab',1)
except IOError as err:
  print "Error opening log file with error %s" %(err)

s.connect((host_ip,port))

print 'Socket connected to ' + host + ' on ' + host_ip + ':' + str(port)

while True:
  data = s.makefile().readline()
  print 'received:\n' + data
  of.write(data)

#s.close
