#!/bin/bash

Green='\e[0;32m'
Red='\e[0;31m'
Color_Off='\e[0m'

rm -f tests/error.tmp
for file in tests/test_*.sh
do
    printf "    ${file}:"
    bash $file 2>&1 > /dev/null
    if [ "$?" = "0" ]
    then
        printf "$Green|[ OK ]"
    else
        printf "$Red|[FAIL]"
        echo "$file" >> tests/error.tmp # This is our way to tell "make" a test failed
    fi
    printf "$Color_Off\n"
done

if [ -f tests/error.tmp ]
then
    printf "\n$Red"
    echo "Failed tests:"
    printf "$Color_Off\n"
    cat tests/error.tmp
fi
