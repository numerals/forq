#!/usr/bin/python

##
# Forismatic Conky
# https://github.com/MnC-69/forq.git
#
# Copyright (c) 2014 Sartaj Singh, Sumit Sahrawat
# Licensed under the MIT license.
##

import getQuote as gq # handles the api
import sys

def main():
    """
    Requests a random quote using forismatic API
    """
    quote = gq.getQuote()
    try:
        text = quote.requestQuote() # get quote
        quote.parseJSON(text) # check if parsable
        quote.saveJSON(text, sys.argv.pop()) # saving
    except:
        pass

if __name__ == '__main__':
    main()

