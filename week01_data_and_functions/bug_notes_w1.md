---
## 🐛 Bug 记录（实时更新）
见 [bug_notes_w1.md](./bug_notes_w1.md)
| 序号 | 现象 | 原因 | 解决 | 如何避免 |
|:---:|:---|:---|:---|:---|
| 1 |没有输入值调用函数直接结束|函数中判断列表是否为空不能用None，None是用来判断是不是空值而不是用来判断是不是空列表|将if scores is None 改为if not scores |分清楚空值和空列表/空元组等区别|
| 2 |path模块切割文件后缀和判断对象是不是目录出错|判断是不是目录用.is_dir()这个是方法后面必须加(),而切割文件名后缀.stem是属性，后面不能加()|在.is_dir后面加上(),在.stem后面删去()|记住判断是不是目录和是不是文件（.is_file()/.is_dir()）都要加(),提取文件名（.stem/.parent/.suffix/.name）都不能加()|
| 3 |报错：FileNotFoundError|添加文件时没有查看目录是否存在|直接使用.mkdir(parents=True,exist_ok=True),这样无论是否存在目录都不会报错|在添加文件时记得先创建目录|