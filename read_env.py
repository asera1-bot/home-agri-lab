import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

host = "localhost"
port = os.getenv("POSTGRES_PORT")
dbname = os.getenv("POSTGRES_DB")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")

conn = psycopg.connect(
    host=host,
    port=port,
    dbname=dbname,
    user=user,
    password=password
)

print(conn)
