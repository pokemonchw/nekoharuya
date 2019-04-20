import queue,sys
from lib import cqhttp
from Command import Command
now_queue = queue.Queue()
qq_bot = cqhttp.CQHttp()
user_data = {'qq':{},'qq_group':{}}
white_list = {'qq':{},'qq_group':{}}
command_list = []

# 添加命令进命令列表
def append_command(command:Command):
    global command_list
    command_list.append(command)

# 创建命令模组
def create_variavle(name,var):
    this_module = sys.modules[__name__]
    setattr(this_module,name,var)
