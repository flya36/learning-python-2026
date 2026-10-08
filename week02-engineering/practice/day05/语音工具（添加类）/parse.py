'''实现完整流程:输入音频目录→遍历目录下所有音频文件→统计
(说话人数量、真假样本数、总时长)
→导出JSON/CSV格式的统计结果;'''
import wave
from pathlib import Path


def get_wav_duration(wav_path: Path) -> float:
    # 读取wav文件时长（秒），损坏文件返回0并提示
    try:
        with wave.open(str(wav_path), "rb") as wf:
            frames = wf.getnframes()    # 获取音频总采样帧数
            rate = wf.getframerate()    # 获取采样率（每秒多少帧
            return round(frames / rate, 2)  # 时长 = 总帧数 / 采样率，单位：秒
    except Exception as e:
        print(f"跳过损坏文件 {wav_path.name}: {e}")
        return 0.0