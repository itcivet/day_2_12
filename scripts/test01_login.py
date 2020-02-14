# 1导包
import unittest
from parameterized import parameterized
from api.api_login import ApiLogin
import api
from get_log import GetLog
from tool.assert_common import asser_common
from tool.read_yaml import read_yaml
# 2定义测试类 继承unittest.TestCase


# 日记


log = GetLog.get_logger()


class TestLogin(unittest.TestCase):
    # 1 初始化
    def setUp(self) -> None:
        # 获取apilogin对象
        self.login = ApiLogin()

    # 2登陆测试方法
    @parameterized.expand(read_yaml("login.yaml"))
    def test_login(self, mobile, password):
        # 调用登陆接口
        result = self.login.api_login(mobile, password)
        print("登陆结果:", result.json())
        r = result.json()
        # 断言
        asser_common(self, result)
        # # 断言
        # # 断言状态码 200
        # self.assertEqual(200, result.status_code)
        # # 断言success True
        # self.assertEqual(True, r.get("success"))
        # # 断言code 10000
        # self.assertEqual(10000, r.get("code"))
        # # 断言message 操作成功！
        # self.assertEqual("操作成功！", r.get('message'))
        # 提取token
        token = r.get("data")
        log.info("正在提取token:{}".format(token))
        # 追加到公共变量 headers
        api.headers["Authorization"] = "Bearer " + token
        print("追加后的headers为:", api.headers)
