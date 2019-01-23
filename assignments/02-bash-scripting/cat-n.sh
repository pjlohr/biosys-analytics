#!/bin/bash

set -u

if [[ $# -eq 0 ]]; then
    echo "Usage"            
        exit 1
fi

FILE=$1

if ! [[ -f "$FILE" ]]; then
    echo "foo is not a file"
	exit 1

fi

i=0
while read -r LINE; do

	i=$((i+1))
        echo "$i $LINE"

done < "$FILE"
