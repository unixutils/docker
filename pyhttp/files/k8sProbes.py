#!/usr/bin/python3
import requests
import glob
import subprocess
import sys

pyhttpServiceUrl = 'http://localhost:7000'
HTTP_OK = 200

def req():
    response = requests.get(pyhttpServiceUrl)
    return response

def isStarted():
    pyhttpLockFile = glob.glob("/pyhttp/pyhttpLockFile_*")
    if pyhttpLockFile:
        print("Service lockfile found!")
        AOK = True
    else:
        print("Service lockfile not found!")
        AOK = False
    return AOK

def isReady():
    response = req()
    if response.status_code == HTTP_OK:
        print("Service is Ready! expected HTTP 200. Received {}".format(response.status_code))
        AOK = True
    else:
        print("Service not Ready! expected HTTP 200. Received {}".format(response.status_code))
        AOK = False
    return AOK


def isValid():
    options = ['isStarted', 'isReady']
    if len(sys.argv) != 2 or sys.argv[1] not in options:
        print('Invalid usage! Available options are {}'.format(options))
        sys.exit(1)
    return True

def main():
    if isValid():
        if sys.argv[1] == 'isStarted':
            probeOK = isStarted()
        if sys.argv[1] == 'isReady':
            probeOK = isReady()
        if not probeOK:
            sys.exit(1)

if __name__ == "__main__":
    main()

