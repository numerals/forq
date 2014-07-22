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

# UID of the user
USER_UID=$($SCRIPT_DIR/conf/uid.sh)

# If provided root access, warn the user
if [ "$ROOT_ACCESS" != "0" ]
then
    echo -n 'This will install themes to \"/root/.forq\" continue? (y|n) : '
    read -r REPLY
    if [ "$REPLY" != 'y' && "$REPLY" != 'Y' ]
    then
        exit 1
    fi
fi

# If ~/.forq exists
if [ -d ~/.forq ]; then
    rm -rf ~/.forq
fi

# Make directory ~/.forq
mkdir ~/.forq

# Install all theme files to ~/.forq
for file in "$SHELL_DIR"; do
    install 744 "$SHELL_DIR/themes/$file" "~/.forq/$file"
done
