#!/bin/sh

set -e

if [ ! -f se-leg/compose.yml ]; then
    echo "Run $0 from the se-leg-developer top level directory"
    exit 1
fi

SP_METADATA="https://rasp.se-leg.docker/Shibboleth.sso/Metadata"

./bin/docker-compose -f se-leg/compose.yml down
./bin/docker-compose -f se-leg/compose.yml up -d ra_sp
printf "Waiting for shibboleth container to be ready."
until $(curl -k --output /dev/null --silent --head --fail $SP_METADATA); do
    printf '.'
    sleep 1
done
echo "\n"
curl -ks $SP_METADATA -o ./pysaml2-idp/etc/sp.xml
echo "Downloaded $SP_METADATA to ./pysaml2-idp/etc/sp.xml"
printf "Copied "
cp -v ./pysaml2-idp/etc/idp.xml ./se-leg-ra-sp/etc/shibboleth/idp.xml
./bin/docker-compose -f se-leg/compose.yml down
./bin/docker-compose -f se-leg/compose.yml rm --all
