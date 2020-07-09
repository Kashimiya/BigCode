'''
将控制台输出保存到文件https://www.cnblogs.com/pfeiliu/p/12723589.html
'''

import os
import sys
from CodeLineCount import LineCounter
from CodeInfo import CodeInfo
from FaceToTestCount import CodeFaceToTestCount

CODE_INFO = []
MAX_LINE_NUM = 114514


def list_files(path):

    '''
    遍历工程路径path，如果遇到文件则统计，如果遇到目录则进行递归
    圈复杂度待实现
    '''

    global CODE_INFO
    global MAX_LINE_NUM

    FaceToTestHandler = CodeFaceToTestCount(path+'/test_data.json')
    lineCounter = LineCounter(MAX_LINE_NUM)

    filenames = os.listdir(path)
    for f in filenames:
        fpath = os.path.join(path, f)
        if (os.path.isfile(fpath)):
            LineCount = lineCounter.countLines(fpath)
            if LineCount != MAX_LINE_NUM:
                if FaceToTestHandler.isFaceToTest(fpath):
                    LineCount = MAX_LINE_NUM
            Cyclomatic_Complexity = 0  # 待填写
            CODE_INFO.append(CodeInfo(fpath, LineCount, Cyclomatic_Complexity))
        if (os.path.isdir(fpath)):
            list_files(fpath)


def printResult():

    global CODE_INFO

    for code in CODE_INFO:
        code.printCodeInfo()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        # 命令行按照如下格式输入即可运行程序
        print("Usage : python3 CodeHandler.py project_path")
    else:
        project_path = sys.argv[1]
        list_files(project_path)
