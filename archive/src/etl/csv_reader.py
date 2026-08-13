from pathlib import Path
import pandas as pd

current_file = Path(__file__).resolve()
base_dir = current_file.parent[1]

csv_file = base_dir / 'data' / 'sample' / 'harvest_sample.csv'

def reader_csv():
    df = pd.read_csv(csv_file, encoding='utf-8')
    
    for index, row in df.iterrows():
        row_dict = row.to_dict()
        print(row_dict)
    
