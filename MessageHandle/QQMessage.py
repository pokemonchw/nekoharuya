import queue,threading,CacheHandle
now_queue = queue.Queue()

# 处理qq消息队列
def start():
    while(True):
        if not now_queue.empty():
            message = now_queue.get()
            eval(message['message_type'] + '_message')(message)

# 处理私聊
def private_message(message):
    user_data = message['sender']
    set_user_data(user_data)
    now_message = message['message']
    eval('privete_' + message['sub_type'] + '_message')(message)

# 处理非好友私聊
def private_group_message(message):
    pass

# 处理好友私聊
def private_friend_message(message):
    pass

# 处理群组消息
def group_message(message):
    group_id = message['group_id']
    now_message = message['message']
    set_user_data(message['sender'])

# 初始化用户数据
def set_user_data(user_data):
    if user_data['user_id'] not in CacheHandle.user_data['qq']:
        new_user = {str(user_data['user_id']):{
            "user_sex":user_data['sex'],
            "user_age":str(user_data['age']),
            "nick_name":user_data['nickname']
        }}
        CacheHandle.user_data['qq'].update(new_user)

now_threading = threading.Thread(target=start,daemon=True)
now_threading.start()
