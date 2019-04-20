import Command,CacheHandle

@Command.command_listener('帮助','help','help','查询帮助菜单')
def command_help(message):
    reply_text = "心智模型003号为您服务\n欢迎查询帮助菜单\n当前可用查询为:None"
    reply_data = {
        "message_source":message['message_source'],
        "message_type":'reply',
        "data":{
            "message_active_region":message['data']['message_type'],
            "user_id":message['data']['user_id'],
            "message":reply_text
        }
    }
    if 'group_id' in message['data'].keys():
        reply_data['data']['group_id'] = message['data']['group_id']
    CacheHandle.now_queue.put(reply_data)
