import queue,CacheHandle,threading

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
    text = message['data']['message']
    print(CacheHandle.command_list)
    for command in CacheHandle.command_list:
        if text.find(command.command_cn) > -1 or text.find(command.command_en) > -1 or text.find(command.command_en_short) > -1:
            command.func(message)
            return 'command'
    return message
