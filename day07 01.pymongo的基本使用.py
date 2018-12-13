from pymongo import MongoClient

"""
mongdb和python交互的模块
pymongo 提供了mongdb和python交互的所有方法 安装方式: pip install pymongo
"""


class MongoTest(object):
    # 建立Mongodb的数据连接
    # 没有开启认证的模式
    # self.client = MongoClient()
    # 两种方式
    # 第一种方式
    # self.client = MongoClient(host='127.0.0.1', port=27017, username='py6', password='123')
    # 指定URI
    def __init__(self):
        self.client = MongoClient()
        # 创建数据连接对象,如果没有的话会自动生成 client[db名][集合名]
        self.collection = self.client['py06']['pymongo_test']

    def insert_one(self):
        """插入一条数据"""
        self.collection.insert_one({'name': 'chainrain01', 'age': 16})

    def insert_more(self):
        datas = [{'name': 'chainrain{}'.format(i), 'age': i} for i in range(1, 20)]
        self.collection.insert_many(datas)

    def update_one(self):
        self.collection.update_one()

if __name__ == '__main__':
    mt = MongoTest()
    # mt.insert_one()
    mt.insert_more()