# csv:表格文件
import csv
from pathlib import Path

# # 定义csv文件路径
# current_dir = Path(__file__).parent
# csv_path = current_dir/'audio_list.csv'
# # 打开csv文件并阅读
# with open(csv_path,'r',encoding='utf-8')as f:
#     # 读取csv文件-->.DictReader(自动把第一行当表头)
#     reader = csv.DictReader(f)
#     # 逐行读取，每行都是一个字典
#     for row in reader:
#         print('文件路径，',row['file_path'])
#         print('说话人ID,',row['speaker_id'])
#         print('标签，',row['label'])
#         print('时长，',row['duration'])
#         print('---')



current_dir = Path(__file__).parent
output_path = current_dir/'output'/'statistics.csv'
# 创建output文件夹-->mkdir只能用于创建文件夹，因此只能先创建output文件夹，后续再创建文件夹下的csv文件
output_path.parent.mkdir(parents=True,exist_ok=True)
# 定义表头
fieldnames = ['speaker_id','total_samples','real_samples','fake_samples']
# 要写入的数据，列表中装字典，每个字典一行
data = [
    {'speaker_id':'speaker_001','total_samples':42,'real_samples':21,'fake_samples':21},
    {'speaker_id':'speaker_002','total_samples':43,'real_samples':22,'fake_samples':21},
]
# 打开文件，写入数据
# newline=“”-->避免csv出现多余空行
with open(output_path,'w',encoding='utf-8',newline='')as f:
    # 创建dictwriter对象，指定表头为fieldnames
    writer = csv.DictWriter(f,fieldnames=fieldnames)
    # 写入表头
    writer.writeheader()
    # 写入一行数据
    writer.writerow({'speaker_id':'speaker_001','total_samples':42,'real_samples':21,'fake_samples':21})
    # 写入多行数据
    writer.writerows(data)