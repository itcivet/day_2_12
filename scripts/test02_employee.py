import unittest

from parameterized import parameterized

import api
from api.api_employee import ApiEmployee
from get_log import GetLog
from tool.assert_common import asser_common

from tool.read_yaml import read_yaml

log = GetLog.get_logger()


class TestEmployee(unittest.TestCase):
    """1.初始化方法"""

    @classmethod
    def setUpClass(cls) -> None:
        """获取apiempolyee对象"""
        cls.api = ApiEmployee()

    # 2新增员工
    @parameterized.expand(read_yaml("employee_post.yaml"))
    def test01_post(self, username, mobile, workNumber):
        # 调用新增员工接口
        r = self.api.api_post_employee(username, mobile, workNumber)
        # 断言
        asser_common(self, r)
        print("新增员工结果:", r.json())
        log.info("新增员工结果:{}".format(r.json()))
        # 提取user_id
        api.user_id = r.json().get("data").get("id")
        print("员工user_id为", api.user_id)
        log.info("新增员工后提取的员工id为:{}".format(api.user_id))

    # 3修改员工测试方法
    def test02_put(self):
        """调用更新接口"""
        r = self.api.api_put_employee()
        log.info("更新员工结果为:{}".format(r.json()))
        # 断言
        asser_common(self, r)

    # 4查询员工测试方法
    def test03_get(self):
        """调用查询接口"""
        r = self.api.api_get_employee()
        log.info("查询员工结果为:{}".format(r.json()))
        # 断言
        asser_common(self, r)

    # 5删除员工测试方法
    def test04_delete(self):
        # 调用删除员工接口
        r = self.api.api_delete_employee()
        print("删除结果", r.json())
        # 断言
        asser_common(self, r)
