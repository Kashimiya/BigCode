"""
原代码地址https://www.cnblogs.com/laizhenghong2012/p/11348004.html
"""

import os


class LineCounter:
    # 后缀集合
    # __CPP_SUFFIX_SET = {'.h', '.hpp', '.hxx', '.c', '.cpp', '.cc', '.cxx'}
    # __PYTHON_SUFFIX_SET = {'.py'}
    # __JAVA_SUFFIX_SET = {'.java'}

    # 最大行数
    __MAX_LINE_NUM = 0

    def __init__(self, maxLineNum):
        self.__MAX_LINE_NUM = maxLineNum

    def countLines(self, FilePath):

        # suffix = os.path.splitext(FilePath)[-1]
        LineCount = 0

        # if suffix in self.__CPP_SUFFIX_SET or suffix in self.__JAVA_SUFFIX_SET:
        #     LineCount = self.__MAX_LINE_NUM
        # else:
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
