from langchain.tools import tool
import yfinance as yf

@tool
def get_company_fundamentals(symbol: str) -> str:

    """
    Get company fundamentals including PE ratio,
    EPS, ROE, debt-to-equity ratio,
    profit margins and financial health.
    """

    stock = yf.Ticker(symbol)

    info = stock.info

    return f"""
    Company: {info.get('longName')}
    PE Ratio: {info.get('trailingPE')}
    EPS: {info.get('trailingEps')}
    ROE: {info.get('returnOnEquity')}
    Debt To Equity: {info.get('debtToEquity')}
    Profit Margin: {info.get('profitMargins')}
    """