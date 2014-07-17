#! /usr/bin/sh

##
# Forismatic Conky
# https://github.com/MnC-69/forq.git
#
# Copyright (c) 2014 Sartaj Singh, Sumit Sahrawat
# Licensed under the MIT license.
##

PATH1=/usr/local/forq
PATH2=~/.forq

# Explains the usage
usage_forq()
{
    echo "Usage: forq <flag>"
    echo "Valid flags:"
    echo "  -n : Request new quote from forismatic"
    echo "  -q : Print last quote"
    echo "  -a : Print author of last quote"
}

echo -n 'Install in /usr/local/forq (1) OR ~/.forq (2) [ 1|2 ] -> '
read ans 

if [ "$ans" = "2" ]
then
    path=$PATH2
else
    path=$PATH1
fi

echo "Installing in $path"

if [ ! -d $path ]
then
    mkdir $path           # Make directory if directory does not exist
fi

cp src/* $path                  # Copy scripts
cp conf/forq /usr/bin/          # Copy the forq conf file

echo "Install successful"
usage_forq
