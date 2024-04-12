import json

def merge_json_arrays(json1_path, json2_path, output_path):
    with open(json1_path, 'r', encoding='utf-8') as json1_file:
        json1_data = json.load(json1_file)

    with open(json2_path, 'r', encoding='utf-8') as json2_file:
        json2_data = json.load(json2_file)

    merged_data = json1_data + json2_data

    with open(output_path, 'w', encoding='utf-8') as output_file:
        json.dump(merged_data, output_file, indent=4)

# 路徑設置為你自己的文件路徑
json1_path = 'pts_json/filtered_data.json'
json2_path = 'json/filtered_data.json'
output_path = 'json/pts_cts.json'

merge_json_arrays(json1_path, json2_path, output_path)
