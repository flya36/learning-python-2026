import logging
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict

logger = logging.getLogger(__name__)


@dataclass
class AudioSample:
    """单个音频样本数据模型（对应单个wav文件）"""
    file_path: str       # 音频文件完整路径
    speaker_id: str      # 说话人ID
    label: bool          # 标签：True=真实语音 / False=克隆语音
    duration: float = 0.0  # 音频时长（秒），基础版暂占位，后续可接入librosa

    def is_file_valid(self) -> bool:
        """校验文件是否存在"""
        return Path(self.file_path).exists()


class AudioDataset:
    """
    音频数据集类（组合模式核心）
    不继承AudioSample，而是通过内部列表包含多个AudioSample对象
    """
    def __init__(self):
        # 组合的核心：用列表存储所有AudioSample实例
        self._samples: List[AudioSample] = []

    def add_sample(self, sample: AudioSample) -> bool:
        """添加单个样本，自动校验有效性"""
        if not isinstance(sample, AudioSample):
            logger.error(f"添加失败：类型错误，仅支持AudioSample，传入{type(sample)}")
            return False
        if not sample.is_file_valid():
            logger.warning(f"文件不存在，跳过：{sample.file_path}")
            return False

        self._samples.append(sample)
        logger.debug(f"已添加样本：{sample.file_path}")
        return True

    def add_samples(self, sample_list: List[AudioSample]) -> int:
        """批量添加样本，返回成功添加数量"""
        success_count = 0
        for sample in sample_list:
            if self.add_sample(sample):
                success_count += 1
        logger.info(f"批量添加完成：成功{success_count}个，失败{len(sample_list)-success_count}个")
        return success_count

    # ---------------------- 统计功能（基于内部样本组合实现） ----------------------
    def get_total_count(self) -> int:
        """总样本数"""
        return len(self._samples)

    def get_speaker_count(self) -> int:
        """独立说话人数量"""
        speakers = {sample.speaker_id for sample in self._samples}
        return len(speakers)

    def get_label_stats(self) -> Dict[str, int]:
        """真假样本统计"""
        real = sum(1 for s in self._samples if s.label)
        fake = sum(1 for s in self._samples if not s.label)
        return {"真实语音": real, "克隆语音": fake, "总计": real + fake}

    def get_total_duration(self) -> float:
        """总时长（秒）"""
        return sum(sample.duration for sample in self._samples)

    def get_all_samples(self) -> List[AudioSample]:
        """获取所有样本（供导出模块使用）"""
        return self._samples.copy()  # 返回副本，避免外部修改内部数据
