#!/bin/bash
#
# Create users for the se-leg local developer environment.
#

# -------------------------------------------------------------------------------------
# User se-leg-op, readWrite
#
for db in seleg_op; do
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
mongo localhost/seleg_op --eval '
  db.clients.update({ "lookup_key" : "client1"},
                    { "lookup_key" : "client1",
                      "data" : {
                          "response_types" : ["code"],
                          "redirect_uris" : [
                              "https://demo.seleg_dev/se-leg-rp/authorization-response"
                          ],
                          "client_secret" : "abcdef"
                      },
                    }, upsert=true)
'

mongo localhost/seleg_op --eval '
  db.clients.update({ "lookup_key" : "client2"},
                    { "lookup_key" : "client2",
                      "data" : {
                          "response_types" : ["code"],
                          "redirect_uris" : [
                              "https://demo.seleg_dev/nstic-rp/authorization-response"
                          ],
                          "client_secret" : "abcdef",
                          "vetting_policy" : "POST_AUTH"
                      },
                    }, upsert=true)
'
