import json

def analyze_text_lengths(data):
    title_lengths = []
    content_lengths = []
    combined_lengths = []
    titles = []
    contents = []

    for item in data:
        # 分析 title 字數
        title = item.get("title", "")
        title_length = len(title)
        title_lengths.append(title_length)
        titles.append(title)

        # 分析 content 字數
        content = item.get("content", "")
        content_length = len(content)
        content_lengths.append(content_length)
        contents.append(content)

        # 計算 title 和 content 的總長度
        combined_length = title_length + content_length
        combined_lengths.append(combined_length)

    # 計算平均數
    avg_title_length = sum(title_lengths) / len(title_lengths)
    avg_content_length = sum(content_lengths) / len(content_lengths)
    avg_combined_length = sum(combined_lengths) / len(combined_lengths)

    # 計算中位數
    sorted_title_lengths = sorted(title_lengths)
    sorted_content_lengths = sorted(content_lengths)
    sorted_combined_lengths = sorted(combined_lengths)
    
    mid_index_title = len(sorted_title_lengths) // 2
    mid_index_content = len(sorted_content_lengths) // 2
    mid_index_combined = len(sorted_combined_lengths) // 2
    
    median_title_length = sorted_title_lengths[mid_index_title] if len(sorted_title_lengths) % 2 != 0 else \
                         (sorted_title_lengths[mid_index_title - 1] + sorted_title_lengths[mid_index_title]) / 2

    median_content_length = sorted_content_lengths[mid_index_content] if len(sorted_content_lengths) % 2 != 0 else \
                           (sorted_content_lengths[mid_index_content - 1] + sorted_content_lengths[mid_index_content]) / 2

    median_combined_length = sorted_combined_lengths[mid_index_combined] if len(sorted_combined_lengths) % 2 != 0 else \
                            (sorted_combined_lengths[mid_index_combined - 1] + sorted_combined_lengths[mid_index_combined]) / 2

    # 統計最小值和最大值
    min_title_length = min(title_lengths)
    max_title_length = max(title_lengths)
    min_content_length = min(content_lengths)
    max_content_length = max(content_lengths)
    min_combined_length = min(combined_lengths)
    max_combined_length = max(combined_lengths)

    # 統計前 10 大和前 10 小（不重複）
    top_10_min_title = sorted(set(title_lengths))[:10]
    top_10_max_title = sorted(set(title_lengths), reverse=True)[:10]
    top_10_min_content = sorted(set(content_lengths))[:10]
    top_10_max_content = sorted(set(content_lengths), reverse=True)[:10]
    top_10_min_combined = sorted(set(combined_lengths))[:10]
    top_10_max_combined = sorted(set(combined_lengths), reverse=True)[:10]

    # 找到最大和最小的 title、content 和 combined
    min_title_index = title_lengths.index(min_title_length)
    max_title_index = title_lengths.index(max_title_length)
    min_content_index = content_lengths.index(min_content_length)
    max_content_index = content_lengths.index(max_content_length)
    min_combined_index = combined_lengths.index(min_combined_length)
    max_combined_index = combined_lengths.index(max_combined_length)

    return (
        avg_title_length, median_title_length, min_title_length, max_title_length, top_10_min_title, top_10_max_title,
        avg_content_length, median_content_length, min_content_length, max_content_length, top_10_min_content, top_10_max_content,
        avg_combined_length, median_combined_length, min_combined_length, max_combined_length, top_10_min_combined, top_10_max_combined,
        titles[min_title_index], titles[max_title_index], contents[min_content_index], contents[max_content_index],
        titles[min_combined_index], contents[min_combined_index]
    )

# 讀取 JSON 檔案
with open('json/pts_cts.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# 分析 title 和 content 字數
(
    avg_title, median_title, min_title, max_title, top_10_min_title, top_10_max_title,
    avg_content, median_content, min_content, max_content, top_10_min_content, top_10_max_content,
    avg_combined, median_combined, min_combined, max_combined, top_10_min_combined, top_10_max_combined,
    min_title_text, max_title_text, min_content_text, max_content_text,
    min_combined_title_text, min_combined_content_text
) = analyze_text_lengths(json_data)

print(f"Average Title Length: {avg_title}")
print(f"Median Title Length: {median_title}")
print(f"Min Title Length: {min_title}")
print(f"Max Title Length: {max_title}")
print(f"Top 10 Min Title Length: {top_10_min_title}")
print(f"Top 10 Max Title Length: {top_10_max_title}")
print(f"Min Title Text: {min_title_text}")
print(f"Max Title Text: {max_title_text}")
print()
print(f"Average Content Length: {avg_content}")
print(f"Median Content Length: {median_content}")
print(f"Min Content Length: {min_content}")
print(f"Max Content Length: {max_content}")
print(f"Top 10 Min Content Length: {top_10_min_content}")
print(f"Top 10 Max Content Length: {top_10_max_content}")
print(f"Min Content Text: {min_content_text}")
print(f"Max Content Text: {max_content_text}")
print()
print(f"Average Combined Length: {avg_combined}")
print(f"Median Combined Length: {median_combined}")
print(f"Min Combined Length: {min_combined}")
print(f"Max Combined Length: {max_combined}")
print(f"Top 10 Min Combined Length: {top_10_min_combined}")
print(f"Top 10 Max Combined Length: {top_10_max_combined}")
print(f"Min Combined Title Text: {min_combined_title_text}")
print(f"Min Combined Content Text: {min_combined_content_text}")
