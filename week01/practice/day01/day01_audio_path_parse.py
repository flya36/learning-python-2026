# def audio_path_parse(file_name):
#     name_dict = {}
#     name_dict['file_name'] = file_name
#     name_no_ext = file_name.split('.')[0]
#     name_list = name_no_ext.split('_')
#     for part in name_list:
#         if part.startswith('spk'):
#             name_dict['speaker_id'] = part[3:]
#         elif part in ('real','fake'):
#             name_dict['label'] = part
#     return name_dict
# while True:
#     name = input('请输入一个音频文件名字符串(输入-1视为结束):')
#     if name == '-1':
#         break
#     else:
#         print(audio_path_parse(name))

def audio_path_parse(file_name):
    # 预先初始化全部key，防止后面KeyError
    name_dict = {
        "file_name": file_name,
        "speaker_id": "",
        "label": ""
    }
    # 去掉后缀，只处理文件名主体
    name_no_ext = file_name.split('.')[0]
    name_list = name_no_ext.split('_')
    for part in name_list:
        if part.startswith('spk'):
            name_dict['speaker_id'] = part[3:]
        elif part in ('real', 'fake'):
            name_dict['label'] = part
    # 只返回，不在函数内部print
    return name_dict

while True:
    name = input('请输入一个音频文件名字符串(输入-1视为结束):')
    if name == "-1":
        break
    res = audio_path_parse(name)
    print(res)