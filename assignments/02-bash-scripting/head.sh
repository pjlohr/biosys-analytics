#!/bin/bash

set -u

if [[ $# -eq 0 ]]; then
    echo "Usage"
        exit 1
fi

FILE=$1
num_Lines=${2:-3}

if ! [[ -f "$FILE" ]]; then
    echo "foo is not a file"
	exit 1
fi

i=1
while read -r LINE; do

        if [[ $i -gt $num_Lines ]]; then
                break
        else

            echo "$LINE"
        fi
	i=$((i+1))

done < "$FILE"



