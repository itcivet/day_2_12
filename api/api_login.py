import requests
import api
from get_log import GetLog

# 获取日记

log = GetLog.get_logger()


class ApiLogin:
    # 1初始化
    def __init__(self):
        # 组装登陆url
        self.login_url = api.host + "/api/sys/login"
        # 日记
        log.info("正在初始化登陆url:{}".format(self.login_url))

    # 2.登陆接口封装
    def api_login(self, mobile, password):
        # 1定义测试数据
        data = {"mobile": mobile, "password": password}
        # 日记
        log.info("正在初始化登陆数据:{}请求信息头:{}".format(data, api.headers))
        # 2调用post方法 后将响应数据返回
        return requests.post(url=self.login_url, json=data, headers=api.headers)
