
import json
import requests
import asyncio
import websockets

class EquosWSClient():

    symbolToPairId = {}
    timespan_mappings = {
        '1m': 1,
        '5m': 2,
        '15m': 3,
        '1h': 4,
        '6h': 5,
        '1d': 6,
        '7d': 7,
    }

    def __init__(self, _username: str, _password: str, _userId: str):
        super().__init__()
        self.base_uri = 'wss://equos.io/ws'
        self.restURI = 'https://equos.io/api'
        self.username = _username
        self.password = _password
        self.userId = _userId
        self.fetchMarkets()

    def fetchMarkets(self):
        r = requests.get(self.restURI + '/getInstrumentPairs')
        markets = r.json().get('instrumentPairs')
        for pair in markets:
            self.symbolToPairId[pair[1]] = pair[0]

    def fetch_ws_orderbook_stream(self, symbol):
        asyncio.get_event_loop().run_until_complete(self._orderbook(symbol))

    def fetch_ws_trade_history_stream(self, symbol):
        asyncio.get_event_loop().run_until_complete(self._trade_history(symbol))

    def fetch_ws_ohlc_stream(self, symbol, timespan):
        asyncio.get_event_loop().run_until_complete(self._ohlc(symbol, timespan))

    def fetch_ws_orders_stream(self, account = None):
        asyncio.get_event_loop().run_until_complete(self._orders(account))

    def fetch_ws_positions_stream(self, account = None):
        loop = asyncio.get_event_loop().run_until_complete(self._positions(account))
        loop.run_until_complete()

    def fetch_ws_risk_stream(self, account = None):
        asyncio.get_event_loop().run_until_complete(self._risk(account))

    async def _orderbook(self, symbol):
        pairId = self.symbolToPairId.get(symbol, None)

        if pairId is None:
            raise Exception(f"Unable to subscribe to orderbook as pairId is not valid. Pair ID mappings are: {self.symbolToPairId}")

        uri = self.base_uri + '/orderbook'

        async with websockets.connect(uri) as websocket:
            await websocket.send(json.dumps({'pairId': pairId}))
            while True:
                res = await websocket.recv()
                print(res)
                # Do whatever business logic you want here

    async def _trade_history(self, symbol):
        pairId = self.symbolToPairId.get(symbol, None)

        if pairId is None:
            raise Exception(f"Unable to subscribe to orderbook as pairId is not valid. Pair ID mappings are: {self.symbolToPairId}")

        uri = self.base_uri + '/tradehistory'

        async with websockets.connect(uri) as websocket:
            await websocket.send(json.dumps({'pairId': pairId}))
            while True:
                res = await websocket.recv()
                print(res)
                # Do whatever business logic you want here
 
    async def _ohlc(self, symbol, timespan):
        pairId = self.symbolToPairId.get(symbol, None)

        if pairId is None:
            raise Exception(f"Unable to subscribe to orderbook as pairId is not valid. Pair ID mappings are: {self.symbolToPairId}")

        timespanInt = self.timespan_mappings.get(timespan, None)

        if timespanInt is None:
            raise Exception(f"Unable to subscribe to orderbook as timespanInt is not valid. Timespan ID mappings are: {self.timespan_mappings}")

        uri = self.base_uri + '/chart'

        async with websockets.connect(uri) as websocket:
            await websocket.send(json.dumps({'pairId': pairId, 'timespan': timespanInt}))
            while True:
                res = await websocket.recv()
                print(res)
                # Do whatever business logic you want here
 
    async def _orders(self, account = None):
        uri = self.base_uri + '/userorders'
        params = {'login': self.username, 'password': self.password, 'userId': self.userId}

        if account is not None:
            params['account'] = account

        payload = json.dumps(params)
        payload = payload.replace(" ", "")

        print(f"payload is: {payload}")
        async with websockets.connect(uri) as websocket:
            await websocket.send(payload)
            while True:
                res = await websocket.recv()
                print(res)
                # Do whatever business logic you want here

    async def _positions(self, account = None):
        uri = self.base_uri + '/userposition'
        params = {'login': self.username, 'password': self.password, 'userId': self.userId}

        if account is not None:
            params['account'] = account

        payload = json.dumps(params)
        payload = payload.replace(" ", "")

        print(f"payload is: {payload}")
        async with websockets.connect(uri) as websocket:
            await websocket.send(payload)
            while True:
                res = await websocket.recv()
                print(res)
                # Do whatever business logic you want here

    async def _risk(self, account = None):
        uri = self.base_uri + '/userrisk'
        params = {'login': self.username, 'password': self.password, 'userId': self.userId}

        if account is not None:
            params['account'] = account

        payload = json.dumps(params)
        payload = payload.replace(" ", "")

        print(f"payload is: {payload}")
        async with websockets.connect(uri) as websocket:
            await websocket.send(payload)
            while True:
                res = await websocket.recv()
                print(res)
                # Do whatever business logic you want here
