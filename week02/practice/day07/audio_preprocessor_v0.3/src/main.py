import logging
from pathlib import Path
from utils.logger import logger  # 触发日志配置（basicConfig）
from models.audio_sample import AudioDataset
from core.parser import scan_audio_dir
from core.exporter import export_to_csv, export_stats_to_json

logger = logging.getLogger(__name__)

def main(audio_dir: str, output_dir: str = "../output"):
    # 1. 创建输出目录
    Path(output_dir).mkdir(exist_ok=True)

    # 2. 扫描目录 + 解析样本
    logger.info(f"开始扫描音频目录：{audio_dir}")
    sample_list = scan_audio_dir(audio_dir)

    # 3. 构建数据集（组合模式：把样本装进Dataset）
    dataset = AudioDataset()
    success_num = dataset.add_samples(sample_list)
    logger.info(f"数据集构建完成，共载入{success_num}个样本")

    # 4. 打印统计信息
    label_stats = dataset.get_label_stats()
    logger.info("=== 数据统计 ===")
    logger.info(f"总样本数：{dataset.get_total_count()}")
    logger.info(f"说话人数：{dataset.get_speaker_count()}")
    logger.info(f"标签分布：{label_stats}")
    logger.info(f"总时长：{round(dataset.get_total_duration(), 2)}秒")

    # 5. 导出结果
    csv_path = f"{output_dir}/audio_samples.csv"
    json_path = f"{output_dir}/audio_stats.json"

    export_to_csv(dataset, csv_path)
    export_stats_to_json(dataset, json_path)

    logger.info("处理完成！")


if __name__ == "__main__":
    # 测试：替换为你的音频文件夹路径（相对 src 目录）
    AUDIO_DIR = "../data/test_audio"
    main(AUDIO_DIR)
