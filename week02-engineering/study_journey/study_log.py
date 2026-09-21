# import logging

# # 设置日志级别和输出格式
# logging.basicConfig(level=logging.DEBUG)

# # 输出日志
# logging.debug("这是调试信息")
# logging.info("程序正常运行")
# logging.warning("这是一个警告")
# logging.error("发生了一个错误")
# logging.critical("严重错误，程序可能崩溃")

# import logging
# # 配置日志信息
# logging.basicConfig(
#     level=logging.DEBUG,        #debug以上（包含debug）日志信息都会打印出来
#     format="%(asctime)s | %(levelname)-8s | %(funcName)s:%(lineno)d | %(message)s",
#     handlers=[
#         logging.FileHandler("test.log", encoding="utf-8"),
#         logging.StreamHandler()
#     ]
# )
# logger = logging.getLogger(__name__)

# def divide(a, b):
#     logger.debug(f"开始计算：{a} / {b}")
#     try:
#         result = a / b
#         logger.info(f"计算成功：{result}")
#         return result
#     except ZeroDivisionError:
#         logger.exception("除数不能为0")
#         return None

# if __name__ == "__main__":
#     logger.info("程序启动")
#     divide(10, 2)
#     divide(10, 0)
#     logger.warning("这是一个测试警告")
#     logger.info("程序结束")


import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s | %(levelname)-8s | %(funcName)s:%(lineno)d | %(message)s',
    handlers=[logging.FileHandler('test.log',encoding='utf-8'),
              logging.StreamHandler()]
)
loger = logging.getLogger(__name__)
def divide(a,b):
    try:
        res = a/b
        return res
    except ZeroDivisionError:
        loger.exception('除数不能为0')
        loger.error('除数不能为0')
if __name__=='__main__':
    divide(10,5)
    divide(10,0)