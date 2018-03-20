#!/bin/sh

if [ ! -f se-leg/compose.yml ]; then
    echo "Run $0 from the se-leg-developer top level directory"
    exit 1
fi

#
# Set up entrys in /etc/hosts for the containers with externally accessible services
#
( printf "127.0.0.1\tdemo.seleg_dev\n";
  printf "172.16.20.204\trasp.se-leg.docker\n";
  printf "172.16.20.205\tidp.se-leg.docker\n";
  printf "172.16.20.10\tmongodb.se-leg.docker\n";
) \
    | while read line; do
    if ! grep -q "^${line}$" /etc/hosts; then
	echo "$0: Adding line '${line}' to /etc/hosts"
	if [ "x`whoami`" = "xroot" ]; then
	    echo "${line}" >> /etc/hosts
	else
	    echo "${line}" | sudo tee -a /etc/hosts
	fi
    else
	echo "Line '${line}' already in /etc/hosts"
    fi
done

./bin/docker-compose -f se-leg/compose.yml rm -f --all
./bin/docker-compose -f se-leg/compose.yml up $*
