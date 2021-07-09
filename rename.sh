#!/bin/bash

for file in *.sh; do
	name=$(basename "$file" .sh) #basename function returns the basename without extension
	echo mv "$file" "name.SH" #echo the changes so they're printed and not actually changed
done 
	
