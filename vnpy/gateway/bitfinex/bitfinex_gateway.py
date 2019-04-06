# encoding: UTF-8
"""
"""

import hashlib
import hmac
import sys,json
import time
from copy import copy
from datetime import datetime
from urllib.parse import urlencode

from requests import ConnectionError

from vnpy.api.rest import Request, RestClient
from vnpy.api.websocket import WebsocketClient

from vnpy.trader.constant import (
    Direction,
    Exchange,
    PriceType,
    Product,
    Status,
)
from vnpy.trader.gateway import BaseGateway
from vnpy.trader.object import (
    TickData,
    OrderData,
    TradeData,
    PositionData,
    AccountData,
    ContractData,
    OrderRequest,
    CancelRequest,
    SubscribeRequest,
)

BASE_URL = "https://api.bitfinex.com/"
KEY = "DdxG9mA8RUkC7ThevEO6byRj6ezEqWDCeNKvOomJdPk"
#KEY = "DdxG9mA8RUkC7ThevEO6byRj6ezEqWDCeNKvOomJdPk"
SECRET = "dhxB6m0q9jwyZAwPJC6HlO16fEduyOfcEpMyC0Ow4rD"

REST_HOST = "https://api.bitfinex.com/"
WEBSOCKET_HOST = "wss://api-pub.bitfinex.com/ws/2"

STATUS_BITFINEX2VT = {
    "ACTIVE": Status.NOTTRADED,
    "PARTIALLY FILLED": Status.PARTTRADED,
    "EXECUTED": Status.ALLTRADED,
    "CANCELED": Status.CANCELLED,
   # "Rejected": Status.REJECTED,
}

PRICETYPE_VT2BITFINEX = {PriceType.LIMIT: "EXCHANGE LIMIT", PriceType.MARKET: "EXCHANGE MARKET"}
DIRECTION_VT2BITFINEX = {Direction.LONG: "Buy", Direction.SHORT: "Sell"}
"""

STATUS_BITMEX2VT = {
    "New": Status.NOTTRADED,
    "Partially filled": Status.PARTTRADED,
    "Filled": Status.ALLTRADED,
    "Canceled": Status.CANCELLED,
    "Rejected": Status.REJECTED,
}

DIRECTION_BITMEX2VT = {v: k for k, v in DIRECTION_VT2BITMEX.items()}
PRICETYPE_VT2BITMEX = {PriceType.LIMIT: "Limit", PriceType.MARKET: "Market"}
"""


class BitfinexGateway(BaseGateway):
    """
    VN Trader Gateway for bitfineX connection.
    """

    default_setting = {
        "key": "DdxG9mA8RUkC7ThevEO6byRj6ezEqWDCeNKvOomJdPk",
        "secret": "dhxB6m0q9jwyZAwPJC6HlO16fEduyOfcEpMyC0Ow4rD",
        "session": 3,
        "proxy_host": "127.0.0.1",
        "proxy_port": 1080,
    }

    def __init__(self, event_engine):
        """Constructor"""
        super(BitfinexGateway, self).__init__(event_engine, "BITFINEX")

        self.rest_api = BitfinexRestApi(self)
        self.ws_api = BitfinexWebsocketApi(self)

    def connect(self, setting: dict):
        """"""
        key = setting["key"]
        secret = setting["secret"]
        session = setting["session"]
        proxy_host = setting["proxy_host"]
        proxy_port = setting["proxy_port"]

        self.rest_api.connect(key, secret, session, proxy_host, proxy_port)

        self.ws_api.connect(key, secret, proxy_host, proxy_port)

    def subscribe(self, req: SubscribeRequest):
        """"""
        self.ws_api.subscribe(req)

    def send_order(self, req: OrderRequest):
        """"""
        #return self.rest_api.send_order(req)
        return self.ws_api.send_order(req)

    def cancel_order(self, req: CancelRequest):
        """"""
        self.rest_api.cancel_order(req)

    def query_account(self):
        """"""
        pass

    def query_position(self):
        """"""
        pass

    def close(self):
        """"""
        self.rest_api.stop()
        self.ws_api.stop()


class BitfinexRestApi(RestClient):
    """
    BitfineX REST API
    """

    def __init__(self, gateway: BaseGateway):
        """"""
        super(BitfinexRestApi, self).__init__()

        self.gateway = gateway
        self.gateway_name = gateway.gateway_name

        self.key = ""
        self.secret = ""

        self.order_count = 1_000_000
        self.connect_time = 0
        print(self.gateway_name , self.key ,self.secret,self.order_count, self.connect_time)

    def sign(self, request):
        """
        Generate BitfineX signature.
        """
        # Sign
        nonce = str(int(round(time.time() * 1000000)))

        if request.params:
            query = urlencode(request.params)
            path = request.path + "?" + query
        else:
            path = request.path

        if request.data:
            request.data = urlencode(request.data)
        else:
            request.data = ""

        msg = request.method + "/api/v2/{}{}{}".format(path, nonce, request.data)
        #print("secret type",type(self.secret), "| secret: " ,self.secret)
        #print("msg type",type(msg))
        signature = hmac.new(
            #self.secret.encode("utf8"), msg.encode("utf8"), digestmod=hashlib.sha384
            self.secret, msg.encode("utf8"), digestmod=hashlib.sha384
        ).hexdigest()

        # Add headers
        headers = {
            "bfx-nonce": nonce,
            "bfx-apikey": self.key,
            "bfx-signature": signature,
            "content-type": "application/json"
        }

        request.headers = headers
        return request

    def connect(
        self,
        key: str,
        secret: str,
        session: int,
        proxy_host: str,
        proxy_port: int,
    ): 
        """
               Initialize connection to REST server.
        """
        self.key = key
        self.secret = secret.encode()

        self.connect_time = (
            int(datetime.now().strftime("%y%m%d%H%M%S")) * self.order_count
        )

        self.init(REST_HOST, proxy_host, proxy_port)
        print("rest connect: ",REST_HOST, proxy_host, proxy_port)
        self.start(session)
        print("rest client connected")
        self.gateway.write_log("REST API启动成功")

    def send_order(self, req: OrderRequest):
        """"""
        self.order_count += 1
        orderid = str(self.connect_time + self.order_count)
        print("[debug in send_order req]: ")
        print(req.__dict__)
        data = {
            "symbol": req.symbol,
            "side": DIRECTION_VT2BITFINEX[req.direction],
            "ordType": PRICETYPE_VT2BITFINEX[req.price_type],
            "price": req.price,
            "orderQty": int(req.volume),
            "clOrdID": orderid,
        }

        print("debug send_order  data: ")
        print(data)
        # Only add price for limit order.
        if req.price_type == PriceType.LIMIT:
            data["price"] = req.price

        order = req.create_order_data(orderid, self.gateway_name)
        print("debug send_order: ")
        print(order)
        self.add_request(
            "POST",
            "/v2/auth/r/orders",
            callback=self.on_send_order,
            data=data,
            extra=order,
            on_failed=self.on_send_order_failed,
            on_error=self.on_send_order_error,
        )

        print("begin to call on order")
        self.gateway.on_order(order)
        return order.vt_orderid

    def cancel_order(self, req: CancelRequest):
        """"""
        orderid = req.orderid

        if orderid.isdigit():
            params = {"clOrdID": orderid}
        else:
            params = {"orderID": orderid}

        self.add_request(
            "DELETE",
            "/order",
            callback=self.on_cancel_order,
            params=params,
            on_error=self.on_cancel_order_error,
        )

    def on_send_order_failed(self, status_code: str, request: Request):
        """
        Callback when sending order failed on server.
        """
        order = request.extra
        order.status = Status.REJECTED
        self.gateway.on_order(order)

        msg = f"委托失败，状态码：{status_code}，信息：{request.response.text}"
        self.gateway.write_log(msg)

    def on_send_order_error(
        self, exception_type: type, exception_value: Exception, tb, request: Request
    ):
        """
        Callback when sending order caused exception.
        """
        order = request.extra
        order.status = Status.REJECTED
        self.gateway.on_order(order)

        # Record exception if not ConnectionError
        if not issubclass(exception_type, ConnectionError):
            self.on_error(exception_type, exception_value, tb, request)

    def on_send_order(self, data, request):
        """"""
        print("debug on_send_order")
        print(data)
        print(request)
        pass

    def on_cancel_order_error(
        self, exception_type: type, exception_value: Exception, tb, request: Request
    ):
        """
        Callback when cancelling order failed on server.
        """
        # Record exception if not ConnectionError
        if not issubclass(exception_type, ConnectionError):
            self.on_error(exception_type, exception_value, tb, request)

    def on_cancel_order(self, data, request):
        """"""
        pass

    def on_failed(self, status_code: int, request: Request):
        """
        Callback to handle request failed.
        """
        msg = f"请求失败，状态码：{status_code}，信息：{request.response.text}"
        self.gateway.write_log(msg)

    def on_error(
        self, exception_type: type, exception_value: Exception, tb, request: Request
    ):
        """
        Callback to handler request exception.
        """
        msg = f"触发异常，状态码：{exception_type}，信息：{exception_value}"
        self.gateway.write_log(msg)

        sys.stderr.write(
            self.exception_detail(exception_type, exception_value, tb, request)
        )


class BitfinexWebsocketApi(WebsocketClient):
    """"""

    def __init__(self, gateway):
        """"""
        super(BitfinexWebsocketApi, self).__init__()

        self.gateway = gateway
        self.gateway_name = gateway.gateway_name
        self.orderId = 1000000
        self.date = int(datetime.now().strftime('%y%m%d%H%M%S')) * self.orderId
        self.key = ""
        self.secret = ""

        self.callbacks = {
            "trade": self.on_tick,
            "orderBook10": self.on_depth,
            "execution": self.on_trade,
            "order": self.on_order,
            "position": self.on_position,
            "margin": self.on_account,
            "instrument": self.on_contract,
        }

        self.ticks = {}
        self.accounts = {}
        self.orders = {}
        self.trades = set()
        self.tickDict = {}
        self.bidDict = {}
        self.askDict = {}
        self.orderLocalDict = {}
        self.channelDict = {}       # ChannelID : (Channel, Symbol)


    def connect(
        self, key: str, secret: str,  proxy_host: str, proxy_port: int
    ):
        """"""
        self.key = key
        self.secret = secret.encode()

        self.init(WEBSOCKET_HOST, proxy_host, proxy_port)

        self.start()

    def subscribe(self, req: SubscribeRequest):
        """
        Subscribe to tick data upate.
        """
        print("debug subscribe: ")
        print( req.__dict__)
        #self.ticks[req.symbol] = tick
        # vigar need need to modify  channel/symbol
        d = {
            'event': 'subscribe',
            'channel': 'book',
            'symbol': 'BTCUSD'
        }
        print(d)
        self.send_packet(d)

    def send_order(self, req: OrderRequest):
        self.orderId += 1
        orderid = str(self.date + self.orderId)
        vtOrderID = '.'.join([self.gateway_name, str(orderid)])
        
        if req.direction == Direction.LONG:
            amount = req.volume
        else:
            amount = -req.volume
            
        o = {
            'cid': orderid,
            'type': PRICETYPE_VT2BITFINEX[req.price_type],
            'symbol': 't' + req.symbol,
            'amount': str(amount),
            'price': str(req.price)
        }
        
        req = [0, 'on', None, o]
        print("send_order in ws: " , req)
        #self.sendReq(req)
        self.send_packet(req)
        
        return vtOrderID

    def on_connected(self):
        """"""
        self.gateway.write_log("Websocket API连接成功")
        self.authenticate()

    def on_disconnected(self):
        """"""
        self.gateway.write_log("Websocket API连接断开")

    # need debug 20190404
    def on_packet(self, packet: dict):
        """"""
        #print("on_packet func", type(packet))
        #print(packet)

        if isinstance(packet, dict):
            self.onResponse(packet)
        else:
            self.onUpdate(packet)

    #----------------------------------------------------------------------
    def onResponse(self, data):
        """"""
        print("onResponse func", type(data))
        print(data)
        if 'event' not in data:
            return
        
        if data['event'] == 'subscribed':
            symbol = str(data['symbol'].replace('t', ''))
            #symbol = str(data['symbol'])
            self.channelDict[data['chanId']] = (data['channel'], symbol)
    
    #----------------------------------------------------------------------
    def onUpdate(self, data):
        """"""
        if data[1] == u'hb':
            return
        
        channelID = data[0]
        
        if not channelID:
            self.onTradeUpdate(data)
        else:
            self.onDataUpdate(data)
    
    #----------------------------------------------------------------------
    def onDataUpdate(self, data):
        """"""
        print("debug onDataUpdate", data)
        channelID = data[0]
        channel, symbol = self.channelDict[channelID]
        print("debug onDataUpdate channel_symbol", channel, symbol)
        symbol = str(symbol.replace('t', ''))
        #symbol = str(symbol)
        
        # 获取Tick对象
        if symbol in self.tickDict:
            tick = self.tickDict[symbol]
        else:
            tick = TickData(
                symbol=symbol,
                exchange=Exchange.BITFINEX,
                name=symbol,
                datetime=datetime.now(),
                gateway_name=self.gateway_name,
            )
            #tick.vtSymbol = '.'.join([tick.symbol, tick.exchange])
            
            self.tickDict[symbol] = tick
        
        l = data[1]
        
        # 常规行情更新
        if channel == 'ticker':
            tick.volume = float(l[-3])
            tick.highPrice = float(l[-2])
            tick.lowPrice = float(l[-1])
            tick.lastPrice = float(l[-4])
            tick.openPrice = float(tick.lastPrice - l[4])
        # 深度报价更新
        elif channel == 'book':
            bid = self.bidDict.setdefault(symbol, {})
            ask = self.askDict.setdefault(symbol, {})
            
            if len(l) > 3:
                for price, count, amount in l:
                    price = float(price)
                    count = int(count)
                    amount = float(amount)
                    
                    if amount > 0:
                        bid[price] = amount
                    else:
                        ask[price] = -amount
            else:
                price, count, amount = l
                price = float(price)
                count = int(count)
                amount = float(amount)                
                
                if not count:
                    if price in bid:
                        del bid[price]
                    elif price in ask:
                        del ask[price]
                else:
                    if amount > 0:
                        bid[price] = amount
                    else:
                        ask[price] = -amount
            
            # Bitfinex的深度数据更新是逐档推送变动情况，而非5档一起推
            # 因此会出现没有Bid或者Ask的情况，这里使用try...catch过滤
            # 只有买卖深度满足5档时才做推送
            try:
                # BID
                bid_keys = bid.keys()
                #bidPriceList.sort(reverse=True)
                bidPriceList = sorted(bid_keys, reverse=True)
                
                tick.bidPrice1 = bidPriceList[0]
                tick.bidPrice2 = bidPriceList[1]
                tick.bidPrice3 = bidPriceList[2]
                tick.bidPrice4 = bidPriceList[3]
                tick.bidPrice5 = bidPriceList[4]
                
                tick.bidVolume1 = bid[tick.bidPrice1]
                tick.bidVolume2 = bid[tick.bidPrice2]
                tick.bidVolume3 = bid[tick.bidPrice3]
                tick.bidVolume4 = bid[tick.bidPrice4]
                tick.bidVolume5 = bid[tick.bidPrice5]
                
                # ASK
                ask_keys = ask.keys()
                #askPriceList.sort()
                askPriceList = sorted(ask_keys, reverse=True)
                
                tick.askPrice1 = askPriceList[0]
                tick.askPrice2 = askPriceList[1]
                tick.askPrice3 = askPriceList[2]
                tick.askPrice4 = askPriceList[3]
                tick.askPrice5 = askPriceList[4]
                
                tick.askVolume1 = ask[tick.askPrice1]
                tick.askVolume2 = ask[tick.askPrice2]
                tick.askVolume3 = ask[tick.askPrice3]
                tick.askVolume4 = ask[tick.askPrice4]
                tick.askVolume5 = ask[tick.askPrice5]  
            except IndexError:
                return            
        
        dt = datetime.now()
        tick.date = dt.strftime('%Y%m%d')
        tick.time = dt.strftime('%H:%M:%S.%f')
        tick.datetime = dt
        
        # 推送
        self.gateway.on_tick(copy(tick))

    #----------------------------------------------------------------------
    def onWallet(self, data):
        """"""
        if str(data[0]) == 'exchange':
            accountid = str(data[1])
            account = self.accounts.get(accountid, None)
            if not account:
                account = AccountData(accountid=accountid, gateway_name=self.gateway_name)
            
            account.vtAccountID = '.'.join([account.gateway_name, account.accountid])
            account.balance = float(data[2])
            account.available = None if not data[-1] else float(data[-1])
            if account.available and account.balance:
                account.frozen = account.balance - account.available
            self.gateway.on_account(copy(account))

    #----------------------------------------------------------------------
    def onTradeUpdate(self, data):
        """"""
        print("debug onTradeUpdate: " , data)
        name = data[1]
        info = data[2]
        
        if name == 'ws':
            for l in info:
                self.onWallet(l)
            self.gateway.write_log(u'账户资金获取成功')
        elif name == 'wu':
            self.onWallet(info)
        elif name == 'os':
            for l in info:
                self.onOrder(l)
            self.gateway.write_log(u'活动委托获取成功')
        elif name in ['on', 'ou', 'oc']:
            self.onOrder(info)
        elif name == 'te':
            self.onTrade(info)

    def on_error(self, exception_type: type, exception_value: Exception, tb):
        """"""
        msg = f"触发异常，状态码：{exception_type}，信息：{exception_value}"
        self.gateway.write_log(msg)

        sys.stderr.write(self.exception_detail(
            exception_type, exception_value, tb))

    # debug OK , 0405 
    def authenticate(self):
        """
            Authenticate websocket connection to subscribe private topic.
        """
        nonce = int(time.time() * 1000000)
        authPayload = 'AUTH' + str(nonce)
        signature = hmac.new(
            self.secret, authPayload.encode(), digestmod=hashlib.sha384
        ).hexdigest()

        req = {
            'apiKey': self.key,
            'event': 'auth',
            'authPayload': authPayload,
            'authNonce': nonce,
            'authSig': signature
        }

        self.send_packet(req)

    def subscribe_topic(self):
        """
        Subscribe to all private topics.
        """
        req = {
            "op": "subscribe",
            "args": [
                "instrument",
                "trade",
                "orderBook10",
                "execution",
                "order",
                "position",
                "margin",
            ],
        }
        self.send_packet(req)

    def on_tick(self, d):
        """"""
        symbol = d["symbol"]
        tick = self.ticks.get(symbol, None)
        if not tick:
            return

        tick.last_price = d["price"]
        tick.datetime = datetime.strptime(
            d["timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        self.gateway.on_tick(copy(tick))

    def on_depth(self, d):
        """"""
        symbol = d["symbol"]
        tick = self.ticks.get(symbol, None)
        if not tick:
            return

        for n, buf in enumerate(d["bids"][:5]):
            price, volume = buf
            tick.__setattr__("bid_price_%s" % (n + 1), price)
            tick.__setattr__("bid_volume_%s" % (n + 1), volume)

        for n, buf in enumerate(d["asks"][:5]):
            price, volume = buf
            tick.__setattr__("ask_price_%s" % (n + 1), price)
            tick.__setattr__("ask_volume_%s" % (n + 1), volume)

        tick.datetime = datetime.strptime(
            d["timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        self.gateway.on_tick(copy(tick))

    def on_trade(self, d):
        """"""
        # Filter trade update with no trade volume and side (funding)
        if not d["lastQty"] or not d["side"]:
            return

        tradeid = d["execID"]
        if tradeid in self.trades:
            return
        self.trades.add(tradeid)

        if d["clOrdID"]:
            orderid = d["clOrdID"]
        else:
            orderid = d["orderID"]

        trade = TradeData(
            symbol=d["symbol"],
            exchange=Exchange.BITFINEX,
            orderid=orderid,
            tradeid=tradeid,
            direction=DIRECTION_BITMEX2VT[d["side"]],
            price=d["lastPx"],
            volume=d["lastQty"],
            time=d["timestamp"][11:19],
            gateway_name=self.gateway_name,
        )

        self.gateway.on_trade(trade)

    def on_order(self, d):
        """"""
        if "ordStatus" not in d:
            return

        sysid = d["orderID"]
        order = self.orders.get(sysid, None)
        if not order:
            if d["clOrdID"]:
                orderid = d["clOrdID"]
            else:
                orderid = sysid

            # time = d["timestamp"][11:19]

            order = OrderData(
                symbol=d["symbol"],
                exchange=Exchange.BITMEX,
                orderid=orderid,
                direction=DIRECTION_BITMEX2VT[d["side"]],
                price=d["price"],
                volume=d["orderQty"],
                time=d["timestamp"][11:19],
                gateway_name=self.gateway_name,
            )
            self.orders[sysid] = order

        order.traded = d.get("cumQty", order.traded)
        order.status = STATUS_BITMEX2VT.get(d["ordStatus"], order.status)

        self.gateway.on_order(copy(order))

    def on_position(self, d):
        """"""
        position = PositionData(
            symbol=d["symbol"],
            exchange=Exchange.BITMEX,
            direction=Direction.NET,
            volume=d["currentQty"],
            gateway_name=self.gateway_name,
        )

        self.gateway.on_position(position)

    def on_account(self, d):
        """"""
        accountid = str(d["account"])
        account = self.accounts.get(accountid, None)
        if not account:
            account = AccountData(accountid=accountid,
                                  gateway_name=self.gateway_name)
            self.accounts[accountid] = account

        account.balance = d.get("marginBalance", account.balance)
        account.available = d.get("availableMargin", account.available)
        account.frozen = account.balance - account.available

        self.gateway.on_account(copy(account))

    def on_contract(self, d):
        """"""
        if "tickSize" not in d:
            return

        if not d["lotSize"]:
            return

        contract = ContractData(
            symbol=d["symbol"],
            exchange=Exchange.BITMEX,
            name=d["symbol"],
            product=Product.FUTURES,
            pricetick=d["tickSize"],
            size=d["lotSize"],
            gateway_name=self.gateway_name,
        )

        self.gateway.on_contract(contract)

