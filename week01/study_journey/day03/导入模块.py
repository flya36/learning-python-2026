# 1.导入模块 ---> 调用方式：模块名.功能名 /别名.功能名
# 第一种
import random
random.randint(1,100)
# 第二种
import random as rd
rd.randint(1,23)

# 2.导入模块中的具体功能 ---> 调用方式：功能名() /功能别名（）
# 第一种
from random import randint
randint(1,41)
# 第二种
from random import randint as ri
ri(93,149)
# 第三种
from random import *
randint(2,41)