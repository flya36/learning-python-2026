'''有一个服务器访问日志文件 access.log,每行格式为:IP地址 - - [时间] "请求方法 路径 协议" 状态码 响应大小。
请编写函数 analyze_log(log_path, output_csv)，完成以下功能：
读取日志文件，逐行解析，提取 IP 地址和 HTTP 状态码；
统计每个 IP 的总请求次数、404 错误次数；
按总请求次数降序排序；
将统计结果写入 CSV 文件，表头为 ip,total_requests,error_404;
异常处理：日志文件不存在、行格式解析失败时，跳过该行并计数。'''
import csv
from pathlib import Path
def analyze_log(log_path, output_csv):
    # IP地址 - - [时间] "请求方法 路径 协议" 状态码 响应大小
    # 读取日志文件，逐行解析，提取 IP 地址和 HTTP 状态码
    log_path = Path(log_path)
    output_csv = Path(output_csv)
    if not log_path.exists() or not log_path.is_file():
        print(f'{log_path}不存在')
    else:
        res = {}
        with open(log_path,'r',encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                line.strip()
                if not line:
                    continue
                parts = line.split()
                if len(parts) != 8:
                    print('行格式解析失败')
                    continue
                ip = parts[0]
                state = parts[-2]
                if ip not in res:
                    res[ip] = {
                        'total_requests':0,
                        'error_404':0
                    }
                res[ip]['total_requests'] += 1
                if state == '404':
                    res[ip]['error_404'] += 1
        # 按总请求次数降序排序
        res = dict(sorted(res,key=lambda x:res[x]['total_requests'],reverse=True))
        # 将统计结果写入 CSV 文件，表头为 ip,total_requests,error_404
        output_csv.parent.mkdir(parents=True,exist_ok=True)
        filednames = ['ip','total_requests','error_404']
        with open(output_csv,'w',encoding='utf-8',newline='') as f:
            writer = csv.DictWriter(f,fieldnames=filednames)
            writer.writeheader()
            writer.writerows({'ip':id,'total_requests':info['total_requests'],'error_404':info['error_404']} for id,info in res.items())