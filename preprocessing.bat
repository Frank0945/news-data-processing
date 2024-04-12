@echo off
echo onlycn
python onlycn.py
echo filter_duplicate_data
python filter_duplicate_data.py
echo clean_content
python clean_content.py
echo unescape
python unescape.py
echo filter_by_length
python filter_by_length.py
echo count_json_data
python count_json_data.py
pause