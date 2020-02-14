import requests
import api
from get_log import GetLog

log = GetLog.get_logger()


class ApiEmployee():
    # 1初始化
    def __init__(self):
        # 新增url
        self.post_url = api.host + "/api/sys/user"
        # 修改url
        self.put_url = api.host + "/api/sys/user/{}"
        # 查询url
        self.get_url = api.host + "/api/sys/user/{}"
        # 删除url
        self.delete_url = api.host + "/api/sys/user/{}"
        # 日记
        log.info("新增员工url:{}".format(self.post_url))
        log.info("删除,更新,修改url:{}".format(self.delete_url))

    # 2新增员工-接口封装
    def api_post_employee(self, username, mobile, workNumber):
        # 请求参数
        data = {"username": username,
                "mobile": mobile,
                "workNumber": workNumber}
        log.info("新增员工数据:{}新增员工请求信息头:{}".format(data, api.headers))

        # 调用post方法>返回响应对象 ---json接受参数
        response = requests.post(url=self.post_url, json=data, headers=api.headers)
        log.info("xxxxx:{}".format(response.json()))
        return response

    # 3修改员工-接口封装
    def api_put_employee(self):
        # 请求参数
        data = {"username": "bibao-01", }
        # 调用put方法>返回响应对象
        return requests.put(url=self.put_url.format(api.user_id), json=data, headers=api.headers)

    # 4查询员工-接口封装
    def api_get_employee(self):
        # 调用get方法>返回响应对象=====当前headers中存在Content-Type不过没有请求体不影响使用
        return requests.get(url=self.get_url.format(api.user_id), headers=api.headers)

    # 5删除员工-接口封装
    def api_delete_employee(self):
        log.info("删除员工信息头提示:{}".format(api.headers))
        # 调用delete方法>返回响应对象
        return requests.delete(url=self.delete_url.format(api.user_id), headers=api.headers)
