#!/bin/bash
#set -ex

dlt-daemon > /var/log/dlt-daemon.log 2>&1 &
routingmanagerd > /var/log/routingmanagerd.log 2>&1 &
# engine-service > /var/log/engine.log 2>&1 &
radio-service > /var/log/radio.log 2>&1 &
#/radio-client
/bin/bash
