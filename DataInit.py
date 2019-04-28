import time,CacheHandle,BotIo
from DataPath import *

cache_pool = [CacheHandle.user_data,CacheHandle.white_list]
path_pool = [user_data_path,white_list_path]
# 初始化数据
def init():
    for i in range(0,len(cache_pool)):
        now_data = read_data(path_pool[i])
        if now_data != 'Null':
            cache_pool[i].update(now_data)

# 读取数据
def read_data(now_path):
    try:
        return BotIo.load_json(now_path)
    except:
        return 'Null'
