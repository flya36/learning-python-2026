from pathlib import Path

# # 创建路径对象
# # __file__:当前文件路径，Path(__file__).parent:获取当前文件的所在文件夹路径
# current_dir = Path(__file__).parent
# print(current_dir)
# # audio_dir表示在当前文件所在文件夹下data/audio文件的路径
# audio_dir = current_dir/'data'/'audio'
# print(audio_dir)

# # 判断audio_dir文件夹是否存在
# print(audio_dir.exists())
# # 判断是文件还是文件夹
# print(current_dir.is_file())    #判断是不是文件-->返回False
# print(current_dir.is_dir())     #判断是不是文件夹-->返回True

# # 提取文件名，后缀，父目录
# file_path = Path('data/audio/speaker_001_001_real.wav')
# # 1.提取完整文件名
# print(file_path.name)
# # 2.提取不带后缀（.wav）的文件名
# print(file_path.stem)
# # 3.提取文件后缀（扩展名）（.wav）
# print(file_path.suffix)
# # 4.提取父目录
# print(file_path.parent)

# # 遍历文件夹里的文件
# audio_dir = Path('data/audio')
# # 遍历audio_dir下所有wav文件（只看当前文件夹，不进子文件夹）-->glob
# for wav_file in audio_dir.glob('*.wav'):
#     print(wav_file)
# # 遍历audio_dir下所有wav文件包括子文件夹下wav文件-->rglob(递归)
# for wav_file in audio_dir.rglob('*.wav'):
#     print(wav_file)

output_dir = Path('output/statistics')
# 创建文件夹-->.mkdir()
# parents=True：如果父文件夹不存在一起创建
# exist_ok=True：如果文件夹已经存在也不报错
output_dir.mkdir(parents=True,exist_ok=True)