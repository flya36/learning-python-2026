'''实现完整流程:输入音频目录→遍历目录下所有音频文件→统计
(说话人数量、真假样本数、总时长)
→导出JSON/CSV格式的统计结果;'''
import json
import csv
import wave
import logging
from pathlib import Path

# ========== 当日学习点2：错误日志系统 ==========
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
    handlers=[
        logging.FileHandler('audio_tool_error.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def get_wav_duration(wav_path: Path) -> float:
    # 读取wav文件时长（秒），损坏文件返回0并记录日志
    try:
        with wave.open(str(wav_path), "rb") as wf:
            frames = wf.getnframes()
            rate = wf.getframerate()
            return round(frames / rate, 2)
    except FileNotFoundError as e:
        logger.error(f"文件不存在: {wav_path.name} - {str(e)} - 已跳过该文件")
        return 0.0
    except wave.Error as e:
        logger.error(f"音频文件损坏/格式不支持: {wav_path.name} - {str(e)} - 已跳过该文件")
        return 0.0
    except Exception as e:
        logger.error(f"读取文件未知错误: {wav_path.name} - {str(e)} - 已跳过该文件")
        return 0.0


def audio_statistics(audio_dir: str, output_dir: str = "./output") -> dict:
    """
    音频文件批量统计工具 V0.3
    :param audio_dir: 音频文件目录路径
    :param output_dir: 结果输出目录
    :return: 统计结果字典
    """
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

    try:
        output_path.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        logger.critical(f"输出目录创建失败: {output_dir} - {str(e)} - 程序终止")
        return result

    # ========== 场景1：目标目录无效/为空 ==========
    if not audio_path.exists():
        logger.error(f"目标目录不存在: {audio_dir} - 终止统计，返回空结果")
        _export_result(result, output_path)
        return result

    if not audio_path.is_dir():
        logger.error(f"目标路径不是有效目录: {audio_dir} - 终止统计，返回空结果")
        _export_result(result, output_path)
        return result

    try:
        wav_files = list(audio_path.glob("*.wav"))
    except PermissionError as e:
        logger.error(f"目录无读取权限: {audio_dir} - {str(e)} - 终止统计")
        _export_result(result, output_path)
        return result

    if not wav_files:
        logger.warning(f"目录内未找到 .wav 文件: {audio_dir} - 已输出空统计结果")
        _export_result(result, output_path)
        return result

    # 3. 解析与统计
    speaker_set = set()
    skip_count = 0

    for file in wav_files:
        filename = file.stem
        parts = filename.split("_")

        # ========== 场景2：文件名格式错误 ==========
        if len(parts) < 3:
            logger.warning(f"文件名格式错误，跳过: {file.name} - 命名需符合 说话人ID_xxx_label 格式")
            skip_count += 1
            continue

        speaker_id = parts[0]
        label = parts[-1]
        duration = get_wav_duration(file)

        # 时长为0说明文件读取失败，已在函数内记录日志
        if duration <= 0:
            skip_count += 1
            continue

        # 基础计数
        result["total_files"] = int(result["total_files"]) + 1
        result["total_duration_sec"] = float(result["total_duration_sec"]) + duration
        speaker_set.add(speaker_id)

        # 标签统计
        if label == "real":
            result["real_count"] = int(result["real_count"]) + 1
        elif label == "fake":
            result["fake_count"] = int(result["fake_count"]) + 1
        else:
            logger.warning(f"未知标签类型，跳过统计: {file.name} - 标签值: {label}")
            skip_count += 1
            continue

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
    logger.info(f"统计完成：有效文件{result['total_files']}个，跳过{skip_count}个，结果已输出到 {output_path.resolve()}")
    return result


def _export_result(result: dict, output_dir: Path):
    """导出 JSON 和 CSV 两种格式"""
    json_path = output_dir / "audio_stats.json"
    csv_path = output_dir / "audio_stats.csv"
    speaker_detail_raw = result.get("speaker_detail", {})
    speaker_detail = speaker_detail_raw if isinstance(speaker_detail_raw, dict) else {}

    try:
        # 导出 JSON
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2, sort_keys=True)

        # 导出 CSV（说话人明细）
        with open(csv_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["说话人ID", "样本数", "真实样本", "伪造样本", "总时长(秒)", "总时长(分钟)"])
            for speaker_id, detail in speaker_detail.items():
                writer.writerow([
                    speaker_id,
                    detail["count"],
                    detail["real_count"],
                    detail["fake_count"],
                    detail["duration_sec"],
                    detail["duration_min"]
                ])
            writer.writerow([])
            writer.writerow(["汇总", result["total_files"], result["real_count"],
                             result["fake_count"], result["total_duration_sec"],
                             result["total_duration_min"]])
        logger.debug("结果文件导出成功")
    except IOError as e:
        logger.error(f"结果导出失败: {str(e)}")


if __name__ == "__main__":
    stats = audio_statistics("./example", "./output")
    print("\n统计结果预览:")
    print(f"总文件数: {stats['total_files']}")
    print(f"说话人数量: {stats['speaker_count']}")
    print(f"真实样本: {stats['real_count']} | 伪造样本: {stats['fake_count']}")
    print(f"总时长: {stats['total_duration_min']} 分钟")
