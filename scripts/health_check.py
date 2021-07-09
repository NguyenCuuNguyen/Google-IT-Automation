#!/usr/bin/env python

import shutil #provides functions that support file copying and removal. 
import psutil #Python system and process utilities: system monitoring, profiling, limiting process resources, and managing running processes. 

from network import *

def check_disk_usage(usage):
	"""Verifies that there's enough free space on disk"""
	du = shutil.disk_usage(disk)
	free = du.free/ du.total * 100
	return free >20

def check_cpu_usage():
	"""Verifies that there's enough unused CPU"""
	usaage = psutil.cpu_percent(1)
	return usage <76

# If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage('/') or not check_cpu_usage():
	print("ERROR!")
elif check_localhost() and check_connectivity():
	print("Everything is ok")
else:
	print("Network check failed")
