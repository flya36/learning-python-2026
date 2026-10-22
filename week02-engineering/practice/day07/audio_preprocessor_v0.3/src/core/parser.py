import logging
from pathlib import Path
from typing import List
import soundfile as sf
from models.audio_sample import AudioSample

logger = logging.getLogger(__name__)


def get_audio_duration(file_path: str) -> float:
    """读取音频真实时长（秒），失败时返回0.0"""
    try:
        return round(sf.info(file_path).duration, 3)
    except Exception as e:
        logger.warning(f"读取音频时长失败 {Path(file_path).name}：{str(e)}")
        return 0.0


def parse_audio_path(file_path: str) -> AudioSample:
    """
    从音频文件路径解析样本信息
    文件名约定格式：speaker001_real_001.wav 或 speaker002_fake_003.wav
    """
    path = Path(file_path)
    if path.suffix.lower() not in [".wav", ".mp3"]:
        raise ValueError(f"不支持的音频格式：{path.suffix}")

    # 从文件名提取说话人ID和标签
    filename = path.stem  # 不带后缀的文件名
    parts = filename.split("_")

    if len(parts) < 2:
        raise ValueError(f"文件名格式错误，无法解析：{filename}")

    speaker_id = parts[0]
    label_str = parts[1].lower()

    if label_str not in ["real", "fake"]:
        raise ValueError(f"标签识别失败：{label_str}，仅支持real/fake")

    label = label_str == "real"

    return AudioSample(
        file_path=str(path.absolute()),
        speaker_id=speaker_id,
        label=label,
        duration=get_audio_duration(str(path.absolute()))
    )


def scan_audio_dir(dir_path: str) -> List[AudioSample]:
    """遍历目录，解析所有音频文件，返回样本列表"""
    dir_path = Path(dir_path)
    if not dir_path.is_dir():
        raise NotADirectoryError(f"目录不存在：{dir_path}")

    samples = []
    for audio_file in list(dir_path.rglob("*.wav")) + list(dir_path.rglob("*.mp3")):
        try:
            sample = parse_audio_path(str(audio_file))
            samples.append(sample)
        except Exception as e:
            logger.warning(f"解析文件失败 {audio_file.name}：{str(e)}")

    logger.info(f"目录扫描完成：共找到{len(samples)}个有效音频文件")
    return samples
