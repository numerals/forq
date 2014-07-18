#! /usr/bin/sh

##
# Forismatic Conky
# https://github.com/MnC-69/forq.git
#
# Copyright (c) 2014 Sartaj Singh, Sumit Sahrawat
# Licensed under the MIT license.
##

# The directory where the install.sh script is kept
SCRIPT_DIR=$(readlink -f ${0%/*})

# Whether root access is provided
ROOT_ACCESS=1

# UID of the user
USER_UID=$($SCRIPT_DIR/conf/uid.sh)

# If user = root, the root_access = true
if [ "$USER_UID" = "0" ]
then
    ROOT_ACCESS=0
fi

# If no root access, exit
if [ "$ROOT_ACCESS" != "0" ]
then
    echo 'Cannot install without root access'
    exit 1
fi

# Path to install
path=/usr/local/forq

if [ ! -d $path ]
then
    mkdir $path           # Make directory if directory does not exist
fi

# Install files
install -m 0755 "$SCRIPT_DIR/src/generate.py" "$path"
install -m 0644 "$SCRIPT_DIR/src/getQuote.py" "$path"
install -m 0644 "$SCRIPT_DIR/src/quote.json" "$path"
install -m 0755 "$SCRIPT_DIR/src/parse.py" "$path"
install -m 0755 "$SCRIPT_DIR/conf/width.sh" "$path"
install -m 0755 "$SCRIPT_DIR/conf/forq" "/usr/bin" # Copy the forq conf file
