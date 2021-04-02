#!/bin/bash

set -e
USER_ID=${LOCAL_USER_ID:-9001}

useradd --shell /bin/bash -u $USER_ID -o -c "" -m healthdb
export HOME=/home/healthdb
export CORE=/app

exec /usr/local/bin/gosu healthdb "$@"
