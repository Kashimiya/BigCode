'''
代码原址https://www.cnblogs.com/laizhenghong2012/p/11348004.html
将控制台输出保存到文件https://www.cnblogs.com/pfeiliu/p/12723589.html
'''

import os
import sys


# 后缀集合
CPP_SUFFIX_SET = {'.h', '.hpp', '.hxx', '.c', '.cpp', '.cc', '.cxx'}
PYTHON_SUFFIX_SET = {'.py'}
JAVA_SUFFIX_SET = {'.java'}

# 全局变量
MAX_LINE_NUM = 114514


def list_files(path):
    '''
    遍历工程路径path，如果遇到文件则统计其行数，如果遇到目录则进行递归
    '''
    filenames = os.listdir(path)
    for f in filenames:
        fpath = os.path.join(path, f)
        if (os.path.isfile(fpath)):
            count_lines(fpath)
        if (os.path.isdir(fpath)):
            list_files(fpath)


def count_lines(fpath):
    '''
    对于文件fpath，计算它的行数，然后根据其后缀将它的行数加到相应的全局变量当中
    '''
    global CPP_SUFFIX_SET, PYTHON_SUFFIX_SET, JAVA_SUFFIX_SET
    global MAX_LINE_NUM

    # 统计行数
    suffix = os.path.splitext(fpath)[-1]
    LineCount = 0
    if suffix in CPP_SUFFIX_SET or suffix in JAVA_SUFFIX_SET:
        LineCount = MAX_LINE_NUM
    else:
        with open(fpath, 'rb') as f:
            last_data = '\n'
            while True:
                data = f.read(0x400000)
                if not data:
                    break
                LineCount += data.count(b'\n')
                last_data = data
            if last_data[-1:] != b'\n':
                LineCount += 1
    print("{")
    print("FilePath : "+fpath + ",")
    print("LineCount : ")
    print(LineCount)
    print(",")
    print("}")

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print("Usage : python3 code_analyst.py project_path")
    else:
        project_path = sys.argv[1]
        list_files(project_path)