# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'


# 去重容器类: 用于把已爬指纹存储到基于Redis的set集合中
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 调度器: 用于把待爬请求存储到基于Redis的队列
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 是不进行调度持久化:
# 如果是True, 当程序结束的时候, 会保留Redis中已爬指纹和待爬的请求
# 如果是False, 当程序结束的时候, 会清空Redis中已爬指纹和待爬的请求
SCHEDULER_PERSIST = True
# SCHEDULER_PERSIST = False
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    # 用于把爬取到的数据, 存储Redis数据库中(可选)
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

# 配置Redis数据库连接
# 方式1: 配置IP和端口号
# REDIS_HOST = '127.0.0.1'
# REDIS_PORT = 6379
# 方法2; 配置Redis的URL
REDIS_URL = 'redis://127.0.0.1:6379/0'



LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1
