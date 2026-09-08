# '''
# 索引与切片
# 给定时间字符串 `time_str = "2026-09-07 14:25:30"`
# 1. 用切片提取日期部分 `2026-09-07`
# 2. 用切片提取小时 `14`
# 3. 用反向切片提取秒数 `30`
# '''
# time_str = "2026-09-07 14:25:30"
# print(f'日期：{time_str[:10]}')
# print(f'小时{time_str[11:13]}')
# print(f'秒数{time_str[-2:]}')

# '''
# # find + 切片
# # 给定日志行：`log = "[INFO] 2026-09-07 用户登录成功 user_id=10086"`
# # 1. 用 `find()` 找到 `]` 的位置
# # 2. 基于该位置，切片提取出日志级别 `INFO`
# # 3. 切片提取出后面的完整消息内容
# # '''
# log = "[INFO] 2026-09-07 用户登录成功 user_id=10086"
# index = log.find(']')
# level = log[1:index]
# content = log[index+1:].strip()  #去掉首尾空格
# print(level)
# print(content)


# '''
# strip + split
# 给定原始读取的文件行：`line = "  gen_spk07_real.wav  \n"`
# 1. 去除首尾空白和换行符
# 2. 按下划线 `_` 分割成三部分
# 3. 打印分割后的列表
# '''
# line = "  gen_spk07_real.wav  \n"
# line1 = line.strip()
# print(line1)
# line_list = line1.split('_')
# print(line_list)

# '''
# replace + 字符串格式化
# 给定变量：`speaker = "spk12"`、`total = 156`、`real_count = 89`
# 1. 计算真实样本占比（保留 1 位小数）
# 2. 用 f-string 格式化输出：`说话人spk12：总计156条，真实样本89条，占比57.1%`
# '''
# speaker = "spk12"
# total = 156
# real_count = 89
# real_sample = real_count / total
# print(f'说话人{speaker}：总计{total}条，真实样本{real_count}条，占比{real_sample * 100:0.1f}%')


'''
音频文件名解析
输入一个音频文件名字符串，例如 `audio_name = "dataset_01_gen_spk03_fake.wav"`
要求：
- 提取说话人 ID（如 `03`）
- 提取标签（`real` / `fake`）
- 最终返回字典格式：`{"speaker_id": "03", "label": "fake"}`
提示：可以多次 split，或者结合 find 定位。
'''
name = input('请输入一个音频文件名字符串：')
name_no_ext = name.split('.')[0]
name_list = name_no_ext.split('_')
print(name_list)
name_dict = {}
for part in name_list:
    if part.startswith('spk'):
        name_dict['speaker_id'] = part[3:]
    elif part in ('real','fake'):
        name_dict['label'] = part
print(name_dict)

# '''
# 日志字段拼接
# 给定列表 `fields = ["2026-09-07", "14:25:30", "ERROR", "数据库连接失败", "1001"]`
# 要求：
# 1. 用逗号 `,` 拼接成标准 CSV 格式字符串
# 2. 用 `|` 拼接成日志展示格式
# 3. 分别打印两个结果
# '''
# fields = ["2026-09-07", "14:25:30", "ERROR", "数据库连接失败", "1001"]
# fields_csv = ','.join(fields)
# fields_log = ' | '.join(fields)
# print(fields_csv)
# print(fields_log)