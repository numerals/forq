#! /usr/bin/sh

##
# Forismatic Conky
# https://github.com/MnC-69/forq.git
#
# Copyright (c) 2014 Sartaj Singh, Sumit Sahrawat
# Licensed under the MIT license.
##

SCRIPT_DIR=$(readlink -f ${0%/*})
ROOT_ACCESS=1
USER_UID=$($SCRIPT_DIR/conf/uid.sh)

if [ "$USER_UID" = "0" ]
then
    ROOT_ACCESS=0
fi

if [ "$ROOT_ACCESS" != "0" ]
then
    echo 'Cannot install without root access'
    exit 1
fi

path=/usr/local/forq

if [ ! -d $path ]
then
    mkdir $path           # Make directory if directory does not exist
fi

install -m 0755 "$SCRIPT_DIR/src/generate.py" "$path"
install -m 0644 "$SCRIPT_DIR/src/getQuote.py" "$path"
install -m 0755 "$SCRIPT_DIR/src/parse.py" "$path"
install -m 0755 "$SCRIPT_DIR/conf/width.sh" "$path"
install -m 0755 "$SCRIPT_DIR/conf/forq" "/usr/bin" # Copy the forq conf file
