#!/bin/bash
#
# Create users for the se-leg local developer environment.
#

# -------------------------------------------------------------------------------------
# User eduid_oidc_proofing, read
#
for db in eduid_am; do
    mongo localhost/${db} --eval '
      if (db.system.users.count({"user": "eduid_oidc_proofing,"}) == 0) {
         db.addUser( { user: "eduid_oidc_proofing", pwd: "eduid_oidc_proofing_pw", roles: ["read"] } );
      }
'
done

# -------------------------------------------------------------------------------------
#
# User eduid_am, readWrite
#
for db in eduid_am; do
    mongo localhost/${db} --eval '
      if (db.system.users.count({"user": "eduid_am"}) == 0) {
         db.addUser( { user: "eduid_am", pwd: "eduid_am_pw", roles: ["readWrite"] } );
      }
'
done

#
# User eduid_am, read
#
for db in eduid_signup eduid_dashboard eduid_api; do
    mongo localhost/${db} --eval '
      if (db.system.users.count({"user": "eduid_am"}) == 0) {
         db.addUser( { user: "eduid_am", pwd: "eduid_am_pw", roles: ["read"] } );
      }
'
done
