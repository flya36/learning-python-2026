f = open(r'E:\python learning\learning-python-2026\week01_data_and_functions\practice\day04_file_operation\sample_log.txt','r',encoding='utf-8')
print(f.read())
f.close()


# 使用 `with` 上下文管理器打开文件，逐行读取，统计并输出：文件总行数、`[ERROR]` 出现的行数。
# with open(r'.\week01_data_and_functions\practice\day04_file_operation\sample_log.txt','r',encoding='utf-8')as f:
#     lines = f.readlines()
#     stas = {'文件总行数':len(lines),'[ERROR]出现的行数':0}
#     for line in lines:
#         if 'ERROR' in line:
#             stas['[ERROR]出现的行数'] += 1
#     print(stas)
stas = {'文件总行数':0,'[ERROR]出现的行数':0}
with open(r'.\week01_data_and_functions\practice\day04_file_operation\sample_log.txt','r',encoding='utf-8')as f:
    for line in f:
        stas["文件总行数"] +=1
        if "[ERROR]" in line:
            stas['[ERROR]出现的行数'] += 1
print(stas)
