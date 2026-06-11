# tools/stock_price.py

from langchain.tools import tool
import yfinance as yf


@tool
def get_stock_price(symbol: str) -> str:
    """
    Get the latest stock price, market capitalization,
    valuation metrics and current trading information.
    """

    stock = yf.Ticker(symbol)

    info = stock.info

    return f"""
    Company: {info.get('longName')}
    Current Price: {info.get('currentPrice')}
    Market Cap: {info.get('marketCap')}
    PE Ratio: {info.get('trailingPE')}
    """