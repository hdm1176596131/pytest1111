import requests
import json

"""get请求"""
def get(url, data=None, headers=None):
    if headers is not None:
        res = requests.get(url=url, data=data, headers=headers)
    else:
        res = requests.get(url=url)
    return res.json()

"""POST请求"""
def post(url, data, headers):
    if headers is not None:
        res = requests.post(url=url, data=data, headers=headers)
    else:
        res = requests.post(url=url, data=data)
    if str(res) == "<Response [200]>":
        return res.json()
    else:
        return res.text


class ApiRequest(object):

    def __init__(self):
        self.r = None

    # -----第一种请求方式封装request库，调用可根据实际情况传参
    def send_requests(self, method, url, data=None, params=None, headers=None, cookies=None, json=None, files=None,
                      timeout=None):
        self.r = requests.request(method, url, data=data, params=params, headers=headers, cookies=cookies, json=json,
                                  files=files, timeout=timeout)
        return self.r

    """主方法"""
    @staticmethod
    def all_method(method, url, data=None, headers=None):
        if method == 'get' or method == 'GET':
            res = get(url, data, headers)
        elif method == 'post' or method == 'POST':
            res = post(url, data, headers)
        else:
            res = '请求方式不正确'
        return json.dump(res, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ':'))
