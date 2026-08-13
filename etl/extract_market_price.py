import csv

def load_csv():

    rows = []

    with open("data/raw/market/SCH7020.csv", mode="r", encoding="cp932") as f:
        reader = csv.reader(f)

        for row in reader:
            if row and row[0] == "神奈川":
                rows.append(row)

    return rows

if __name__ == "__main__":
    load_csv()
