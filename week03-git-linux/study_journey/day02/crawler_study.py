import requests
from lxml import html

# 定义url
target_url = "https://www.tiobe.com/tiobe-index/"

# 发送请求，获取数据
response = requests.get(target_url)

# # 输出
# print(response.text)

# 解析数据
doc = html.fromstring(response.text)
# 解析表头
table_head = doc.xpath('//table[@id = "top20"]/thead/tr/th/text()')
print(table_head)
# 解析表格数据
tr_list = doc.xpath('//table[@id = "top20"]/tbody/tr')
for tr in tr_list:
    td_list = tr.xpath('./td/text()')
    print(td_list)