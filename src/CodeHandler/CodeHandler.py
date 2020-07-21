"""
将控制台输出保存到文件https://www.cnblogs.com/pfeiliu/p/12723589.html
"""

import os
import sys
import json
import ast
from CodeLineCount import LineCounter
from CodeInfo import CodeInfo
from FaceToTestCount import CodeFaceToTestCount
import mccabe_alter
import pylint

# 最大行数和最大圈复杂度
MAX_LINE_NUM = 200
MAX_CYCLOMATIC_COMPLEXITY = 50


class CodeHandler:
    __CODE_INFO = []
    __MAX_LINE_NUM = 0
    __MAX_CYCLOMATIC_COMPLEXITY = 0

    def __init__(self, max_line_num, max_cyclomatic_complexity):
        self.__MAX_LINE_NUM = max_line_num
        self.__MAX_CYCLOMATIC_COMPLEXITY = max_cyclomatic_complexity

    def list_files(self, path):

        """
        遍历工程路径path，如果遇到文件则统计，如果遇到目录则进行递归
        """

        lineCounter = LineCounter(self.__MAX_LINE_NUM)

        filenames = os.listdir(path)
        for f in filenames:
            fpath = os.path.join(path, f)
            if f == '.mooctest':
                cases_path = ''
                code_path = ''
                files = os.listdir(fpath)
                for file in files:
                    if file != 'testCases.json':
                        code_path = os.path.join(fpath, file)
                    else:
                        cases_path = os.path.join(fpath, 'testCases.json')
                LineCount = 0
                Cyclomatic_Complexity = 0
                if self.__checkPY(code_path):
                    FaceToTestHandler = CodeFaceToTestCount(cases_path)
                    LineCount = lineCounter.countLines(code_path)
                    if LineCount != self.__MAX_LINE_NUM:
                        if FaceToTestHandler.isFaceToTest(code_path):
                            LineCount = self.__MAX_LINE_NUM
                    # TODO 圈复杂度统计
                    if LineCount != self.__MAX_LINE_NUM:
                        Cyclomatic_Complexity = mccabe_alter.get_module_complexity(code_path,0)
                    else:
                        Cyclomatic_Complexity = self.__MAX_CYCLOMATIC_COMPLEXITY
                else:
                    LineCount = self.__MAX_LINE_NUM
                    Cyclomatic_Complexity = self.__MAX_CYCLOMATIC_COMPLEXITY

                self.__CODE_INFO.append(CodeInfo(code_path, LineCount, Cyclomatic_Complexity))
            elif os.path.isdir(fpath):
                self.list_files(fpath)

    def __checkPY(self, path):
        with open(path, encoding='UTF-8') as mod:
            code = mod.read()
            try:
                tree = compile(code, path, "exec", ast.PyCF_ONLY_AST)
            except SyntaxError:
                return False
        return True

    def printResult(self, targetPath):

        file = open(targetPath, 'w')

        for code in self.__CODE_INFO:
            file.write(json.dumps(code.__dict__))
            file.write(",\n")

        file.close()


if __name__ == '__main__':

    # global MAX_LINE_NUM

    if len(sys.argv) != 3:

        # 命令行按照如下格式输入即可运行程序
        # @param: project_path: 包含代码文件的目录，可以是文件夹或者文件
        # @param: target_path: 输出目标，是一个json文件
        # TODO 将CodeInfo的json文件输出到doc里
        print("Usage :  project_path target_path")
    else:
        project_path = sys.argv[1]
        target_path = sys.argv[2]
        handler = CodeHandler(MAX_LINE_NUM, MAX_CYCLOMATIC_COMPLEXITY)
        handler.list_files(project_path)
        handler.printResult(target_path)
