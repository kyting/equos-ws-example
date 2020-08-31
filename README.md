# EQUOS Websocket API Python example

**NOTE: This class is a sample only and does not come with warranties. I do not take responsibility for any losses due to this API. Use at your own risk!**

This repository contains an example class which allows one to connect to Equos' Websocket API. 

## How to use this class

**Functions do not process any data - they only return them**. If you'd like them to process data to suit your purposes, you'll have to do it yourself. 

To start, import the script as follows:

```
from EquosWSClient import EquosWSClient

# Instantiate the client
client = EquosWSClient('username', 'password', 'userId')
```

Where:

* `username` is your username which is used to log into the Equos website.
* `password` is the password for your account
* `userId` is the last non-zero digits of the `Sender Comp Id` in the Settings > API page

After instatiation, you will be able to call one of the following functions:

* `fetch_ws_orderbook_stream(symbol)` - Subscribes to the public [orderbook websocket stream](https://developer.equos.io/#order-book-channel)
* `fetch_ws_trade_history_stream(symbol)` - Subscribes to the public [trade history websocket stream](https://developer.equos.io/#trade-history-channel)
* `fetch_ws_ohlc_stream(symbol, timespan)` - Subscribes to the public [candles websocket stream](https://developer.equos.io/#chart-channel)
* `fetch_ws_orders_stream()` - Subscribes to the private [orders websocket stream](https://developer.equos.io/#user-orders-channel). Requires `account` if you are an institutional user.
* `fetch_ws_positions_stream()` - Subscribes to the private [positions websocket stream](https://developer.equos.io/#user-position-channel). Requires `account` if you are an institutional user.
* `fetch_ws_risk_stream()` - Subscribes to the private [risk websocket stream](https://developer.equos.io/#user-risk-channel). Requires `account` if you are an institutional user.

For example, after instantiation, you can call the orderbook as follows:

```
client.fetch_ws_orderbook_stream("BTC/USDC")
```

Timespan mappings for charts are as follows:

* 1 Minute: '1m'
* 5 Minutes: '5m'
* 15 Minutes: '15m'
* 1 Hour: '1h'
* 6 Hours: '6h'
* 1 Day: '1d'
* 1 Week: '7d'