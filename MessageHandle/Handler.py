import queue,CacheHandle,threading,Config,Command

now_queue = queue.Queue()

def start():
    while(True):
        if not now_queue.empty():
            message = now_queue.get()
            message = command_handle(message)
            if message != 'command':
                print()

now_threading = threading.Thread(target=start,daemon=True)
now_threading.start()

# 处理并执行命令消息
def command_handle(message):
    text = message['data']['message'].strip()
    if text.startswith(Config.command_switch):
        text = text.lstrip(Config.command_switch)
        for command in CacheHandle.command_list:
            command_judge_bool = command_judge(command,text)
            if command_judge_bool[0]:
                command.func(message,command_judge_bool[1])
                return 'command'
    return message

# 判断是否含有当前命令
def command_judge(command,text):
    auxiliary = ''
    if (len(command.command_cn) and len(command.command_en) and len(command.command_en_short)) > len(text):
        return [False]
    if command.accurate:
        if text not in [command.command_cn,command.command_en,command.command_en_short]:
            auxiliary = Command.get_auxiliary_command(command,text)
            if auxiliary == '':
                return [False]
    if text.startswith(command.command_cn) or text.startswith(command.command_en) or text.startswith(command.command_en_short):
        return [True,auxiliary]
    return [False]
