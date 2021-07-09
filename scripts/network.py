#!/usr/bin/env python3 #shebang: defines interpreter's location

import requests
import socket

def check_localhost():
	#check socket module to see if local host if correctly configured:
	#translates host name to IPv4@ format
	localhost = socket.gethostbyname('localhost') #result = loop back @
	if localhost == "127.0.0.1":
		return True
	else:
		return False

def check_connectivity():
	#below func returns web's status code:
	request = requests.get("http://www.google.com")
	if request.status_code == 200:
		return True
	else:
		return False

