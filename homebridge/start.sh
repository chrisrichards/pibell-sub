#!/bin/bash

echo Makding directory
mkdir -p /data/homebridge/

echo Copying files
cp /root/.homebridge/config.json /data/homebridge/

echo avahi-browse
avahi-browse -a

echo Starting homebridge
homebridge --user-storage-path /data/homebridge/