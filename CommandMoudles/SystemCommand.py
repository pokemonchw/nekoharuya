import Command,CacheHandle

command_help_auxiliary = ['h']
@Command.command_listener(command_cn='帮助',command_en='help',command_en_short='h',descript='查询帮助菜单',auxiliary_command=command_help_auxiliary)
def command_help(message,auxiliary):
    reply_text = "心智模型003号为您服务\n欢迎查询帮助菜单\n当前可用查询为:None"
    reply_data = {
        '':"心智模型003号为您服务\n欢迎查询帮助菜单\n当前可用查询为:None",
        "h":"心智模型003号为您服务\n欢迎查询帮助菜单\n目前没有可选的帮助项"
    }
    reply_text = reply_data[auxiliary]
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
