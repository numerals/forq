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
    requests a random quote
    """
    quote = {'method': 'getQuote', 'format': 'text', 'lang':'en'}
    r = requests.post("http://api.forismatic.com/api/1.0/", params=quote) # post request
    print(r.text)

if __name__ == '__main__':
    try:
        main()
        return 0
    except:
        return 1

