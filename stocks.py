import requests
import json
import sys
import getopt

import config as cfg



### Function is to convert json returned from API into a dictionary with key being name or label, and values being price.
def convertAPIDataToMarketData(data):

    market = data['Markets'][0]
    #dictionary to store allStocks with name and price key value pair
    allstocks = {}

    for stock in market:
        allstocks[stock['Name']] = stock['Price']

    return allstocks

#takes dictionary of allstocks and name of a stock to return price
def getPrice(allStocks, name):
    return allStocks[name]



def main():
    #later configure this respoinse status code to handle errors
    response = response = requests.get(cfg.api_url)
    print(response.status_code)
    ListOfStocks = convertAPIDataToMarketData(response.json())
    #below accepts first argument passed in command line
    print(getPrice(ListOfStocks, sys.argv[1]))



if __name__ == '__main__':
    main()
