import queue,CacheHandle,threading

now_queue = queue.Queue()

def start():
    pass

now_threading = threading.Thread(target=start,daemon=True)
now_threading.start()
