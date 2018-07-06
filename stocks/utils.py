from .models import Stock
import requests


apikey='E4YH51H5HDVQFJB2'

def add_stocks(stocklist):
    for stock in stocklist:
        ticker,name=stock.split(',')
        Stock.objects.create(tickersymbol=ticker,tickername=name)

def get_quote(symbol):
    url='https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols=' + symbol + '&apikey='+ apikey
    requesteddatanew=requests.get(url)
    mydict=requesteddatanew.json()
    stockdict={}
    for each in mydict['Stock Quotes']:
        stockdict[each['1. symbol']]=each['2. price']
    timestamp=mydict['Stock Quotes'][0]['4. timestamp']
    return stockdict,timestamp