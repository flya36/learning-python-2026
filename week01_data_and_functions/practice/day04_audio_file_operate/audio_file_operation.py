'''
1. 使用 `with` 语句完成以下流程：
   - 读取 `audio_list.txt`，逐行处理
   - 去除每行首尾空白，跳过空行
   - 筛选出后缀为 `.wav` 的文件路径
   - 将所有有效 wav 路径写入新文件 `valid_audio.txt`，每行一个路径
2. 最后读取 `valid_audio.txt`，打印所有有效路径和总数量。
'''
# content = []
# with open(r'week01_data_and_functions\practice\day04_audio_file_operate\audio_list.txt','r',encoding='utf-8') as f:
#     lines = f.readlines()
#     for line in lines:
#         if not line:
#             continue
#         line1 = line.strip()
#         if line1.endswith('.wav'):
#             content.append(line)
# with open(r'week01_data_and_functions\practice\day04_audio_file_operate\valid_audio.txt','w',encoding='utf-8') as f:
#     for line in content:
#         f.write(line)
# with open(r'week01_data_and_functions\practice\day04_audio_file_operate\valid_audio.txt','r',encoding='utf-8') as f:
#     print(f.readlines())
#     print(f'有效路径总数量：{len(content)}')

'''
1. 使用 with 语句完成以下流程：
   - 读取 audio_list.txt，逐行处理
   - 去除每行首尾空白，跳过空行
   - 筛选出后缀为 .wav 的文件路径
   - 将所有有效 wav 路径写入新文件 valid_audio.txt，每行一个路径
2. 最后读取 valid_audio.txt，打印所有有效路径和总数量。
'''

valid_paths = []

# 1. 读取原始列表，清洗+筛选
with open(r'week01_data_and_functions\practice\day04_audio_file_operate\audio_list.txt', 'r', encoding='utf-8') as f:
    for line in f:
        # 先去除首尾空白（换行、空格、制表符）
        path = line.strip()
        # 跳过空行
        if not path:
            continue
        # 统一转小写判断后缀，兼容 .WAV
        if path.lower().endswith('.wav'):
            valid_paths.append(path)

# 2. 写入有效路径文件
with open(r'week01_data_and_functions\practice\day04_audio_file_operate\valid_audio.txt', 'w', encoding='utf-8') as f:
    for path in valid_paths:
        f.write(path + '\n')  # 统一加换行

# 3. 读取结果并打印验证
print(f"有效 wav 文件共 {len(valid_paths)} 个：")
with open(r'week01_data_and_functions\practice\day04_audio_file_operate\valid_audio.txt', 'r', encoding='utf-8') as f:
    for path in f:
        print('-', path.strip())
