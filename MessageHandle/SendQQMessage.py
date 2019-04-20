import queue,CacheHandle,threading,requests
from MessageMoudle import QQBOTCONFIG

now_queue = queue.Queue()

def start():
    while(True):
        if not now_queue.empty():
            message = now_queue.get()
            if 'group_id' in message.keys():
                send_group_message(message)
            else:
                send_private_message(message)

now_threading = threading.Thread(target=start,daemon=True)
now_threading.start()

# 发送私聊
def send_private_message(message):
    url = QQBOTCONFIG.API_ROOT + 'send_private_msg?user_id=' + str(message['user_id']) + '&message=' + message['message']
    requests.post(url)

# 发送群聊
def send_group_message(message):
    url = QQBOTCONFIG.API_ROOT + 'send_group_msg?group_id=' + str(message['group_id']) + '&message=' + message['message']
    requests.post(url)
