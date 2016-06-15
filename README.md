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

To try out the demo, just open your favorite browser to [http://demo.seleg_dev](http://demo.seleg_dev).

