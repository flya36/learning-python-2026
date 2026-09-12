'''
先手动创建一个 `sample_log.txt` 文件，写入以下模拟日志内容
2026-09-02 09:12:01 [INFO] 开始扫描音频目录
2026-09-02 09:12:03 [INFO] 找到 12 个 wav 文件
2026-09-02 09:12:05 [ERROR] 文件 sample_007.wav 格式损坏
2026-09-02 09:12:07 [INFO] 完成样本统计
2026-09-02 09:12:09 [ERROR] 读取 speaker_03 目录失败
2026-09-02 09:12:10 [INFO] 程序退出
'''
import os
print("当前工作目录：", os.getcwd())

with open('./sample_log.txt','w',encoding='utf-8')as f:
    f.write('2026-09-02 09:12:01 [INFO] 开始扫描音频目录\n')
    f.write('2026-09-02 09:12:03 [INFO] 找到 12 个 wav 文件\n')
    f.write('2026-09-02 09:12:05 [ERROR] 文件 sample_007.wav 格式损坏\n')
    f.write('2026-09-02 09:12:07 [INFO] 完成样本统计\n')
    f.write('2026-09-02 09:12:09 [ERROR] 读取 speaker_03 目录失败\n')
    f.write('2026-09-02 09:12:10 [INFO] 程序退出')