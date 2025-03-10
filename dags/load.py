from prefect import task
import psycopg2

@task
def load(df):
    """Carrega os dados no PostgreSQL."""
    conn = psycopg2.connect(
        dbname="finance_data_db", user="admin", password="admin", host="localhost"
    )
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stock_data (
            date DATE PRIMARY KEY,
            open FLOAT,
            high FLOAT,
            low FLOAT,
            close FLOAT,
            volume BIGINT
        )
    """)

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO stock_data (date, open, high, low, close, volume)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (date) DO NOTHING
        """, (row["date"], row["open"], row["high"], row["low"], row["close"], row["volume"]))

    conn.commit()
    conn.close()