import json
import csv
import logging
from models import AudioDataset

logger = logging.getLogger(__name__)


def export_to_csv(dataset: AudioDataset, output_path: str) -> bool:
    """导出样本明细为CSV"""
    try:
        samples = dataset.get_all_samples()
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["文件路径", "说话人ID", "标签", "时长(秒)"])
            for s in samples:
                writer.writerow([s.file_path, s.speaker_id, "真实" if s.label else "克隆", s.duration])
        logger.info(f"CSV导出成功：{output_path}")
        return True
    except Exception as e:
        logger.error(f"CSV导出失败：{str(e)}")
        return False


def export_stats_to_json(dataset: AudioDataset, output_path: str) -> bool:
    """导出统计结果为JSON"""
    try:
        stats = {
            "总样本数": dataset.get_total_count(),
            "独立说话人数": dataset.get_speaker_count(),
            "标签统计": dataset.get_label_stats(),
            "总时长(秒)": round(dataset.get_total_duration(), 2)
        }
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
        logger.info(f"JSON统计导出成功：{output_path}")
        return True
    except Exception as e:
        logger.error(f"JSON导出失败：{str(e)}")
        return False
