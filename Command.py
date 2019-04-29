from functools import wraps
import CacheHandle,Config,time,sys

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
        append_command(Command(command_cn,command_en,command_en_short,descript,accurate,auxiliary_command,return_wrapper))
        create_variavle(func.__name__,return_wrapper)
        return return_wrapper
    return decorator

# 添加命令进命令列表
def append_command(command:Command):
    CacheHandle.command_list.append(command)
    auxiliary_info = '辅助命令:'
    for i in command.auxiliary_command:
        auxiliary_info += ' ' + i
    CacheHandle.command_list_all_info += "命令:" + command.command_cn + ' en:' + command.command_en + ' short:' + command.command_en_short + '\n  描述:\n    ' + command.descript + '\n  ' + auxiliary_info + '\n'
    CacheHandle.command_list_short_info += "命令" + command.command_cn + ' en:' + command.command_en + ' short:' + command.command_en_short + '\n'
    CacheHandle.command_list_info += "命令:" + command.command_cn + ' en:' + command.command_en + ' short:' + command.command_en_short + '\n  描述:\n    ' + command.descript + '\n'

# 创建命令模组
def create_variavle(name,var):
    this_module = sys.modules[__name__]
    setattr(this_module,name,var)

# 获取当前辅助命令
def get_auxiliary_command(command,text):
    auxiliary = text
    while(auxiliary.startswith(command.command_cn)):
        auxiliary = text.lstrip(command.command_cn)
        break
    while(auxiliary.startswith(command.command_en)):
        auxiliary = text.lstrip(command.command_en)
        break
    while(auxiliary.startswith(command.command_en_short)):
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

# 处理命令的cd
def cd_handler(command_id,reply_data,now_cd,qq_group_cd,message,max_index=0):
    cd_user = reply_data['data']["user_id"]
    if message['message_source'] == 'qq_group':
        reply_data['data'].update({"group_id":message["data"]["group_id"]})
        cd_user = reply_data['data']['group_id']
        now_cd = qq_group_cd
    if judge_command_cd(message['message_source'],cd_user,command_id,now_cd):
        cd_data = get_cd_starttime_data(command_id)
        cd_data['cd'][command_id].update({"cd_index":1})
        CacheHandle.user_data[message['message_source']].update({cd_user:cd_data})
    else:
        if CacheHandle.user_data[message['message_source']][cd_user]['cd'][command_id]['cd_index'] >= max_index:
            reply_data["message_type"] = "warning"
            reply_data['data'].update({"warning_type":"command_cd"})
        else:
            CacheHandle.user_data[message['message_source']][cd_user]['cd'][command_id]['cd_index'] += 1

# 获取命令cd开始时间数据
def get_cd_starttime_data(command_id):
    now_time = time.time()
    return {
        "cd":{
            command_id:{
                "start_time":now_time
            }
        }
    }

# 将接收消息转换为回复消息结构体
def message_data_to_reply_data(message):
    return {
        "message_source":message['message_source'],
        "message_type":'reply',
        "data":{
            "message_active_region":message['data']['message_type'],
            "user_id":message['data']['user_id'],
        }
    }
