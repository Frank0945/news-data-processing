import json
import html

# 讀取 JSON 檔案
with open('json/cleaned_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 將 HTML 編碼轉換回正常字串
for item in data:
    item['title'] = html.unescape(item['title'])
    item['content'] = html.unescape(item['content'])

# 寫入處理後的資料到新的 JSON 檔案
output_filename = 'json/unescape_data.json'
with open(output_filename, 'w', encoding='utf-8') as output_file:
    json.dump(data, output_file, ensure_ascii=False, indent=2)

print(f"處理後的資料已經儲存到 {output_filename} 檔案中。")
