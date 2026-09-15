import json
# 记住ensure_ascii,indent,sort_keys这几个参数
json.dumps(ensure_ascii=False,indent=2,sort_keys=True)    #将dict转换为json类型（字符串）
json.dump(ensure_ascii=False,indent=2,sort_keys=True)     #dump用于创建json文件语句（文件数据之前是用字典的形式）
json.load()     #load用于将json

#csv是一种表格文件，可用excel打开
import csv
reader = csv.DictReader()     #将csv文件内容读到reader中去（每行为字典形式）
# 创建csv文件时，要防止空行存在，可以在with open（）中加上newline=''
with open(file_path,'w',encoding='utf-8',newline='') as f:
    writer = csv.DictWriter(f,fieldnames=fieldnames)        #表示要创建csv文件，并指定表头为fielnames
    writer.writeheader()    #写入表头
    writer.writerows(data)      #写入多行数据（每行为一个字典）
    writer.writerow()       #写入一行数据

# pathlib是文件操作（用于路径和创建目录等）
from pathlib import Path
file_name = Path(file_name)     #将字符串file_name变为文件对象
file_name.exists()      #判断文件是否存在，返回bool值
file_name.is_file()     #判断是不是文件
file_name.is_dir()      #判断是不是文件夹
# 提取文件名，文件后缀，文件名（不带后缀），父目录(上一级文件)
file_name.name      #是属性，不带（）
file_name.suffix
file_name.stem
file_name.parent
# 创建文件夹-->mkdir()
file_dir.mkdir(parents=True,exist_ok=True)      #parents=True(父文件夹不存在一起创建) exis_ok=True(文件夹已经存在也不报错)
# 遍历文件夹里的文件
file_dir.glob('.wav')       #遍历返回文件对象，可用list()强制转换为列表
file_dir.rglob('.wav')      #不仅遍历该目录下的文件，还可遍历该目录下存在的文件夹（属于递归）