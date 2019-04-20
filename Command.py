from functools import wraps
import CacheHandle

# 构造命令对象
class Command:
    def __init__(self,command_cn:str,command_en:str,command_en_short:str,descript:str,func:callable):
        self.command_cn = command_cn
        self.command_en = command_en
        self.command_en_short = command_en_short
        self.descript = descript
        self.func = func

# 生成命令对象
def command_listener(command_cn:str,command_en:str,command_en_short:str,descript:str):
    def decorator(func):
        @wraps(func)
        def return_wrapper(*args,**kwargs):
            return func(*args,**kwargs)
        CacheHandle.append_command(Command(command_cn,command_en,command_en_short,descript,return_wrapper))
        CacheHandle.create_variavle(func.__name__,return_wrapper)
        return return_wrapper
    return decorator

