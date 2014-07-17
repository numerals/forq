#!/usr/bin/python

##
# Forismatic Conky
# https://github.com/MnC-69/forq.git
#
# Copyright (c) 2014 Sartaj Singh, Sumit Sahrawat
# Licensed under the MIT license.
##

import sys
import getQuote as gq # handles the api

def main():
    """
    Requests a random quote using forismatic API
    """
    quote = gq.getQuote()
    text = quote.readJSON(sys.argv.pop())
    print(text) # print the requested

if __name__ == '__main__':
    main()


