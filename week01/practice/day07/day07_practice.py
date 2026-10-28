'''
给定一个文本文件 `audio_list.txt`，每行存储一个音频文件名，格式约定为 `说话人ID_样本编号_标签.wav`（标签仅允许 `real` / `fake`）。
请编写函数 `validate_and_statistics(file_path, output_path)`，完成以下功能：
1. 读取文件，逐行读取文件名，去除首尾空格和空行；
2. 校验每个文件名：格式不符合、标签不合法、文件扩展名为非 `.wav` 的，标记为异常并跳过；
3. 统计：总文件数、有效文件数、异常文件数、说话人总数、真实样本数、伪造样本数、每个说话人的样本分布；
4. 将统计结果导出为 JSON 文件，保存到 `output_path`;
5. 异常处理：文件不存在时，打印提示并输出空结果文件。
'''
from pathlib import Path
import json
def validate_and_statistics(file_path, output_path):
    res = {'total_file':0,
           'valid_file':0,
           'wrong_file':0,
           'speaker_count':0,
           'total_real':0,
           'total_fake':0,
           'detail':{}
           }
    # 异常处理：文件不存在时，打印提示并输出空结果文件
    file_path = Path(file_path)
    output_path = Path(output_path)
    if not file_path.exists() or not file_path.is_file():
        print('文件不存在')
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(res, f, ensure_ascii=False, indent=2)
        return res
    # 读取文件，逐行读取文件名，去除首尾空格和空行
    with open(file_path,'r',encoding='utf-8') as f:
        file_name = f.readlines()
        for name in file_name:
            name = name.strip()
            if not name:
                continue
            res['total_file'] += 1
            parts = Path(name).stem.split('_')
            speaker_id = parts[0]
            label = parts[-1]
            # 校验每个文件名：格式不符合、标签不合法、文件扩展名为非 `.wav` 的，标记为异常并跳过
            if len(parts) < 3 or not name.endswith(".wav") or label not in ('real','fake'):
                print(f'{name}异常')
                res['wrong_file'] +=1
                continue
            # 统计：有效文件数、说话人总数、真实样本数、伪造样本数、每个说话人的样本分布
            res['valid_file'] += 1
            if speaker_id not in res['detail']:
                res["detail"][speaker_id] = {
                "real_count": 0,
                "fake_count": 0,
                "total": 0
            }
            res['detail'][speaker_id]["total"] += 1
            if label == 'fake':
                res['total_fake'] += 1
                res['detail'][speaker_id]['fake_count'] += 1
            elif label == 'real':
                res['total_real'] += 1
                res['detail'][speaker_id]['real_count'] += 1
    res["speaker_count"] = len(res["detail"])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=2, sort_keys=True)

    return res
if __name__ == "__main__":
    res = validate_and_statistics("audio_list.txt", "audio_stats.json")