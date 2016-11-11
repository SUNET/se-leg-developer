# se-leg developer repo

## Why?

To help developers write code locally with a (as close as possible) production environment.

## How?

To run all containerns just run `start.sh`. It will ask for permission to write to your /etc/hosts.

To run the container with your local repos just symlink the [se-leg-rp](https://github.com/SUNET/se-leg-rp/) repo and [se-leg-op](https://github.com/SUNET/se-leg-op/) repo to the `sources` directory.


    se-leg-developer
    ├── sources
    │   ├── se-leg-rp -> /.../se-leg-rp/
    │   └── se-leg-op -> /.../se-leg-op/

To try out the demo, just open your favorite browser to [https://demo.seleg_dev](https://demo.seleg_dev).

### How to add another RP

To use your own RP with the OP you have to register it in the MongoDB. The easiest way to do that is to add your client configuration to the end of `$REPO/mongodb/db-scripts/createUsers.sh`. This script will be run as soon as the MongoDB container starts.

An example:
```
mongo localhost/seleg_op --eval '
  db.clients.update({ "lookup_key" : "your_client_id"},
                    { "lookup_key" : "your_client_id",
                      "data" : {
                          "response_types" : ["code"],
                          "redirect_uris" : [
                              "https://url/to/your/authorization-response/endpoint/"
                          ],
                          "client_secret" : "a_secret"
                      },
                    }, upsert=true)
'
```

