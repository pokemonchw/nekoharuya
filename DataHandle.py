import time,CacheHandle,BotIo
from DataPath import *

# 保存用户数据
def init():
    time.sleep(30)
    BotIo.save_json(white_list_path,CacheHandle.user_data)
    BotIo.save_json(user_data_path,CacheHandle.user_data)

