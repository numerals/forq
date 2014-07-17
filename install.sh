#! /usr/bin/bash

##
# Forismatic Conky
# https://github.com/MnC-69/forq.git
#
# Copyright (c) 2014 Sartaj Singh, Sumit Sahrawat
# Licensed under the MIT license.
##

# explains the usage
usage_forq()
{
    echo "Usage: forq <flag>"
    echo "Valid flags:"
    echo "  -n : Request new quote from forismatic"
    echo "  -q : Print last quote"
    echo "  -a : Print author of last quote"
}

echo -n 'Install in /usr/local/forq ? [Y|N] -> '
read ans 

if [ "$ans" = "N" ]
then
    echo -n 'Enter Path -> '
    read path # custom path
else
    path=/usr/local/forq/ # default path
fi

echo "Installing in $path"

if [ ! -d $path ]
then
    mkdir $path # make directory if directory does not exist
fi
cp src/* $path # copy scripts
cp conf/forq /usr/bin/ # copy the forq conf file

echo "Install successful"
usage_forq
