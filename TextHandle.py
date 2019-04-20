from lib import langconv

# 全角转为半角
def full_to_half(ustring):
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 0x3000:
            inside_code = 0x0020
        else:
            inside_code -= 0xfee0
        if not (0x0021 <= inside_code and inside_code <= 0x7e):
            rstring += uchar
            continue
        rstring += chr(inside_code)
    return rstring

# 半角转为全角
def half_to_full(ustring):
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 0x0020:
            inside_code = 0x3000
        else:
            if not (0x0021 <= inside_code and inside_code <= 0x7e):
                rstring += uchar
                continue
        inside_code += 0xfee0
        rstring += chr(inside_code)
    return rstring

# 繁体转为简体
def traditional_to_simplified(text):
    text = langconv.Converter('zh-hans').convert(text)
    return text

# 简体转为繁体
def simlified_to_traditional(text):
    text = langconv.Converter('zh-hant').convert(text)
    return text

# 判断字符串使用的是繁体还是简体
def judge_chinese_type(text):
    new_text = simlified_to_traditional(text)
    if new_text == text:
        return 'traditional'
    return 'simlified'
