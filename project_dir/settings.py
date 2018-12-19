# 配置日志文件路径
DEFAULT_LOG_FILENAME = 'baidu.log'

# 配置和开启爬虫
SPIDERS = [
    'spiders.baidu_spider.BaiduSpider',
    # 'spiders.douban_spider.DoubanSpider'
]

# 配置和开启管道
PIPELINES = [
   'pipelines.BaiduPipeline',
   'pipelines.DoubanPipeline',
]

# # 配置和开启下载器中间件
# DOWNLOADER_MIDDLEWARES = [
#     'middlewares.downloader_middlewares.DownloaderMiddleware1',
#     'middlewares.downloader_middlewares.DownloaderMiddleware2',
# ]
#
# # 配置和开启爬虫中间件
# SPIDER_MIDDLEWARES = [
#     'middlewares.spider_middlewares.SpiderMiddleware1',
#     'middlewares.spider_middlewares.SpiderMiddleware2',
# ]