# 把一组模拟日志数据组织成 “字典列表” 结构，完成按 IP 统计出现次数的小练习
# 字典列表：[{k:v},{k:v},{k:v}]多个字典，字典创建应在循环里面
log_records = []
ip_count = {}
while True:
    ip = input('请输入ip(输入-1视为结束):')
    if ip == '-1':
        break
    else:
        time = input('请输入时间')
        log_record = {'ip':ip,'time':time}
        log_records.append(log_record)
print(log_records)
for log in log_records:
    ip = log['ip']
    if ip not in ip_count:
        ip_count[ip] = 1
    else:
        ip_count[ip] += 1
print(ip_count)