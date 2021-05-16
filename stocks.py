import requests
import json

import config as cfg

#later configure this respoinse status code to handle errors
response = response = requests.get(cfg.api_url)
print(response.status_code)


### Function is to convert json returned from API into a dictionary with key being name or label, and values being price.
def convertAPIDataToMarketData(data):

    market = data['Markets'][0]
    #dictionary to store allStocks with name and price key value pair
    allstocks = {}

    for stock in market:
        allstocks[stock['Name']] = stock['Price']

    return allstocks


ListOfStocks = convertAPIDataToMarketData(response.json())


#need to look into why the price is different than price on robinhood may need diff api :/
print(ListOfStocks['Dogecoin'])
