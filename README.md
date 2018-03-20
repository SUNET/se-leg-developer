# se-leg developer repo

## Why?

To help developers write code locally with a (as close as possible) production environment.

## How?
Before you start the enviroment run `./bin/exchange_metadata.sh` to setup the metadata needed for the idp and sp.

To run all containerns just run `start.sh`. It will ask for permission to write to your /etc/hosts.

To run the container with your local repos just symlink the [se-leg-rp](https://github.com/SUNET/se-leg-rp/) repo and [se-leg-op](https://github.com/SUNET/se-leg-op/) repo to the `sources` directory.


    se-leg-developer
    ├── sources
    │   ├── se-leg-rp -> /.../se-leg-rp/
    │   └── se-leg-op -> /.../se-leg-op/

To try out the demo, just open your favorite browser to [https://demo.seleg_dev](https://demo.seleg_dev).

An already setup user is `testuser` with password `qwerty`.

### How to add another RP

To use your own RP with the OP you have to register it in the MongoDB. The easiest way to do that is to add your client configuration to `$REPO/mongodb/db-scripts/local.yaml`. This file will be read as the MongoDB container starts.

An example:
```
 seleg_op:
    initial_data:
      clients:
        - lookup_key: 'my_client_name'
          data:
            response_types:
              - 'code'
            redirect_uris:
              - 'https://my_rp/authorization-response'
            client_secret: 'abcdef'

```

