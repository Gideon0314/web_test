# -*- coding: UTF-8 -*-
import redis   # 导入redis 模块
from config.config import REDIS_INFO


host = REDIS_INFO.host
port = REDIS_INFO.port
password = REDIS_INFO.password
db = REDIS_INFO.db


def link_redis():
    pool = redis.ConnectionPool(host=host, port=port, password=password, db=db,decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    return r


if __name__ == '__main__':
    r = link_redis()
    # 取出键值
    print(r.get(''))
