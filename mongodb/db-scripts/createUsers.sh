#!/bin/bash
#
# Create users for the se-leg local developer environment.
#

# -------------------------------------------------------------------------------------
# User se-leg-op, readWrite
#
for db in se_leg_op; do
    mongo localhost/${db} --eval '
      if (db.system.users.count({"user": "se_leg_op"}) == 0) {
         db.addUser( { user: "se_leg_op", pwd: "se_leg_op_pw", roles: ["readWrite"] } );
      }
'
done

# -------------------------------------------------------------------------------------
# User eduid_oidc_proofing, readWrite
#
for db in eduid_oidc_proofing; do
    mongo localhost/${db} --eval '
      if (db.system.users.count({"user": "eduid_oidc_proofing"}) == 0) {
         db.addUser( { user: "eduid_oidc_proofing", pwd: "eduid_oidc_proofing_pw", roles: ["readWrite"] } );
      }
'
done

# -------------------------------------------------------------------------------------
# User eduid_oidc_proofing, read
#
for db in eduid_am; do
    mongo localhost/${db} --eval '
      if (db.system.users.count({"user": "eduid_oidc_proofing"}) == 0) {
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


# Add initial data in mongodb
#

# -------------------------------------------------------------------------------------
# se-leg-op clients
#
mongo localhost/se_leg_op --eval '
  db.clients.update({ "lookup_key" : "client1"},
                    { "lookup_key" : "client1",
                      "data" : {
                          "response_types" : [[
                              "code",
                              "id_token",
                              "token"
                          ]],
                          "redirect_uris" : [
                              "http://se-leg-rp:8080/authorization-response"
                          ],
                          "client_secret" : "abcdef"
                      },
                    }, upsert=true)
'

