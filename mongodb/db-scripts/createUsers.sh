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
# User se-leg-rp, readWrite
#
for db in se_leg_rp; do
    mongo localhost/${db} --eval '
      if (db.system.users.count({"user": "se_leg_rp"}) == 0) {
         db.addUser( { user: "se_leg_rp", pwd: "se_leg_rp_pw", roles: ["readWrite"] } );
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
                              "http://rp:5000/authorization-response"
                          ],
                          "client_secret" : "abcdef"
                      },
                    }, upsert=true)
'

