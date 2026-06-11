from langchain.tools import tool
import yfinance as yf

@tool
def get_technical_indicators(symbol: str) -> str:

    """
    Get technical analysis indicators including
    SMA20, SMA50, moving averages and trend direction.
    Useful for buy or sell decisions.
    """

    df = yf.download(symbol, period="6mo")

    sma20 = df["Close"].rolling(20).mean().iloc[-1]
    sma50 = df["Close"].rolling(50).mean().iloc[-1]

    current = df["Close"].iloc[-1]

    return f"""
    Current Price: {current}
    SMA20: {sma20}
    SMA50: {sma50}
    """