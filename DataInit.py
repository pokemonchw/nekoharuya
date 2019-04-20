import time,CacheHandle,BotIo
from DataPath import *

# 初始化数据
def init():
    cache_pool = [CacheHandle.user_data,CacheHandle.white_list]
    path_pool = [user_data_path,white_list_path]
    now_cache = iter(cache_pool)
    now_path = iter(path_pool)
    for cache in now_cache:
        now_data = read_data(next(now_path))
        if now_data != 'Null':
            cache = now_data

# 读取数据
def read_data(now_path):
    try:
        now_data = BotIo.load_json(now_path)
    except:
        return 'Null'
