from fastapi import FastAPI, Query
from typing import Optional
import json
import datetime as dt
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = {"*"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methoda=["*"],
    allow_headers=["*"],
)

with open('data.json', 'r') as f:
    data = json.load(f)


@app.get('/all')
def listing_trades():
    return data


@app.get('/trade/{trade_id}')
def single_trade(trade_id: str):
    trade = [t for t in data if t['tradeId'] == trade_id]
    return trade[0] if len(trade) > 0 else {}


@app.get('/searchTrade')
def search_trade(search: str = Query(title="search parameter", description="Takes the values of any "
                                                                           "of the following counterparty "
                                                                           "instrumentId "
                                                                           "instrumentName "
                                                                           "trader")):
    trades = [t for t in data if t['counterparty'] == search or t['instrumentId'] == search or
              t['instrumentName'] == search or t['trader'] == search]
    return trades


@app.get('/filterTrades')
def filter_trades(assetclass: Optional[str] = Query(None, title="assetClass", description="Asset class of the trade."),
                  end: Optional[dt.datetime] = Query(None, title="endDate", description="The maximum date for the tradeDateTime field."),
                  maxprice: Optional[float] = Query(None, title="maxPrice", description="The maximum value for the tradeDetails.price field."),
                  minprice: Optional[float] = Query(None, title="minPrice",description="The minimum value for the tradeDetails.price field."),
                  start: Optional[dt.datetime] = Query(None, title="startDate", description="The minimum date for the tradeDateTime field."),
                  tradetype: Optional[str] = Query(None, title="tradeType", description="The tradeDetails.buySellIndicator is a BUY or SELL")):
    filtered = data
    if assetclass is not None:
        filtered = [t for t in filtered if t['assetClass'] == assetclass]

    if end is not None and start is not None:
        filtered = [t for t in filtered if end > dt.datetime.fromisoformat(t['tradeDateTime']) > start]

    if maxprice is not None and minprice is not None:
        filtered = [t for t in filtered if maxprice > t['tradeDetails']['price'] > minprice]

    if tradetype is not None:
        filtered = [t for t in filtered if t['tradeDetails']['buySellIndicator'] == tradetype]

    return filtered
