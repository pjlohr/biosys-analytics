#!/bin/bash

set -u

if [[ $# -eq 0 ]]; then
    find ../../data/gapminder -type f ! -iname "all.*" | sort | sed 's/.*\///' | cut -d "." -f1 | cat -n
        exit 0
fi


STRING=$1

if [[ $(find ../../data/gapminder -iname "$STRING*" -type f | sort | sed 's/.*\///' | cut -d "." -f1 | wc -c) -eq 0  ]]; then
    echo "There are no countries starting with \""$STRING"\""
    exit 1
else
 find ../../data/gapminder -iname "$STRING*" -type f ! -iname "all.*" | sort | sed 's/.*\///' | cut -d "." -f1 | cat -n

fi

exit 0
