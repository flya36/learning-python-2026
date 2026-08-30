'''给定访问日志列表，列表每个元素是访问 IP 字符串。
请写函数`count_ip(log_list)`,返回字典:key 为 ip,value 是该 ip 出现的访问次数。
'''
'''
def count_ip(log_list):
    log_key = list(set(log_list))
    log_dict = {}
    for key in log_key:
        log_dict[key] = log_list.count(key)
    return log_dict
(这一个可以但时间复杂度是n**2,实际项目不这样写)
'''
#修改
def count_ip(log_list):
    log_dict = {}
    for ip in log_list:
        if ip in log_dict:
            log_dict[ip] += 1
        else:
            log_dict[ip] = 1
    return log_dict

log_list = []
while True:
    log = input('请输入访问日志(输入-1视为结束)')
    if log == '-1':
        print('输入完毕')
        break
    else:
        log_list.append(log)
print(count_ip(log_list))



'''提取不重复说话人（去重｜集合）
语音项目场景：传入音频文件对应的说话人 id 列表，返回所有不重复的说话人，转为列表输出。
函数名`get_unique_speaker(speaker_list)`
'''
def get_unique_speaker(id_list):
    unique_speaker_id_list = list(set(id_list))
    return unique_speaker_id_list
id_list = []
while True:
    id = input('请输入说话人id(输入-1视为结束)') 
    if id == '-1':
        break
    id_list.append(id)
print(get_unique_speaker(id_list))



'''
统计列表中出现次数大于 1 的元素（集合 + 字典组合）
输入一个字符串列表，找出所有重复出现过的元素，返回`{元素:出现次数}`的字典，只保留次数 > 1 的项。
函数名`find_dup_items(data_list)`
'''
'''
def find_dup_items(data_list):
    data_key = list(set(data_list))
    data_dict = {}
    for key in data_key:
        if data_list.count(key) > 1:
            data_dict[key] = data_list.count(key)
    return data_dict
(一样的问题，时间复杂度太大，实际项目不这样写，还是直接字典遍历)
'''
#修改
def find_dup_items(data_list):
    temp = {}
    for item in data_list:
        if item in temp:
            temp[item] +=1
        else:
            temp[item] =1
    # 筛选只保留次数大于1
    res = {k:v for k,v in temp.items() if v>1}
    return res

data_list = []
while True:
    data = input('请输入列表元素(输入-1视为结束)')
    if data == '-1':
        print('输入完毕')
        break
    else:
        data_list.append(data)
print(find_dup_items(data_list))



'''
统计每个说话人的音频片段数量
输入：片段所属说话人 id 列表，每个元素代表一段音频归属哪个说话人。
编写函数 `count_speaker_segment(speaker_segs)`
返回字典:key = 说话人 id,value = 该说话人一共有多少段音频。
'''
def count_speaker_segment(speaker_segs):
    count_ip = {}
    for id in speaker_segs:
        if id in count_ip:
            count_ip[id] += 1
        else:
            count_ip[id] = 1
    return count_ip
id_list = []
while True:
    id = input('请输入片段所属说话人 id 列表(输入-1视为结束):')
    if id == '-1':
            print('输入完毕')
            break
    id_list.append(id)
print(count_speaker_segment(id_list))



'''
过滤访问量超过 2 次的 IP
输入 IP 日志列表，编写函数 `filter_high_freq_ip(logs)`
1. 一次遍历统计每个 IP 访问次数
2. 使用字典推导式，只保留访问次数 > 2 的 IP
返回过滤后的频次字典
'''
def filter_high_freq_ip(logs):
    ip_dict = {}
    for ip in logs:
        if ip in ip_dict:
            ip_dict[ip] += 1
        else:
            ip_dict[ip] = 1
    res = {i:c for i,c in ip_dict.items() if c > 2}
    return res
ip_list = []
while True:
    ip = input('请输入 IP 日志列表(输入-1视为结束):')
    if ip == '-1':
            print('输入完毕')
            break
    ip_list.append(id)
print(filter_high_freq_ip(ip_list))