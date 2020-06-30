'''
原代码地址https://www.cnblogs.com/laizhenghong2012/p/11348004.html
'''

import os

# 后缀集合
CPP_SUFFIX_SET = {'.h', '.hpp', '.hxx', '.c', '.cpp', '.cc', '.cxx'}
PYTHON_SUFFIX_SET = {'.py'}
JAVA_SUFFIX_SET = {'.java'}

# 全局变量
MAX_LINE_NUM = 114514

def count_lines(FilePath):

    global CPP_SUFFIX_SET, PYTHON_SUFFIX_SET, JAVA_SUFFIX_SET
    global MAX_LINE_NUM

    # 统计行数
    suffix = os.path.splitext(FilePath)[-1]
    LineCount = 0
    if suffix in CPP_SUFFIX_SET or suffix in JAVA_SUFFIX_SET:
        LineCount = MAX_LINE_NUM
    else:
        with open(FilePath, 'rb') as f:
            last_data = '\n'
            while True:
                data = f.read(0x400000)
                if not data:
                    break
                LineCount += data.count(b'\n')
                last_data = data
            if last_data[-1:] != b'\n':
                LineCount += 1

    return LineCount