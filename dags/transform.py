from prefect import task

@task
def transform(df):
    """Seleciona e renomeia colunas relevantes."""
    df = df[["Date", "Open", "High", "Low", "Close", "Volume"]]
    df.columns = ["date", "open", "high", "low", "close", "volume"]
    return df