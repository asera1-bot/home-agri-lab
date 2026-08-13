import os
import psycopg
from dotenv import load_dotenv

from extract_market_price import load_csv
from transform_monthly_market_price import trans_record

rows = load_csv()
monthly_records = trans_record(rows)

load_dotenv()

conn = psycopg.connect(
    host="localhost",
    port=os.getenv("POSTGRES_PORT"),
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)

cur = conn.cursor()

for record in monthly_records:
    cur.execute(
        """
        INSERT INTO monthly_market_price(
        year,
        month,
        origin_prefecture,
        crop,
        quantity_kg,
        price_yen_per_kg,
        market
        )
        VALUES (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
        )
        ON CONFLICT (
            year,
            month,
            origin_prefecture,
            crop,
            market
        )
        DO NOTHING
        """,
        (
            record["year"],
            record["month"],
            record["origin_prefecture"],
            record["crop"],
            record["quantity_kg"],
            record["price_yen_per_kg"],
            record["market"]
        )
)

conn.commit()
cur.close()
conn.close()
