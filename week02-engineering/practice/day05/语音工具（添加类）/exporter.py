import json
import csv
from pathlib import Path

def _export_result(result: dict, output_dir: Path):
    """导出 JSON 和 CSV 两种格式"""
    json_path = output_dir / "audio_stats.json"
    csv_path = output_dir / "audio_stats.csv"

    speaker_detail_raw = result.get("speaker_detail", {})
    speaker_detail = speaker_detail_raw if isinstance(speaker_detail_raw, dict) else {}

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
        # 汇总行
        writer.writerow([])
        writer.writerow(["汇总", result["total_files"], result["real_count"],
                         result["fake_count"], result["total_duration_sec"],
                         result["total_duration_min"]])