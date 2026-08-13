from extract_market_price import load_csv

def trans_record(rows):
    monthly_records = []

    for row in rows:
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

    return monthly_records

if __name__ == "__main__":
    rows = load_csv()
    monthly_records = trans_record(rows)
