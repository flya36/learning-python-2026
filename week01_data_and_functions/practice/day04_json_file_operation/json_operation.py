'''
模拟语音预处理工具的统计结果导出，完成以下操作：
1. 手动构造一个 Python 字典，包含以下统计信息：
   - 说话人数量、总样本数、真实样本数、伪造样本数
   - 每个说话人的样本数量（字典形式）
   - 平均音频时长（秒）
2. 使用 `json.dump` 将该字典写入当前目录下的 `analysis.json` 文件，要求缩进 2 空格、中文正常显示；
3. 使用 `json.load` 读取刚生成的 `analysis.json` 文件，验证内容与写入一致；
4. 打印读取结果中的 “总样本数” 和 “伪造样本占比”。
'''
import json

stats = {
    "speaker_count": 3,
    "total_samples": 128,
    "real_samples": 64,
    "fake_samples": 64,
    "speaker_samples": {
        "speaker_001": 42,
        "speaker_002": 43,
        "speaker_003": 43
    },
    "avg_duration_seconds": 3.2,
    "export_time": "2026-09-03"
}
with open(r'week01_data_and_functions\practice\day04_json_file_operation\analysis.json','w',encoding='utf-8') as f:
    json.dump(stats,f,indent=2,ensure_ascii=False)
with open(r'week01_data_and_functions\practice\day04_json_file_operation\analysis.json','r',encoding='utf-8') as f:
    res = json.load(f)
    print(res)
    print(res["total_samples"])
    # 计算并打印伪造样本占比
    fake_ratio = res["fake_samples"] / res["total_samples"]
    print(f"伪造样本占比: {fake_ratio:.2%}")
    print(type(res))