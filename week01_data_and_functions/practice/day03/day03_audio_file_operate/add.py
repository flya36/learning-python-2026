# 新建 `audio_list.txt`，写入以下内容
content = '''./dataset/speaker_001.wav
./dataset/speaker_002.wav

./dataset/speaker_003.wav
./dataset/note.txt
./dataset/speaker_004.wav
./dataset/speaker_005.mp3
./dataset/speaker_006.wav'''
with open(r'week01_data_and_functions\practice\day04_audio_file_operate\audio_list.txt','w',encoding='utf-8')as f:
    f.write(content)