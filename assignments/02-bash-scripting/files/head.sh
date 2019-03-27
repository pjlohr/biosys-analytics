
#!/bin/bash

num_Lines=${2:-3}
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

i=1
while read -r LINE; do

        if [[ $i -gt $num_Lines ]]; then
                break
        else

            echo "$LINE"
        fi
	i=$((i+1))

done < "$FILE"



