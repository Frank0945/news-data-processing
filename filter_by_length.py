import json

def filter_by_length(data, title_min, title_max, content_min, content_max, total_length_max):
    filtered_data = []

    for item in data:
        title_length = len(item.get("title", ""))
        content_length = len(item.get("content", ""))
        total_length = title_length + content_length

        # 判斷是否符合條件，新增總長度限制
        if title_min <= title_length <= title_max and \
           content_min <= content_length <= content_max and \
           total_length_min <= total_length <= total_length_max:
            filtered_data.append(item)

    return filtered_data

# 讀取 JSON 檔案
with open('json/unescape_data.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# 設定條件值，包括 total_length_max
title_min = 14
title_max = 32  
content_min = 200
content_max = 2000
total_length_max = 768
total_length_min = 220

# 刪除不符合條件的資料
filtered_data = filter_by_length(json_data, title_min, title_max, content_min, content_max, total_length_max)

# 將結果寫回新的 JSON 檔案
with open('json/filtered_data.json', 'w', encoding='utf-8') as file:
    json.dump(filtered_data, file, ensure_ascii=False, indent=2)
