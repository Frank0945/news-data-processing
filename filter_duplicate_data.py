import json
import hashlib
from tqdm import tqdm

def calculate_hash(data):
    hash_object = hashlib.md5(data.encode())
    return hash_object.hexdigest()

def filter_duplicate_data(json_data):
    seen_title_hashes = set()
    seen_content_hashes = set()
    unique_data = []
    filtered_out = 0

    for item in tqdm(json_data, desc="Filtering duplicates", unit="item"):
        title_hash = calculate_hash(item.get("title"))
        content_hash = calculate_hash(item.get("content"))

        if title_hash not in seen_title_hashes and content_hash not in seen_content_hashes:
            seen_title_hashes.add(title_hash)
            seen_content_hashes.add(content_hash)
            unique_data.append(item)
        else:
            print(f"Duplicate data found: {item.get('title')}")
            filtered_out += 1

    print(f"Filtered out {filtered_out} items.")
    print(f"Remaining items: {len(unique_data)}")

    return unique_data

# 讀取 JSON 檔案
with open('json/chinese_data.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# 過濾掉重複資料
unique_data = filter_duplicate_data(json_data)

# 將結果寫回新的 JSON 檔案
with open('json/unique_data.json', 'w', encoding='utf-8') as file:
    json.dump(unique_data, file, ensure_ascii=False, indent=2)
