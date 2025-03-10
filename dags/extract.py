from prefect import task
import yfinance as yf

@task
def extract(ticker="ITSA4.SA"):
    """Baixa dados de ações do Yahoo Finance."""
    stock = yf.download(ticker, period="1d")
    stock.reset_index(inplace=True)
    return stock