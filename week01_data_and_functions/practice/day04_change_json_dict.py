'''
给定一段语音样本统计的 JSON 字符串，完成以下操作：
1. 使用 `json.loads` 将 JSON 字符串解析为 Python 字典；
2. 从字典中读取并打印：总样本数、真实语音数量、伪造语音数量、说话人列表；
3. 向字典中新增一个字段 `"analysis_date"`，值为当前日期字符串（如 `"2026-09-03"`）；
4. 使用 `json.dumps` 将更新后的字典转回格式化 JSON 字符串（缩进 2 空格）并打印。
'''
import json
json_str = '''
{
    "total_samples": 128,
    "real_samples": 64,
    "fake_samples": 64,
    "speakers": ["speaker_001", "speaker_002", "speaker_003"],
    "sample_format": "wav",
    "has_label": true
}
'''
dict_str = json.loads(json_str)
print(f'总样本数:{dict_str["total_samples"]},真实语音数量:{dict_str["real_samples"]},伪造语音数量:{dict_str["fake_samples"]},说话人列表:{dict_str["speakers"]}')
dict_str["analysis_date"] = "2026-09-03"
json_str = json.dumps(dict_str,indent=2)
print(json_str)