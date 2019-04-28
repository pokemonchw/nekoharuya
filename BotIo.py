import json,pickle

# 判断文件编码是否为utf-8
def is_utf8bom(file_path):
    if b'\xef\xbb\xbf' == open(file_path,mode='rb').read(3):
        return True
    return False

# 载入json文件
def load_json(file_path):
    if is_utf8bom(file_path):
        ec='utf-8-sig'
    else:
        ec='utf-8'
    with open(file_path,'r',encoding=ec) as f:
        try:
            json_data = json.loads(f.read())
        except json.decoder.JSONDecodeError:
            print(file_path + '无效的json文件')
            json_data = []
    return json_data

# 保存数据到json
def save_json(file_path,data):
    print(data)
    data_string = json.dumps(data)
    data_file = open(file_path,'w',encoding='utf-8')
    data_file.write(data_string)
    data_file.close()

