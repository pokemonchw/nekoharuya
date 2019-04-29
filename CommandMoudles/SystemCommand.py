import Command,CacheHandle

command_help_auxiliary = ['h']
help_reply_data = {
    '':"心智模型003号为您服务\n欢迎查询帮助菜单\n当前可用查询为:None",
    "h":"心智模型003号为您服务\n欢迎查询帮助菜单\n目前没有可选的帮助项"
}
@Command.command_listener(command_cn='帮助',command_en='help',command_en_short='h',descript='查询帮助菜单',auxiliary_command=command_help_auxiliary)
def command_help(message,auxiliary):
    reply_text = help_reply_data[auxiliary]
    reply_data = Command.message_data_to_reply_data(message)
    reply_data['data'].update({"message":reply_text})
    Command.cd_handler('help',reply_data,600,6000,message,3)
    CacheHandle.now_queue.put(reply_data)

command_list_auxiliary = ['a','s']
list_reply_data = {
    '':CacheHandle.command_list_info,
    'a':CacheHandle.command_list_all_info,
    's':CacheHandle.command_list_short_info
}
@Command.command_listener(command_cn='命令列表',command_en='list',command_en_short='l',descript='查看命令列表',auxiliary_command=command_list_auxiliary)
def command_list(message,auxiliary):
    reply_text = list_reply_data[auxiliary]
    reply_text = "当前命令列表为:\n" + reply_text + 'Over'
    reply_data = Command.message_data_to_reply_data(message)
    reply_data['data'].update({"message":reply_text})
    Command.cd_handler('list',reply_data,600,6000,message,3)
    CacheHandle.now_queue.put(reply_data)

list_reply_data = {
    '':CacheHandle.command_list_info,
    'a':CacheHandle.command_list_all_info,
    's':CacheHandle.command_list_short_info
}
