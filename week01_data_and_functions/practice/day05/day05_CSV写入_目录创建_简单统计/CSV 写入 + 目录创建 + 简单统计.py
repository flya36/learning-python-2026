'''
掌握 `csv.DictWriter` 写入、`pathlib` 创建目录、路径拼接，结合最基础的计数统计。
1. 用 `pathlib` 定义输出目录 `output/` 和输出文件 `output/statistics.csv`;
2. 自动创建输出目录（不存在就创建，已存在也不报错）；
3. 遍历文件名，按 `speaker_id` 统计 3 个指标：总样本数、真实样本数、伪造样本数；
4. 用 `csv.DictWriter` 写入 CSV,表头固定为:`speaker_id,total_samples,real_samples,fake_samples`;
5. 写入完成后，**再用 `csv.DictReader` 读取刚生成的 CSV**，打印所有内容验证，形成 “写入 - 读取” 闭环。
'''
import csv
from pathlib import Path
audio_files = [
    "speaker_001_001_real.wav",
    "speaker_001_002_real.wav",
    "speaker_001_003_fake.wav",
    "speaker_002_001_real.wav",
    "speaker_002_002_fake.wav",
    "speaker_003_001_real.wav",
]
fieldnames = ['speaker_id','total_samples','real_samples','fake_samples']
stats = {}
for filename in audio_files:
    # 分割文件名
    filename = Path(filename).stem
    parts = filename.split("_")
    speaker_id = f"{parts[0]}_{parts[1]}"
    label = parts[-1]# real / fake

    # 如果这个speaker还没记录，初始化
    if speaker_id not in stats:
        stats[speaker_id] = {
            "speaker_id": speaker_id,
            "total_samples": 0,
            "real_samples": 0,
            "fake_samples": 0
        }
    # 计数累加
    stats[speaker_id]["total_samples"] += 1
    if label == "real":
        stats[speaker_id]["real_samples"] += 1
    elif label == "fake":
        stats[speaker_id]["fake_samples"] += 1
data = list(stats.values())
current_dir = Path(__file__).parent
output_path = current_dir/'output'/'statistics.csv'
# 创建目录
output_path.parent.mkdir(parents=True,exist_ok=True)
with open(output_path,'w',encoding='utf-8',newline='')as f:
    writer = csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
with open(output_path,'r',encoding='utf-8',newline='')as f:
    reader = csv.DictReader(f)
    for raw in reader:
        print(raw)