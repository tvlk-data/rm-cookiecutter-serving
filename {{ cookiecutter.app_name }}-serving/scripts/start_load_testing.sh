#!/bin/bash

if [ $(which python3) = "" ]; then
    echo "Python3 is not installed. Please install Python3 first before proceeding"
    exit 1
fi

python3 -m pip install locustio

rm locust.log

locust --host=$1 -f test/locustfile.py --logfile=locust.log & 

if [ $(uname) = "Linux" ]
then
    x-www-browser http://localhost:8089 & 
elif [ $(uname) = "Darwin" ]
then
    open http://localhost:8089 & 
else
    echo "Please open http://localhost:8089 on your browser" & 
fi

sleep 10s
echo ""
read -p "Press [ENTER] to terminate this session..." key

{% raw -%}
lsof -n | grep LISTEN | grep 8089 | awk '{ print $2 }' | xargs kill
{%- endraw %}