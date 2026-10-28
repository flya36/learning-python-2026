'''
字符串清洗与字符统计
题目：给定原始字符串 `raw = "  Hello2026 World! \n"`
要求：
1. 先去除字符串首尾的所有空白（空格、换行符）
2. 统计清洗后的字符串里，**英文字母、数字、其他字符**分别有多少个
3. 按格式输出：`字母:xx个, 数字:xx个, 其他:xx个`
'''
raw = "  Hello2026 World! \n"
raw_clean = raw.strip()    #去除字符串首尾的所有空白
letter_count = 0
digit_count = 0
other_count = 0
for i in raw_clean:
    if i.isalpha():
        letter_count += 1
    elif i.isdigit():
        digit_count += 1
    else:
        other_count += 1
print(f'字母:{letter_count}个, 数字:{digit_count}个, 其他:{other_count}个')


'''
音频文件名格式化提取（贴合项目场景）
题目：给定音频文件名 `filename = "spk08_fake_clean.wav"`
命名规则：`说话人前缀_标签_备注.后缀`
要求：
1. 提取说话人数字编号：从 `spk08` 中提取出 `08`
2. 提取标签：`fake`
3. 将原文件名的后缀 `.wav` 替换为 `.json`，得到新文件名
4. 最终输出字典格式：`{"speaker_id": "08", "label": "fake", "new_filename": "spk08_fake_clean.json"}`
'''
filename = "spk08_fake_clean.wav"
audio_info = {}
audio_info["new_filename"] = filename.replace(".wav",".json")     # 将原文件名的后缀 `.wav` 替换为 `.json`
name_body = filename.split(".")[0]
parts = name_body.split("_")     #将文件名拆分成各个板块组成列表
for part in parts:
    if part.startswith("spk"):
        audio_info["speaker_id"] = part[3:]
    elif part in ("real","fake"):
        audio_info["label"] = part
print(audio_info)