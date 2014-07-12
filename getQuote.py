##
# Forismatic Conky
# https://github.com/MnC-69/forq.git
#
# Copyright (c) 2014 Sartaj Singh, Sumit Sahrawat
# Licensed under the MIT license.
##

import requests

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

    def saveQuoteJSON(self, quote):
        """
        Takes a string and saves it to the quote.json file
        """
        # Open file used for storing last seen quote
        f = open('quote.json', 'w')

        # Save newly fetched quote to file 
        f.write(quote)

        # Close file
        f.close()
    
    def readQuoteJSON(self):
        """
        Reads the quote form quote.json file 
        """
        # Open old quotes file for reading
        f = open('quote.json', 'r')

        # Read file and return old contents
        quote = f.read()

        # Close file
        f.close()

        return quote

    def parseJSON(self, quote):                   
        """
        Parses the json returned by the forismatic api
        """
        # TODO: Actually parse JSON instead of just printing it out
        print(quote)
