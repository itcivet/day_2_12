import os
import yaml
from config import base_url


def read_yaml(file):
    #1.获取数据文件流
    with open(base_url + os.sep + "data" + os.sep + file, "r", encoding="utf-8")as  f:
        a = []
        #调用方法解析文件流
        for data in yaml.safe_load(f).values():
            a.append(tuple(data.values()))
            return a


if __name__ == '__main__':
    print(read_yaml("login.yaml"))
    # print(base_url)
    # print(base_url + os.sep + "data" + os.sep + "login.yaml")
