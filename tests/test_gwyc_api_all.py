import allure
import pytest
import json
from base import method
from utils import operationExcel
from utils.LogsUtil import LogsUtil
@allure.epic("s")
@allure.feature('ssss')
class TestLogIn:
    @allure.story("sssada")
    def a(self):
        print("ssss")

    pass

    @allure.story("测试登录")
    @pytest.mark.parametrize('data', operationExcel.OperationExcel().getExceldatas())  # 装饰器进行封装用例
    def test_gwyc_api(self,data):
        # 对请求头作为空处理并添加token
        headers = data[operationExcel.ExcelVarles.case_headers]
        if len(str(headers).split()) == 0:
            pass
        elif len(str(headers)) >= 0:
            headers = json.loads(headers)  # 转换为字典
            #        headers['Authorization']=company_login_token#获取登录返回的token并添加到读取出来的headers里面
            headers = headers

        # 对请求参数做为空处理
        params = data[operationExcel.ExcelVarles.case_data]
        if len(str(params).split()) == 0:
            pass
        elif len(str(params)) >= 0:
            params = params

        # 断言封装

        case_code = int(data[operationExcel.ExcelVarles.case_code])

        def case_result_assert(r):
            assert r.json()['code'] == case_code  # 状态码
            # assert data[operationExcel.ExcelVarles.case_result] in json.dumps(r.json(), ensure_ascii=False)  # 响应数据

        # 执行用例
        if data[operationExcel.ExcelVarles.case_method] == 'get':
            r = method.ApiRequest().send_requests(
                method='get',
                url=data[operationExcel.ExcelVarles.case_url],
                data=params,
                headers=headers
            )
            # print (r.json())
            case_result_assert(r)
        elif data[operationExcel.ExcelVarles.case_method] == 'post':
            r = method.ApiRequest().send_requests(
                method='post',
                url=data[operationExcel.ExcelVarles.case_url],
                json=json.loads(params),
                headers=headers)
            # writeContent(r.json()['data']['access_tonken'])#提取出返回数据中想要的变量写入到文件中供其他接口使用
            LogsUtil().info(r.json())
            case_result_assert(r)
