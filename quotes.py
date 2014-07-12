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

def getQuote():
    """
    Gets a random quote using forismatic API
    """
    # The getQuote function's work begins after these function definitions

    def requestQuote():
        """
        Requests a random quote from forismatic.
        Returns a JSON string
        """
        
        # Specification for the request
        quote = {'method': 'getQuote', 'format': 'json', 'lang':'en'}

        # Post Request
        r = requests.post("http://api.forismatic.com/api/1.0/", params = quote)

        # Return data received
        return r.text

    def saveQuoteJSON(quote):
        """
        Takes a string and saves it to the quote.json file
        """
        # Open file used for storing last seen quote
        f = open('quote.json', 'w')

        # Save newly fetched quote to file 
        f.write(quote)

        # Close file
        f.close()
    
    def readQuoteJSON():
        # Open old quotes file for reading
        f = open('quote.json', 'r')

        # Read file and return old contents
        quote = f.read()

        # Close file
        f.close()

        return quote

    def printQuote(quote):           # TODO: Actually parse JSON instead of just printing it out
        print(quote)
        
    # The function's work begins here        
    try:
        # Request a quote
        quote_json = requestQuote()
        
        # Save the quote to file
        saveQuoteJSON(quote_json)
        
        # Print Quote
        printQuote(quote_json)
        
    except:
        # Read old quote from quote.json
        quote_json = readQuoteJSON()

        # Print Quote
        printQuote(quote_json)
        
def main():
    """
    Requests a random quote using forismatic API
    """
    getQuote()

if __name__ == '__main__':
    main()

