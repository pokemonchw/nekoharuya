import Command,CacheHandle,datetime

command_help_auxiliary = ['h']

help_reply_data = {
    '':"心智模型003号为您服务\n欢迎查询帮助菜单\n当前可用查询为:None",
    "h":"心智模型003号为您服务\n欢迎查询帮助菜单\n目前没有可选的帮助项"
}
@Command.command_listener(command_cn='帮助',command_en='help',command_en_short='h',descript='查询帮助菜单',auxiliary_command=command_help_auxiliary)
def command_help(message,auxiliary):
    reply_text = "心智模型003号为您服务\n欢迎查询帮助菜单\n当前可用查询为:None"
    reply_text = help_reply_data[auxiliary]
    reply_data = {
        "message_source":message['message_source'],
        "message_type":'reply',
        "data":{
            "message_active_region":message['data']['message_type'],
            "user_id":message['data']['user_id'],
            "message":reply_text
        }
    }
    now_cd = 600
    cd_user = reply_data['data']["user_id"]
    if message['message_source'] == 'qq_group':
        reply_data['data'].update({"group_id":message["data"]["group_id"]})
        cd_user = reply_data['data']['group_id']
        now_cd = 6000
    if Command.judge_command_cd(message['message_source'],cd_user,'help',now_cd):
        now_time = datetime.datetime.now()
        cd_data = {
            "cd":{
                "help":{
                    "start_time":now_time
                }
            }
        }
        CacheHandle.user_data[message['message_source']].update({cd_user:cd_data})
    else:
        reply_data = {
            "message_source":message['message_source'],
            "message_type":'warning',
            "data":{
                "warning_type":"command_cd",
                "message_active_region":message['data']['message_type'],
                "user_id":message['data']['user_id'],
            }
        }
    CacheHandle.now_queue.put(reply_data)
