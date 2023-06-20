from pymongo import MongoClient
import yaml
import os

paths = os.path.dirname(os.path.abspath(__file__))  # 当前路径
root_path = os.path.dirname(paths)  # 上一层目录


def get_data_from_yaml(files):
    with open(os.path.join(root_path, files), "r", encoding="utf8") as f:
        get_back = yaml.load(f, Loader=yaml.FullLoader)
    return get_back


if __name__ == '__main__':
    host = get_data_from_yaml('configs/base.yaml')['test_db']['host']
    port = get_data_from_yaml('configs/base.yaml')['test_db']['port']
    user = get_data_from_yaml('configs/base.yaml')['test_db']['user']
    pwd = get_data_from_yaml('configs/base.yaml')['test_db']['pwd']
    client = MongoClient(host=host, port=port, username=user, password=pwd)
    print(client.list_database_names())
    # 连接指定数据库
    db = client.houtai_yb
    # 连接指定表
    collection = db.tb_manage_user
    res = collection.find_one({'account': '120298'})
    print(res)
