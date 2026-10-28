class AudioSample:
    def __init__(self, file_path: str, speaker_id: str, label: str, duration: float):
        # 基础参数校验
        if duration < 0:
            raise ValueError(f"音频时长不能为负: {duration}")
        if not file_path:
            raise ValueError("文件路径不能为空")
            
        self.file_path = file_path
        self.speaker_id = speaker_id
        self.label = label  # real / fake
        self.duration = duration

    def __str__(self) -> str:
        return (f'文件路径:{self.file_path} | 说话人id:{self.speaker_id} '
                f'| 标签:{self.label} | 时长:{self.duration:.2f}s')

    def is_real(self) -> bool:
        """便捷方法：判断是否为真实样本"""
        return self.label == "real"
