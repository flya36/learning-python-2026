# 网络解析入门
from lxml import html

# 将html文件文本解析为文档对象
doc = html.fromstring(html.text)

# 解析表头
th_list  = doc.xpath('//table/thead/tr/th/text()' )
print(th_list)
# 解析所有行数据
tr_list = doc.xpath('//table/tbody/tr')
for tr in tr_list:
    td_list = tr.xpath('./td/text()')
    print(td_list)