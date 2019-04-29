import queue,CacheHandle,threading
import MessageHandle.SendQQMessage

now_queue = queue.Queue()

send_data = {
    'qq':MessageHandle.SendQQMessage,
    'qq_group':MessageHandle.SendQQMessage
}

def start():
    while(True):
        if not now_queue.empty():
            message = now_queue.get()
            send_data[message['message_source']].now_queue.put(message['data'])

now_threading = threading.Thread(target=start,daemon=True)
now_threading.start()
