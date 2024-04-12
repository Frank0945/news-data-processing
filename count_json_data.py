import json

def count_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
        data_count = len(json_data)
    return data_count

# 替換 'your_file.json' 為你的檔案路徑
# file_path = 'final/train_data.json'
# file_path = 'final/test_data.json'
file_path = 'json/pts_cts.json'
data_count = count_json_data(file_path)

print(f"The number of data entries in {file_path} is: {data_count}")
