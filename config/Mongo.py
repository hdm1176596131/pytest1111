from pymongo import MongoClient
import yaml
import os

paths = os.path.dirname(os.path.abspath(__file__))  # 当前路径
root_path = os.path.dirname(paths)  # 上一层目录


class Mongo:
    # 数据库初始化连接
    def __init__(self):
        try:
            with open(os.path.join(root_path, 'config/base.yaml'), "r", encoding="utf8") as f:
                get_back = yaml.load(f, Loader=yaml.FullLoader)
                host = get_back['test_db']['host']
                port = get_back['test_db']['port']
                user = get_back['test_db']['user']
                pwd = get_back['test_db']['pwd']
                self.client = MongoClient(host=host, port=port, username=user, password=pwd)
                # print(client.list_database_names())
        except Exception as e:
            print(e)

    pass

    # 连接一号数据库
    def first(self):
        db = self.client.houtai_yb
        return db

    pass

    # 连接二号数据库
    def second(self):
        db = self.client.jzPlatformGame_yb
        return db

    pass

    # 连接三号数据库
    def thirdly(self):
        db = self.client.jzPlatformLog_yb
        return db

    pass

    # 连接四号数据库
    def fourthly(self):
        db = self.client.jzPlatformShare_yb
        return db

    pass

    # 连接对应单个表
    @staticmethod
    def collection_tb_manage_user():
        col = Mongo().first().tb_manage_user
        return col

    pass


if __name__ == '__main__':
    collection = Mongo.collection_tb_manage_user()
    res = collection.find_one({'account': '120298'})
    print(res)
