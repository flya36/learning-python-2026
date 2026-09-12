'''
封装一个函数 `parse_audio_path(file_path)`，模拟当天项目中的 `parse_audio_path` 功能。
函数接收一个音频文件的完整路径字符串，格式为 `数据集/说话人ID/标签_文件名.wav`，例如 `data/speaker_01/real_001.wav`，返回三个值：
- 说话人 ID(speaker_id)
- 标签(label,real/fake)
- 文件名（不含路径）
额外要求：
- 增加可选参数 `delimiter`，默认值为 `_`，支持自定义分隔符
- 如果路径格式不符合预期（缺少分隔符、后缀不是 wav)，返回 `(None, None, None)`
- 主程序传入 3 条不同路径测试，包括 1 条异常路径
'''
def parse_audio_path(file_path: str, delimiter: str = "_") -> tuple:
    """
    解析音频文件路径，返回 (说话人ID, 标签, 文件名)
    :param file_path: 完整文件路径，格式：数据集/说话人ID/标签_文件名.wav
    :param delimiter: 文件名分隔符，默认下划线
    :return: 解析结果；格式错误返回 (None, None, None)
    """
    # 校验后缀（不区分大小写）
    if not file_path.lower().endswith(".wav"):
        return None, None, None
    
    # 按路径分隔符拆分
    parts = file_path.replace("\\", "/").split("/")
    if len(parts) < 3:
        return None, None, None
    
    file_name = parts[-1]
    speaker_id = None
    label = None
    
    # 提取说话人ID
    for part in parts:
        if part.startswith("speaker"):
            speaker_id = part
            break
    
    # 按分隔符解析文件名，提取标签
    name_parts = file_name.split(delimiter)
    if len(name_parts) >= 2 and name_parts[0] in ("real", "fake"):
        label = name_parts[0]
    
    # 任一信息缺失则返回异常
    if not speaker_id or not label:
        return None, None, None
    
    return speaker_id, label, file_name


# 主程序测试
if __name__ == "__main__":
    test_paths = [
        "data/speaker_01/real_001.wav",       # 正常路径
        "dataset/speaker_02/fake_003.wav",     # 正常路径
        "data/unknown/test.wav",               # 异常：无speaker、无标签
        "data/speaker_03/real_005.mp3"         # 异常：后缀错误
    ]
    
    for path in test_paths:
        result = parse_audio_path(path)
        print(f"路径: {path}")
        print(f"解析结果: {result}\n")
