import json

import pymysql
import yaml
import os

paths = os.path.dirname(os.path.abspath(__file__))  # 当前路径
root_path = os.path.dirname(paths)  # 上一层目录


class Mysql:

    """
    初始化数据库
    """
    def __init__(self):
        with open(os.path.join(root_path, 'config/base.yaml'), "r", encoding="utf8") as f:
            get_back = yaml.load(f, Loader=yaml.FullLoader)
            host = get_back['mysql_db']['host']
            port = get_back['mysql_db']['port']
            user = get_back['mysql_db']['user']
            pwd = get_back['mysql_db']['pwd']
            self.con = pymysql.connect(host=host, port=port, user=user, password=pwd, database='recreation', charset='utf8', autocommit=True)
            self.cursor = self.con.cursor()
    pass

    """
    封装查询
    """
    def sql_select(self, sql):
        cursor = self.cursor
        cursor.execute(sql)
        result_set = cursor.fetchall()
        rows = [list(i) for i in result_set]
        columns = [i[0] for i in cursor.description]
        json_data = []
        for row in rows:
            json_data.append(dict(zip(columns, row)))
        json_object = json.dumps(json_data, indent=4, ensure_ascii=False)
        return json.loads(json_object)

    pass

    """
    封装新增
    """
    def sql_add(self, sql):
        ad = self.cursor.execute(sql)  # 执行sql语句, 用变量ad来承接执行语句，返回受影响的行数，比如影响0行，返回0
        self.db.commit()  # 确认
        return ad

    """
    封装修改
    """
    def sql_update(self, sql):
        up = self.cursor.execute(sql)  # 执行sql语句, 用变量up来承接执行语句，返回受影响的行数，比如影响0行，返回0
        self.db.commit()  # 确认
        return up

    """
    封装删除
    """
    def sql_delete(self, sql):
        de = self.cursor.execute(sql)  # 执行sql语句, 用变量de来承接执行语句，返回受影响的行数，比如影响0行，返回0
        self.db.commit()  # 确认
        return de

    """
    关闭数据库连接
    """
    def __del__(self):
        # 关闭游标
        self.cursor.close()
        # 关闭数据库连接
        self.con.close()
    pass


if __name__ == '__main__':
    sql = """ select * from login where id = 3 """
    res = Mysql().sql_select(sql)
    print(res)
