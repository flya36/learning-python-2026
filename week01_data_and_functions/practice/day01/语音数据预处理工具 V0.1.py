# # 「音频文件元数据解析 → 按说话人维度统计 → 全局数据集汇总」

# # 从音频文件的路径 / 文件名中，结构化提取出实验需要的元数据 
# # 数据集目录/说话人ID/标签_样本编号.wav
# def parse_audio_path(file_path: str, delimiter="_"):
#     if not file_path.lower().endswith('.wav'):
#         return None,None,None
#     parts = file_path.replace('\\','/').split('/')
#     if len(parts) < 3:
#         return None, None, None
#     speaker_id = None
#     label = None
#     file_name = parts[-1]
#     for part in parts:
#         if part.startswith('speaker'):
#             speaker_id = part
#             break
#     name_parts = parts[-1].split(delimiter)
#     if len(name_parts) >= 2 and name_parts[0] in ("real", "fake"):
#         label = name_parts[0]
#     if not speaker_id or not label:
#         return None, None, None
#     return speaker_id,label,file_name

# # 按「说话人 ID」维度，对音频样本进行分组统计
# '''
# 遍历所有音频文件，调用 `parse_audio_path` 解析每个文件的元数据，然后按说话人 ID 聚合
# 统计每个说话人的样本总量、真实样本数、伪造样本数、真假样本比例。
# '''
# def count_samples_by_speaker(audio_files):
#     group_statistics = {}
#     file_info = []
#     for file_path in audio_files:
#         file_info.append(parse_audio_path(file_path))
#     for info in file_info:
#         if info[0] in group_statistics:
#             group_statistics[info[0]]['total'] += 1
#             if info[1] == 'real':
#                 group_statistics[info[0]]['real'] += 1
#             elif info[1] == 'fake':
#                 group_statistics[info[0]]['fake'] += 1
#         else:
#             group_statistics[info[0]]['total'] = 1
#             if info[1] == 'real':
#                 group_statistics[info[0]]['real'] = 1
#                 group_statistics[info[0]]['fake'] = 0
#             elif info[1] == 'fake':
#                 group_statistics[info[0]]['fake'] = 1
#                 group_statistics[info[0]]['real'] = 0
#     for group in group_statistics:
#         group_statistics[group]['real_ratio'] = group_statistics[group]['real']/group_statistics[group]['total']
#     return group_statistics

# # 生成整个数据集的全局统计摘要
# '''
# - 输入：音频文件路径列表
# - 输出：全局统计字典，典型字段包括：
#  - 总样本数、总说话人数
#  - 真实样本总数、伪造样本总数、整体真假比例
#  - 单说话人最大 / 最小样本数、样本分布均匀度
#  - （扩展）总音频时长、平均时长
# - 同时支持将结果导出为 JSON/CSV 文件。
# '''
# def summary_statistics(audio_files):
#     global_statistics = {}
#     file_info = []
#     for file_path in audio_files:
#         file_info.append(parse_audio_path(file_path))
#     global_statistics['total_sample'] = len(file_info)
#     group_statistics = count_samples_by_speaker(audio_files)
#     global_statistics['total_speaker'] = len(group_statistics)
#     global_statistics['total_real_sample'] = 0
#     global_statistics['total_fake_sample'] = 0
#     for group in group_statistics:
#         global_statistics['total_real_sample'] += group['real']
#         global_statistics['total_fake_sample'] += group['fake']
#     global_statistics['real_radio'] = global_statistics['total_real_sample']/global_statistics['total_sample']
#     global_statistics['max_speaker_sample'] = max(group_statistics,key=lambda x :x['total'])
#     global_statistics['min_speaker_sample'] = min(group_statistics,key=lambda x :x['total'])
#     return group_statistics
# file_name = ['data/speaker_01/real_001.wav','data/speaker_02/fake_005.wav']
# print(summary_statistics(file_name))


import json
import math


def parse_audio_path(file_path: str, delimiter: str = "_") -> tuple:
    """
    从音频文件路径中提取元数据
    :param file_path: 音频文件完整路径，格式：数据集/说话人ID/标签_样本编号.wav
    :param delimiter: 文件名分隔符，默认下划线
    :return: (说话人ID, 标签, 文件名)；格式无效返回 (None, None, None)
    """
    # 1. 空输入校验
    if not isinstance(file_path, str) or not file_path.strip():
        return None, None, None

    # 2. 后缀校验（不区分大小写）
    if not file_path.lower().endswith(".wav"):
        return None, None, None

    # 3. 【修正】统一路径分隔符：把Windows反斜杠全部替换为正斜杠
    normalized_path = file_path.replace("\\", "/")
    parts = normalized_path.split("/")

    # 4. 路径层级校验（至少3层：数据集/说话人/文件名）
    if len(parts) < 3:
        return None, None, None

    file_name = parts[-1]
    speaker_id = None
    label = None

    # 5. 【修正】匹配speaker前缀，和数据集命名一致
    for part in parts:
        if part.startswith("speaker"):
            speaker_id = part
            break

    # 6. 解析文件名中的标签
    name_parts = file_name.split(delimiter)
    if len(name_parts) >= 2 and name_parts[0] in ("real", "fake"):
        label = name_parts[0]

    # 7. 【修正】任一信息缺失，统一返回全None，避免脏数据
    if not speaker_id or not label:
        return None, None, None

    return speaker_id, label, file_name


def count_samples_by_speaker(audio_files: list[str]) -> dict:
    """
    按说话人维度分组统计样本数量和真假比例
    :param audio_files: 音频文件路径列表
    :return: 字典，key=说话人ID，value=统计信息
    """
    group_stats = {}

    for file_path in audio_files:
        speaker_id, label, _ = parse_audio_path(file_path)

        # 【修正】无效文件直接跳过，不纳入统计
        if not speaker_id or not label:
            continue

        # 说话人不存在则初始化
        if speaker_id not in group_stats:
            group_stats[speaker_id] = {
                "total": 0,
                "real": 0,
                "fake": 0,
                "real_ratio": 0.0
            }

        # 更新计数
        group_stats[speaker_id]["total"] += 1
        if label == "real":
            group_stats[speaker_id]["real"] += 1
        else:
            group_stats[speaker_id]["fake"] += 1

    # 计算每个说话人的真实样本比例
    for stats in group_stats.values():
        if stats["total"] > 0:
            stats["real_ratio"] = round(stats["real"] / stats["total"], 4)

    return group_stats


def summary_statistics(audio_files: list[str]) -> dict:
    """
    生成数据集全局统计摘要
    :param audio_files: 音频文件路径列表
    :return: 全局统计字典
    """
    # 直接复用分组统计结果，【修正】不再重复解析文件
    group_stats = count_samples_by_speaker(audio_files)
    total_speaker = len(group_stats)

    # 空数据集处理，避免除零
    if total_speaker == 0:
        return {
            "total_sample": 0,
            "valid_sample": 0,
            "total_speaker": 0,
            "total_real_sample": 0,
            "total_fake_sample": 0,
            "real_ratio": 0.0,
            "note": "无有效音频文件"
        }

    total_real = 0
    total_fake = 0
    sample_counts = []  # 存储每个说话人的样本数，用于计算均匀度

    # 【修正】正确遍历字典的键和值
    for speaker, stats in group_stats.items():
        total_real += stats["real"]
        total_fake += stats["fake"]
        sample_counts.append(stats["total"])

    total_valid = total_real + total_fake
    real_ratio = round(total_real / total_valid, 4) if total_valid > 0 else 0.0

    # 【修正】正确计算最大/最小样本数，同时返回说话人ID
    max_count = max(sample_counts)
    min_count = min(sample_counts)
    max_speaker = max(group_stats.items(), key=lambda x: x[1]["total"])[0]
    min_speaker = min(group_stats.items(), key=lambda x: x[1]["total"])[0]

    # 计算样本分布均匀度（变异系数CV）
    mean_count = total_valid / total_speaker
    variance = sum((x - mean_count) ** 2 for x in sample_counts) / total_speaker
    std = math.sqrt(variance)
    cv = round(std / mean_count, 4) if mean_count > 0 else 0.0

    return {
        "total_file": len(audio_files),  # 输入的总文件数
        "valid_sample": total_valid,     # 有效样本数
        "total_speaker": total_speaker,
        "total_real_sample": total_real,
        "total_fake_sample": total_fake,
        "real_ratio": real_ratio,  # 【修正】修正拼写错误
        "max_speaker_sample": {
            "speaker": max_speaker,
            "count": max_count
        },
        "min_speaker_sample": {
            "speaker": min_speaker,
            "count": min_count
        },
        "distribution_cv": cv,
        "distribution_evenness": round(max(0, 1 - cv), 4)
    }


def export_to_json(data: dict, output_path: str) -> None:
    """导出统计结果为JSON文件"""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# ========== 测试代码 ==========
if __name__ == "__main__":
    test_files = [
        "data/speaker_01/real_001.wav",
        "data/speaker_01/real_002.wav",
        "data/speaker_01/fake_001.wav",
        "data/speaker_02/fake_001.wav",
        "data/speaker_02/fake_002.wav",
        "data/speaker_03/real_001.wav",
        "data/unknown/test.wav",          # 异常：无speaker目录
        "data/speaker_04/error_001.wav",  # 异常：标签不是real/fake
        "data/speaker_05/test.mp3",       # 异常：后缀错误
        "data\\speaker_06\\real_001.wav"  # Windows反斜杠路径
    ]

    print("=== 按说话人分组统计 ===")
    group_result = count_samples_by_speaker(test_files)
    for k, v in group_result.items():
        print(f"{k}: {v}")

    print("\n=== 全局统计摘要 ===")
    global_result = summary_statistics(test_files)
    for k, v in global_result.items():
        print(f"{k}: {v}")

    # 导出JSON
    export_to_json(global_result, "analysis.json")
    print("\n统计结果已导出到 analysis.json")
