#!/bin/sh

if [ ! -f se-leg/compose.yml ]; then
    echo "Run $0 from the se-leg-developer top level directory"
    exit 1
fi

#
# Set up entrys in /etc/hosts for the containers with externally accessible services
#
(printf "172.16.20.100\tse-leg-op.seleg_dev se-leg-op\n";
printf "172.16.20.254\tetcd.seleg_dev etcd\n";
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
