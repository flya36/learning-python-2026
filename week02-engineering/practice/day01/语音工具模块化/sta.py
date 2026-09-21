from pathlib import Path
from exporter import _export_result
from parse import get_wav_duration

def audio_statistics(audio_dir: str, output_dir: str = "./output") -> dict:
    """
    音频文件批量统计工具 V0.2
    :param audio_dir: 音频文件目录路径
    :param output_dir: 结果输出目录
    :return: 统计结果字典
    """
    # 初始化标准结果
    result: dict[str, object] = {
        "total_files": 0,
        "speaker_count": 0,
        "real_count": 0,
        "fake_count": 0,
        "total_duration_sec": 0.0,
        "total_duration_min": 0.0,
        "speaker_detail": {}
    }
    speaker_detail: dict[str, dict[str, float | int]] = {}
    result["speaker_detail"] = speaker_detail

    audio_path = Path(audio_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # 1. 目录校验
    if not audio_path.exists() or not audio_path.is_dir():
        print(f"[错误] 目录不存在或不是有效目录: {audio_dir}")
        _export_result(result, output_path)
        return result

    # 2. 遍历所有 wav 文件
    wav_files = list(audio_path.glob("*.wav"))
    if not wav_files:
        print("[提示] 目录内未找到 .wav 文件")
        _export_result(result, output_path)
        return result

    # 3. 解析与统计
    speaker_set = set()
    for file in wav_files:
        filename = file.stem
        parts = filename.split("_")

        # 文件名格式容错
        if len(parts) < 3:
            print(f"[跳过] 文件名格式错误: {file.name}")
            continue

        speaker_id = parts[0]
        label = parts[-1]
        duration = get_wav_duration(file)

        # 基础计数
        result["total_files"] = int(result["total_files"]) + 1
        result["total_duration_sec"] = float(result["total_duration_sec"]) + duration
        speaker_set.add(speaker_id)

        # 标签统计
        if label == "real":
            result["real_count"] = int(result["real_count"]) + 1
        elif label == "fake":
            result["fake_count"] = int(result["fake_count"]) + 1

        # 说话人明细
        if speaker_id not in speaker_detail:
            speaker_detail[speaker_id] = {
                "count": 0,
                "real_count": 0,
                "fake_count": 0,
                "duration_sec": 0.0
            }

        detail = speaker_detail[speaker_id]
        detail["count"] = int(detail["count"]) + 1
        detail["duration_sec"] = float(detail["duration_sec"]) + duration
        if label == "real":
            detail["real_count"] = int(detail["real_count"]) + 1
        elif label == "fake":
            detail["fake_count"] = int(detail["fake_count"]) + 1

    # 汇总计算
    result["speaker_count"] = len(speaker_set)
    result["total_duration_min"] = round(float(result["total_duration_sec"]) / 60, 2)
    for spk in speaker_detail.values():
        spk["duration_min"] = round(float(spk["duration_sec"]) / 60, 2)

    # 4. 导出结果
    _export_result(result, output_path)
    print(f"[完成] 统计完成，结果已输出到 {output_path.resolve()}")
    return result