#!/bin/bash

FILE=$1
set -u

if [[ $# -eq 0 ]]; then
    echo "Usage"            
        exit 1
fi

if [[ -f "$FILE" ]]; then
    echo "$1 is a file"

else
    echo "First argument must be a file"
	exit 1
fi

i=0
while read -r LINE; do

	i=$((i+1))
        echo "$i $LINE"

done < "$FILE"
