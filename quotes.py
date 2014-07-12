#!/usr/bin/python

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

        # TODO : Save to file if request successful

        # Print Quote
        print(r.text)
    except:
        # TODO : Read file and return old contents

        print("Couldn't fetch quote") # To be removed

if __name__ == '__main__':
    main()

