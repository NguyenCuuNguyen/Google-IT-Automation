#!/bin/bash
#show the most common lines of sys var log
for logfile in /var/log/*log; do
	echo "Procesing: $logfile"
	cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done
