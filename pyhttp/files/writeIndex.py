#!/usr/bin/python3
import os, glob
import http.server
import socketserver

httpPort = 7000
Handler = http.server.SimpleHTTPRequestHandler

configMapFiles = glob.glob("/pyhttp_config/*PYHTTP*")
indexFile = ("/pyhttp/index.html")
open(indexFile, 'a').close()

ifile = open(indexFile, "r+")

# WELCOME TEXT
ifile.write(r'<pre>')
ifile.write("\n***WELCOME TO PyHTTP***\n")

# ENVIRONMENTAL VARIABLES
ifile.write("\n***Printing env var(s) loaded from configmap***\n")
for i in os.environ:
    if 'PYHTTP_KEY' in i:
        ifile.write(i + '=' + os.environ[i] + '\n')

# FILES MOUNTED FROM CONFIGMAPS
ifile.write("\n***Printing file(s) loaded via configmap***\n")
for file in configMapFiles:
    with open(file, 'r') as f:
        ifile.write("contents of configmap file: " + file + '\n')
        for line in f.readlines():
            ifile.write(line)

ifile.write(r'</pre>')
ifile.close()

os.chdir('/pyhttp')
with socketserver.TCPServer(("", httpPort), Handler) as httpd:
    httpd.serve_forever()

