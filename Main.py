#!/usr/bin/python3
import Message,threading,MessageGet,DataHandle,DataInit

thread_pool = []
moudle_data = {
    "message":Message.init,
    "dataHandle":DataHandle.init
}

# 初始化系统进程
def init():
    DataInit.init()
    threading_id_list = list(moudle_data.keys())
    import CommandMoudles
    index = 0
    while(True):
        for i in range(0,len(threading_id_list)):
            if threading_id_list[i] not in thread_pool:
                thread_pool.append(threading_id_list[i])
                threading_name = threading_id_list[i] + str(index)
                index += 1
                now_threading = threading.Thread(target=now_run,args=(threading_id_list[i],),name=threading_name,daemon=True)
                now_threading.start()

# 进程启动
def now_run(threading_id):
    print('now ' + threading_id + ' start')
    moudle_data[threading_id]()
    thread_pool.remove(threading_id)

init()
