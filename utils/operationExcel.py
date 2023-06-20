#!/usr/bin/python
# -*- coding: utf-8 -*-
# 读取Excel表数据
import xlrd
from common import public


class OperationExcel:

    # 获取shell表
    def getSheet(self):
        book = xlrd.open_workbook(public.filePath())  # 前面已经默认将文件参数传递进去了，所以直接调用不用再传参了

        return book.sheet_by_index(0)  # 根据索引获取到sheet表

    # 以列表形式读取出所有数据
    def getExceldatas(self):
        data = []
        title = self.getSheet().row_values(0)  # 0获取第一行也就是表头
        for row in range(1, self.getSheet().nrows):  # 从第二行开始获取
            row_value = self.getSheet().row_values(row)
            data.append(dict(zip(title, row_value)))  # 将读取出每一条用例作为一个字典存放进列表
        return data


class ExcelVarles:
    case_Id = "用例Id"
    case_module = "用例模块"
    case_name = "用例名称"
    case_url = "用例地址"
    case_method = "请求方式"
    case_type = "请求类型"
    case_data = "请求参数"
    case_headers = "请求头"
    case_preposition = "前置条件"
    case_isRun = "是否执行"
    case_code = "状态码"
    case_result = "期望结果"

