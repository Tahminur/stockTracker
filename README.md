# Stock Tracker
A python application aimed at notifying a user for when a stock goes below a certain price

USE GUIDE
- To use properly you will need a file named config.py that will contain two variables
    - api_url = f"https://www.worldcoinindex.com/apiservice/v2getmarkets?key={key}&fiat=usd"
    - key = this will be the key that is obtained from the World Coin Index in the API's used section below, there should be a generate key option available to you on the website       below

API's used
- World Coin Index: https://www.worldcoinindex.com/apiservice

First Feature Released (Current)
- allow users to retrieve price of a given stock by providing it in the command line

Second Feature to be Released will aim to
- allow users to retrieve prices of multiple given stocks by providing it in the command line
- give updates on the price of the given stocks every 5 minutes
