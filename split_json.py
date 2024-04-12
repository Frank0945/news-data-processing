import json
from sklearn.model_selection import train_test_split

def split_json(input_file, train_file, test_file, test_size=0.2, random_state=None):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 使用 train_test_split 函數進行資料集劃分
    train_data, test_data = train_test_split(data, test_size=test_size, random_state=random_state)

    # 將劃分後的資料寫入新的 JSON 檔案
    with open(train_file, 'w', encoding='utf-8') as train_out:
        json.dump(train_data, train_out, ensure_ascii=False, indent=2)

    with open(test_file, 'w', encoding='utf-8') as test_out:
        json.dump(test_data, test_out, ensure_ascii=False, indent=2)

# 使用範例
split_json('json/pts_cts.json', 'final/train_data.json', 'final/test_data.json', test_size=0.15, random_state=42)
