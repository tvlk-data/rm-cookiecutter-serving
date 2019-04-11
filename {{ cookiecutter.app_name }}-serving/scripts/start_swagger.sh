#!/bin/bash

if [ $(which docker) = "" ]; then
    echo "Docker is not installed. Please install docker first before proceeding"
    exit 1
fi

docker pull swaggerapi/swagger-editor
docker run --rm -d -p 80:8080 swaggerapi/swagger-editor

if [ $(uname) = "Linux" ]
then
    x-www-browser http://localhost
elif [ $(uname) = "Darwin" ]
then
    open http://localhost
else
    echo "Please open http://localhost on your browser"
fi

read -p "Press [ENTER] to terminate this session..." key

{% raw -%}
docker stop $(docker ps -a -q --filter ancestor=swaggerapi/swagger-editor --format="{{.ID}}") > /dev/null
{%- endraw %}