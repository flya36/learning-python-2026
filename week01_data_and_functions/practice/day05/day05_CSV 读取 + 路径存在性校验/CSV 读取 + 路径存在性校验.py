'''
1. 用 `Path(__file__).parent` 定位代码所在目录，拼接出 CSV 文件路径和音频文件夹路径；
2. 用 `csv.DictReader` 读取 `audio_list.csv`:
3. 遍历每一行，拼接出音频文件的完整路径（`data/audio/文件名`):
4. 检查文件是否存在，**只筛选出 label 为 real 且文件真实存在的记录**:
5. 按格式打印结果：`说话人:speaker_001,文件:speaker_001_001.wav,时长:3.2秒`。
'''
import csv
from pathlib import Path
current_dir = Path(__file__).parent
audio_file = current_dir/'data'/'audio_list.csv'
with open(audio_file,'r',encoding='utf-8',newline='')as f:
    reader = csv.DictReader(f)
    for row in reader:
        file_route = current_dir / "data" / "audio" / row["file_name"]
        if row['label'] == 'real' and file_route.is_file():
            print(f'说话人:{row['speaker_id']},文件:{row['file_name']},时长:{row['duration']}')