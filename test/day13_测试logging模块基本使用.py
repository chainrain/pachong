import logging

# 默认日志等级: 警告
# 设置日志级别
logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.WARNING)
# logging.basicConfig(level=logging.ERROR)
# logging.basicConfig(level=logging.CRITICAL)


logging.debug('调试信息')
logging.info('程序运行状态信息')
logging.warning('警告信息')
logging.error('错误信息')
logging.critical('严重错误信息')


# 记录异常日志

# ex = Exception('我错了')
# logging.exception(ex)
# 记录异常日志, 需要try...except中,捕获异常, 然后进行记录
try:
    raise Exception('我错了')
except Exception as ex:
    logging.exception(ex)

