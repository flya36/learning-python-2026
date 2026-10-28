'''
给定一个音频文件目录路径，目录下包含多个 `.wav` 文件，文件名格式统一为 `说话人ID_样本编号_标签.wav`（例如 `speaker01_003_real.wav`、`speaker02_007_fake.wav`）。
请编写一个函数 `audio_statistics(audio_dir, output_path)`，完成以下功能：
1. 遍历目录下所有 `.wav` 文件，从文件名中提取 说话人 ID 和 标签(real/fake);
2. 统计：总文件数、说话人总数、真实样本数、伪造样本数、每个说话人的样本数量；
3. 将统计结果导出为 JSON 文件，保存到 `output_path`;
4. 增加异常处理：目录不存在、目录内无 wav 文件时，返回友好提示并生成空结果文件。
'''
# speaker01_003_real.wav
from pathlib import Path
import json
def audio_statistics(audio_dir, output_path):
    result = {
        "total_files": 0,
        "speaker_count": 0,
        "real_count": 0,
        "fake_count": 0,
        "speaker_detail": {}
    }
    audio_path = Path(audio_dir)
    current_dir = Path(__file__).parent
    output_path = Path(output_path)
    # 1. 目录存在性校验
    if not audio_path.exists() or not audio_path.is_dir():
        print(f"错误：目录 {audio_dir} 不存在或不是有效目录")
        # 生成空结果文件
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        return result
    # 2. 遍历当前目录下所有 wav 文件
    wav_files = list(audio_path.glob("*.wav"))
    if not wav_files:
        print("提示：目录内没有找到 .wav 文件")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        return result
    
    # 3. 解析文件名并统计
    speaker_set = set()
    for file in wav_files:
        filename = file.stem
        parts = filename.split("_")
        # 文件名格式容错
        if len(parts) < 3:
            print(f"跳过格式错误的文件：{file.name}")
            continue
        speaker_id = parts[0]
        label = parts[-1]
        result["total_files"] += 1
        speaker_set.add(speaker_id)
        # 标签统计
        if label == "real":
            result["real_count"] += 1
        elif label == "fake":
            result["fake_count"] += 1
        # 说话人明细统计
        if speaker_id in result["speaker_detail"]:
            result["speaker_detail"][speaker_id] += 1
        else:
            result["speaker_detail"][speaker_id] = 1
    result["speaker_count"] = len(speaker_set)
    with open(output_path,'w',encoding='utf-8')as f:
        json.dump(result,f,ensure_ascii=False,indent=2,sort_keys=True)
    return result
