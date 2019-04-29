import queue,sys
from lib import cqhttp
from Command import Command
now_queue = queue.Queue()
qq_bot = cqhttp.CQHttp()
user_data = {'qq':{},'qq_group':{}}
white_list = {'qq':{},'qq_group':{}}
command_list = []
command_list_info = ''
command_list_all_info = ''
command_list_short_info = ''
