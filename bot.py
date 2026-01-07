import telegram
‎import yfinance as yf
‎import pandas as pd
‎from ta.trend import EMAIndicator
‎from ta.momentum import RSIIndicator
‎from ta.volatility import BollingerBands
‎import time
‎
‎TOKEN = 8543011308:AAGHqqUtZr4DnVzhbtp6cq1mTGtxoyMHYUg
‎CHAT_ID = -5273964410
‎
‎bot = telegram.Bot(token=TOKEN)
‎
‎pairs = {
‎    "EURUSD": "EURUSD=X",
‎    "GBPUSD": "GBPUSD=X",
‎    "USDJPY": "JPY=X",
‎    "EURJPY": "EURJPY=X",
‎    "GBPJPY": "GBPJPY=X",
‎    "AUDUSD": "AUDUSD=X",
‎    "USDCAD": "CAD=X",
‎    "NZDUSD": "NZDUSD=X",
‎    "EURGBP": "EURGBP=X"
‎}
‎
‎def send_signal(msg):
‎    bot.send_message(chat_id=CHAT_ID, text=msg)
‎
‎while True:
‎    for pair, symbol in pairs.items():
‎        data = yf.download(symbol, interval="5m", period="2d")
‎        close = data["Close"]
‎
‎        ema20 = EMAIndicator(close, 20).ema_indicator()
‎        ema50 = EMAIndicator(close, 50).ema_indicator()
‎        rsi = RSIIndicator(close, 14).rsi()
‎        bb = BollingerBands(close)
‎
‎        price = close.iloc[-1]
‎
‎        if ema20.iloc[-1] > ema50.iloc[-1] and rsi.iloc[-1] <= 35 and price <= bb.bollinger_lband().iloc[-1]:
‎            send_signal(f"📈 SIGNAL CALL\nActif: {pair}\nTF: 5m\nExpiration: 5m")
‎
‎        if ema20.iloc[-1] < ema50.iloc[-1] and rsi.iloc[-1] >= 65 and price >= bb.bollinger_hband().iloc[-1]:
‎            send_signal(f"📉 SIGNAL PUT\nActif: {pair}\nTF: 5m\nExpiration: 5m")
‎
‎    time.sleep(300)
‎
