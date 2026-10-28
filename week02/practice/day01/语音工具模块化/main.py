import sta
stats = sta.audio_statistics("./example", "./output")
print("\n统计结果预览:")
print(f"总文件数: {stats['total_files']}")
print(f"说话人数量: {stats['speaker_count']}")
print(f"真实样本: {stats['real_count']} | 伪造样本: {stats['fake_count']}")
print(f"总时长: {stats['total_duration_min']} 分钟")