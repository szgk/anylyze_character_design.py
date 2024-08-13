import csv
import json
from utils import commindline

def csv_to_json():
    [input_path, output_path] = commindline.get_args()
 
    with open(input_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        # CSVファイルからデータを読み込む
        rows = list(reader)
        
    with open(output_path, 'w', encoding="utf-8") as f:
        json.dump(rows, f)

csv_to_json()