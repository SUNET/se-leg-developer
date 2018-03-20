#!/bin/bash
#
# Drop proofing data for the se-leg local developer environment.
#
# Run from repo root dir

bin/docker-compose -f se-leg/compose.yml exec mongodb mongo localhost/se_leg_rp --eval 'printjson(db.proofing_data.drop())'

