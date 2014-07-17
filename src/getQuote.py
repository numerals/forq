##
# Forismatic Conky
# https://github.com/MnC-69/forq.git
#
# Copyright (c) 2014 Sartaj Singh, Sumit Sahrawat
# Licensed under the MIT license.
##

import requests # support for requesting data
import json # allows json support

class getQuote():
    """
    Gets a random quote using forismatic API
    """
    def requestQuote(self):
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

    def saveJSON(self, quote):
        """
        Takes a string and saves it to the quote.json file
        """
        # Open file used for storing last seen quote
        f = open('quote.json', 'w')

        # Save newly fetched quote to file 
        f.write(quote)

        # Close file
        f.close()
    
    def readJSON(self, info = None):
        """
        Reads the quote from quote.json file 
        """
        # Open old quotes file for reading
        f = open('quote.json', 'r')

        # Read file and return old contents
        quote = f.read()

        # Close file
        f.close()

        # parse the JSON string
        quote = self._parseJSON(quote, info)

        return quote

    def _parseJSON(self, quote, info = None):                   
        """
        Parses JSON string
        """
        quote = json.loads(quote)

        if info != None:
            return quote[info] # return required portion of JSON string

        return quote # return the complete JSON string
