# se-leg developer repo

## Why?

To help developers write code locally with a (as close as possible) production environment.

## How?

To run all containerns just run `start.sh`. It will ask for permission to write to your /etc/hosts.
 
If it is the first time you run start.sh it might fail as the bootstrap container didn't finish before the RP or OP managed to start. If it fails just press `ctrl+c` and run start.sh again.

To run the container with your local repos just symlink the [eduid-webapp](https://github.com/SUNET/eduid-webapp/) repo and [se-leg-op](https://github.com/SUNET/se-leg-op/) repo to the `sources` directory.

To try out the demo, just open your favorite browser to [http://demo.seleg_dev](http://demo.seleg_dev).

## Future plans

Break out all eduID specific parts from eduid_webapp.oidc_proofing and create a new se-leg-rp repo with the bare minumum
that is needed for a RP.