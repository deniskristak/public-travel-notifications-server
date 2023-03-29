#!/bin/bash

LOCAL_DIR=$PWD
REMOTE_USER='denis'
REMOTE_SERVER='thenis.co.uk'
REMOTE_DIR='/home/denis/Projects/'

# Continuously monitor the local directory for changes
while true; do
    inotifywait -r -e modify,create,delete "$LOCAL_DIR"
    # Synchronize the changes with the remote server
    rsync -avz -e ssh "$LOCAL_DIR" $REMOTE_USER@$REMOTE_SERVER:$REMOTE_DIR
done
