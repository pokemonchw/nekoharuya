from MessageMoudle.QQBOTCONFIG import *
from lib import cqhttp
import requests,threading,CacheHandle,json
qq_bot = cqhttp.CQHttp(api_root=API_ROOT)

# 获取qq消息
@qq_bot.on_message()
def handle_message(context):
    qq_message = {
        "message_source":"qq",
        "message_type":"normal",
        "data":context
    }
    CacheHandle.now_queue.put(qq_message)

CacheHandle.qq_bot = qq_bot
qq_bot_server = threading.Thread(target=qq_bot.run,kwargs=dict(host=HOST,port=PORT),daemon=True)
qq_bot_server.start()

