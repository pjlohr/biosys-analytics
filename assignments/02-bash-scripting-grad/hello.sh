#!/bin/bash

set -u

if [[ $# -eq 0 ]]; then
    echo "Usage: hello.sh GREETING [NAME]"            
        exit 1
fi

if [[ $# -gt 2 ]]; then
    echo "Usage: hello.sh GREETING [NAME]"
        exit 1
fi

NAME=${2:-Human}
GREETING=$1
printf "%s, %s!\n" "$GREETING" "$NAME"
