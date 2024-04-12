import json

def clean_content(data):
    cleaned_data = []
    
    for item in data:

        if "VideoPlayerisloading" in item.get("content"):
            continue

        # 移除 content 中的空白、'=' 和 '\n'
        cleaned_content = item.get("content", "").replace(" ", "").replace("=", "").replace("\n", "").replace(" ", "").replace("　", "").replace("\t", "")

        prefixes = [
            {"text": "電）", "check": 0, "use": 1},
            {"text": "導）", "check": 0, "use": 1},
            {"text": "導/", "check": 0, "use": 1},
            {"text": "譯/", "check": 0, "use": 1},
            {"text": "（編輯", "check": 1, "use": 0},
            {"text": "新聞來源", "check": 1, "use": 0},
            {"text": "（譯", "check": 1, "use": 0},
        ]

        for prefix_info in prefixes:
            prefix = prefix_info["text"]
            check_index = prefix_info["check"]
            use_index = prefix_info["use"]
    
            removePrefix = cleaned_content.split(prefix, 1)
            if check_index == 1:
                removePrefix = cleaned_content.rsplit(prefix, 1)

            if len(removePrefix) == 2:
                if len(removePrefix[check_index]) < 40:
                    cleaned_content = removePrefix[use_index]

        item["content"] = cleaned_content
        cleaned_title = item.get("title", "").replace("(影音)", "").replace("　", " ").replace("【台語新聞】", "")
        item["title"] = cleaned_title
        
        cleaned_data.append(item)

    return cleaned_data

# 讀取 JSON 檔案
with open('json/unique_data.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# 移除 content 中的空白、'= ' 和 '\n'
cleaned_data = clean_content(json_data)

# 將結果寫回新的 JSON 檔案
with open('json/cleaned_data.json', 'w', encoding='utf-8') as file:
    json.dump(cleaned_data, file, ensure_ascii=False, indent=2)
