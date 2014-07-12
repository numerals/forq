#!/usr/bin/python2

##
# Forismatic Conky
# https://github.com/MnC-69/forq.git
#
# Copyright (c) 2014 Sartaj Singh, Sumit Sahrawat
# Licensed under the MIT license.
##

"""
Generates random quote
"""

import requests

def main():
    """
    Requests a random quote using forismatic API
    """

    # Specification for the request
    quote = {'method': 'getQuote', 'format': 'text', 'lang':'en'}

    try:
        # Post Request
        r = requests.post("http://api.forismatic.com/api/1.0/", params = quote)

        # Open file used for storing last seen quote
        f = open('quote', 'w')

        # Save newly fetched quote to file 
        f.write(r.text)

        # Close file
        f.close()
        
        # Print Quote
        print(r.text)
        
    except:
        # Open old quotes file for reading
        f = open('quote', 'r')

        # Read file and return old contents
        print(f.read())

        # Close file
        f.close()

if __name__ == '__main__':
    main()

