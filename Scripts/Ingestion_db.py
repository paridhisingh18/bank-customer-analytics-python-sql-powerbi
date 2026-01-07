#Importing Libraries
import pandas as pd
import os
from sqlalchemy import create_engine , URL , text
from dotenv import load_dotenv
import logging


#Creating logging
logging.basicConfig (
    filename = "logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode = "a"
)

logger = logging.getLogger(__name__)

#Loading env vars
load_dotenv()

DB_CONFIG = {
    "user": os.getenv('DB_USER'),
    "password": os.getenv('DB_PASS'),
    "host": os.getenv('DB_HOST','localhost'),
    "port": os.getenv('DB_PORT','5432'),
    "database": os.getenv("DB_NAME")
}

#Creating URL and Engine
url = URL.create(
    drivername = "postgresql+psycopg2",
    username = DB_CONFIG["user"],
    password = DB_CONFIG["password"],
    host = DB_CONFIG["host"],
    port= DB_CONFIG["port"],
    database = DB_CONFIG["database"]
)

engine =create_engine(url)


try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        version = result.fetchone()[0]
        logger.info(f"Connected ! Version: {version}")
except Exception as e:
    logger.error(f"Connection failed: {e}")
    raise

# Loading csv to table
def load_csv(csv_path , table_name = "bank_customer" , chunksize = None):
    try:
        logger.info(f"Starting to load CSV: {csv_path}")

        #Reading CSV 
        df = pd.read_csv(csv_path)
        logger.info(f"Read{len(df)} rows from {csv_path}")

        #Loading to DB 
        df.to_sql(table_name , engine, if_exists = 'replace', index= False , chunksize = chunksize )
        logger.info(f"Successfully loaded {len(df)} raw data to {table_name}")
    except Exception as e:
        logger.error(f"Error loading CSV :{e}")
        raise

if __name__ == "__main__" :
    logger.info("Script started")
    load_csv('Downloads/Customer.csv')
    logger.info("Script completed")


engine.dispose()
logger.info("Engine disposed")
    

