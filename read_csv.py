import os
import psycopg
from dotenv import load_dotenv
import csv

monthly_records = []

with open("data/raw/SCH7020.csv", mode="r", encoding="cp932") as f:
    reader = csv.reader(f)

    for row in reader:
        if row and row[0] == "神奈川":
            for month, i in enumerate(range(2, 20, 3), start=1):
            
                record = {
                    "year": 2026,
                    "month": month,
                    "origin_prefecture": "神奈川",
                    "crop": "ミニトマト",
                    "quantity_kg": int(row[i]),
                    "price_yen_per_kg": int(row[i+1]),
                    "market": "東京都中央市場計"
                }

                monthly_records.append(record)
                
    for records in monthly_records:
        print(
            records["year"],
            records["month"],
            records["origin_prefecture"],
            records["crop"],
            records["quantity_kg"],
            records["price_yen_per_kg"],
            records["market"]
        )

print(monthly_records)

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
        INSERT INTO monthly_market_price (
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
