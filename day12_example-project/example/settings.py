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


# 配置去重容器的类: 基于Redis的set的去重容器, 用于存储已爬的指纹字符串数据
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 配置调度器类: 实现一个基于Redis的zset的队列, 用于存储待爬取的请求对象
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 用于配置调度器是否需要持久化
# 如果为True, 当程序结束了, 依然会保留Redis中的指纹和待爬的请求
# 如果为False, 当程序结束了, 依然会请空Redis中的指纹和待爬的请求
SCHEDULER_PERSIST = True
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    # 用于把数据存储到Redis数据库中
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

# 配置Redis数据链接
# 方式1: 配置主机和端口号
# REDIS_HOST = '127.0.0.1'
# REDIS_PORT = 6379
# 方式2: 配置REDIS的URL(推荐)
REDIS_URL= 'redis://127.0.0.1:6379/1'



LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1
