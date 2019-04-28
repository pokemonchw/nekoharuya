import queue,CacheHandle,threading

now_queue = queue.Queue()


def start():
    while(True):
        if not now_queue.empty():
            now_data = now_queue.get()
            eval(now_data['data']['warning_type'] + '_warning')(now_data)

command_cd_warning_text_data = {
    "private":"您在段时间内已使用过本命令,请勿频繁操作",
    "group":"群内已有人在段时间内使用过本命令,请勿频繁操作"
}
def command_cd_warning(message):
    message['message_type'] = 'reply'
    message['data']['message'] = command_cd_warning_text_data[message['data']['message_active_region']]
    CacheHandle.now_queue.put(message)

now_threading = threading.Thread(target=start,daemon=True)
now_threading.start()
