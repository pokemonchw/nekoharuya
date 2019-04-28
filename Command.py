from functools import wraps
import CacheHandle,Config,time

# 构造命令对象
class Command:
    def __init__(self,command_cn:str,command_en:str,command_en_short:str,descript:str,accurate:bool,auxiliary_command:list,func:callable):
        self.command_cn = command_cn
        self.command_en = command_en
        self.command_en_short = command_en_short
        self.descript = descript
        self.func = func
        self.accurate = accurate
        self.auxiliary_command = auxiliary_command

# 生成命令对象
def command_listener(command_cn:str,command_en:str,command_en_short:str,descript:str,accurate:bool=True,auxiliary_command=[]):
    def decorator(func):
        @wraps(func)
        def return_wrapper(*args,**kwargs):
            return func(*args,**kwargs)
        CacheHandle.append_command(Command(command_cn,command_en,command_en_short,descript,accurate,auxiliary_command,return_wrapper))
        CacheHandle.create_variavle(func.__name__,return_wrapper)
        return return_wrapper
    return decorator

# 获取当前辅助命令
def get_auxiliary_command(command,text):
    auxiliary = ''
    while(text.startswith(command.command_cn)):
        auxiliary = text.lstrip(command.command_cn)
        break
    while(text.startswith(command.command_en)):
        auxiliary = text.lstrip(command.command_en)
        break
    while(text.startswith(command.command_en_short)):
        auxiliary = text.lstrip(command.command_en_short)
        break
    if auxiliary.startswith(Config.auxiliary_command_switch):
        auxiliary = auxiliary.lstrip(Config.auxiliary_command_switch)
    if auxiliary in command.auxiliary_command:
        return auxiliary
    return ''

# 判断指令是否在cd时间内
def judge_command_cd(user_type,user_id,command_id,command_cd):
    if user_id in CacheHandle.user_data[user_type]:
        if 'cd' in CacheHandle.user_data[user_type][user_id]:
            if command_id in CacheHandle.user_data[user_type][user_id]['cd']:
                cd_start_time = CacheHandle.user_data[user_type][user_id]['cd'][command_id]['start_time']
                now_time = time.time()
                if now_time - cd_start_time < command_cd:
                    return False
    return True
