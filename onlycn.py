import json
import langid
from collections import Counter

def detect_language(text):
    fragments = text.split()
    languages = [langid.classify(fragment)[0] for fragment in fragments]
    element_counts = Counter(languages)
    if element_counts:
        most_common_element, _ = element_counts.most_common(1)[0]
        return most_common_element
    else:
        return ""

def filter_and_save_chinese(json_data, output_file):
    chinese_data = []
    total_items = len(json_data)

    for idx, item in enumerate(json_data, 1):
        text = item.get("content")
        language = detect_language(text)
        
        if language == 'zh':
            chinese_data.append(item)

        progress_percentage = (idx / total_items) * 100
        print(f"\rProcessing: {idx}/{total_items} ({progress_percentage:.2f}%) CN: {len(chinese_data)}/{total_items}", end='', flush=True)

    # 將中文資料寫入新的 JSON 文件
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(chinese_data, file, ensure_ascii=False, indent=2)

    return len(chinese_data)

# 讀取 JSON 文件
file_path = 'json/merged.json'  # 請替換為實際的文件路徑
output_file_path = 'json/chinese_data.json'  # 請替換為實際的輸出文件路徑

with open(file_path, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# 篩選並保存中文的資料
filtered_count = filter_and_save_chinese(json_data, output_file_path)

# 打印結果
print(f"篩選出的筆數: {filtered_count}")
