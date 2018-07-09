from .models import Stock
import requests
import pickle
import time


apikey='E4YH51H5HDVQFJB2'

def add_stocks(stocklist):
    for stock in stocklist:
        ticker,name=stock.split(',')
        Stock.objects.create(tickersymbol=ticker,tickername=name)

def get_DMA(stocksymbol,timeperiod):
    url='https://www.alphavantage.co/query?function=SMA&symbol='+stocksymbol+'&interval='+'daily' + '&time_period='+timeperiod+'&series_type=close&apikey='+apikey
    requesteddatanew=requests.get(url)
    jsondata=requesteddatanew.json()
    return list(jsondata['Technical Analysis: SMA'].items())[0][0],list(jsondata['Technical Analysis: SMA'].items())[0][1]['SMA'][:-2]


def get_RSI(stocksymbol,timeperiod):
    url='https://www.alphavantage.co/query?function='+'RSI'+'&symbol='+stocksymbol+'&interval='+'daily' + '&time_period='+timeperiod+'&series_type=close&apikey='+apikey
    requesteddatanew=requests.get(url)
    jsondata=requesteddatanew.json()
    return list(jsondata['Technical Analysis: RSI'].items())[0][0],list(jsondata['Technical Analysis: RSI'].items())[0][1]['RSI'][:-2]


def get_technicals(stocks,DMA,RSI_period):
    technicallist={}
    for stocksymbol in stocks:
        dma=get_DMA(stocksymbol,DMA)
        RSI=get_RSI(stocksymbol,RSI_period)
        technicallist[stocksymbol]=[dma[1],RSI[1]]
    return technicallist

def dailyrun_technicals_forall():
    stocknames=getstocknamedict()
    technicallist={}
    total=len(stocknames)
    counter=0
    for stocksymbol in stocknames.keys():
        counter+=1
        try:
            print(stocksymbol,' in progress....')
            dma50=get_DMA(stocksymbol,'50')
            dma200=get_DMA(stocksymbol,'200')
            RSI=get_RSI(stocksymbol,'14')
            technicallist[stocksymbol]=[dma50[1],dma200[1],RSI[1]]
            print(stocksymbol,' - ',counter,' out of ',total,' done.')
            time.sleep(5)
            pickle.dump(technicallist,open('otherfiles/stocktechnicals.pickle','wb'))
        except:
            time.sleep(25)
            continue
    
    


def get_quote(symbol):
    url='https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols=' + symbol + '&apikey='+ apikey
    requesteddatanew=requests.get(url)
    mydict=requesteddatanew.json()
    stockdict={}
    for each in mydict['Stock Quotes']:
        stockdict[each['1. symbol']]=each['2. price'][:-2]
    timestamp=mydict['Stock Quotes'][0]['4. timestamp']
    return stockdict,timestamp


def get_stockdata(stocklist,DMA,RSI_period):

    stocknames=getstocknamedict()
    prices,timestamp=get_quote(stocklist)
    # technicals=get_technicals(stocklist.split(','),DMA,RSI_period)
    technicals=pickle.load(open('otherfiles/stocktechnicals.pickle','rb'))
    newlist=[]
    for stock in stocklist.split(','):
        newdict={}
        newdict[stock]=[]
        newdict[stock].append(prices[stock])
        newdict[stock].append(technicals.get(stock,'couldntget'))
        newdict[stock].append(stocknames.get(stock,'unknown'))
        newlist.append(newdict)
    return newlist,timestamp

def getstocknamedict():
    stocknames=pickle.load(open('otherfiles/stocknames.pickle','rb'))
    # stocknames=[stock.split(',') for stock in stocknames]
    # stocknames=[[stock[0],stock[1]]  for stock in stocknames]
    stocknamedict=dict(stocknames)
    return stocknamedict









