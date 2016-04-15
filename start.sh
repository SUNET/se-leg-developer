#!/bin/sh

if [ ! -x ./bin/docker-compose ]; then
    echo "Run $0 from the se-leg-developer top level directory"
    exit 1
fi

./bin/docker-compose -f se-leg/compose.yml up $*
