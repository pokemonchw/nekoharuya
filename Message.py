import CacheHandle,json,TextHandle
import MessageHandle.Handler
import ReplyHandle.Handler
import WarningHandle.Handler

route_data = {
    "normal":MessageHandle.Handler,
    "reply":ReplyHandle.Handler,
    "warning":WarningHandle.Handler
}

# 消息处理
def init():
    while(True):
        if not CacheHandle.now_queue.empty():
            message = CacheHandle.now_queue.get()
            if 'message' in message['data']:
                message_text = message['data']['message']
                message_chinese_type = TextHandle.judge_chinese_type(message_text)
                message.update({"chinese_type":message_chinese_type})
                if message_chinese_type == 'traditional':
                    message_text = TextHandle.traditional_to_simplified(message_text)
                message_text = TextHandle.full_to_half(message_text)
                message['data']['message'] = message_text
            route_data[message['message_type']].now_queue.put(message)
