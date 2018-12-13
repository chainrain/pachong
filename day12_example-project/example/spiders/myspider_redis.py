from scrapy_redis.spiders import RedisSpider

# 对比继承Spider

# 1. 继承关系: RedisSpider
class MySpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'myspider_redis'

    # 2. 少了start_urls, 增加了redis_key
    # redis_key: 用于指定起始URL在Redis数据库的key
    # redis_key用于指定Redis数据库的地址 对吗?
    # Redis数据库的地址: Redis数据库IP和端口号
    redis_key = 'myspider:start_urls'

    # 可选的, 一般都不写
    # 动态生成allowed_domains, 根据起始URL生成一个allowed_domains
    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(MySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }
