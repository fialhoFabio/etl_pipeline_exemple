from prefect import flow
from extract import extract
from transform import transform
from load import load

@flow
def etl_pipeline():
    """Executa o pipeline ETL completo."""
    data = extract()
    cleaned_data = transform(data)
    load(cleaned_data)

if __name__ == "__main__":
    etl_pipeline()