from get_log import GetLog

log = GetLog.get_logger()


def asser_common(self, response,
                 status_code=200,
                 success=True,
                 code=10000,
                 message="操作成功！"):  # self为TestCase实例
    # response为:响应对象
    try:
        r = response.json()
        # 断言
        # 断言状态码 200
        self.assertEqual(status_code, response.status_code)
        # 断言success True
        self.assertEqual(success, r.get("success"))
        # 断言code 10000
        self.assertEqual(code, r.get("code"))
        # 断言message 操作成功！
        self.assertEqual(message, r.get("message"))
    except Exception as e:
        log.error(e)
        # 抛异常
        raise
