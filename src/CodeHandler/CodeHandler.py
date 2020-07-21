import os
import sys
import json
import ast
import mccabe_alter
import PylintScoreCount
from CodeLineCount import LineCounter
from CodeInfo import CodeInfo
from FaceToTestCount import CodeFaceToTestCount
from CommitTimesCounter import CommitTimesCounter

# 最大行数\最大圈复杂度\最小pylint得分\最大提交次数
MAX_LINE_NUM = 100
MAX_CYCLOMATIC_COMPLEXITY = 40
MIN_PYLINT_SCORE = -25
MAX_COMMIT_TIMES = 40


class CodeHandler:
    __CODE_INFO = []
    __MAX_LINE_NUM = 0
    __MAX_CYCLOMATIC_COMPLEXITY = 0
    __MIN_PYLINT_SCORE = 0
    __MAX_COMMIT_TIMES = 0

    def __init__(self, max_line_num, max_cyclomatic_complexity, min_pylint_score, max_commit_times):
        self.__MAX_LINE_NUM = max_line_num
        self.__MAX_CYCLOMATIC_COMPLEXITY = max_cyclomatic_complexity
        self.__MIN_PYLINT_SCORE = min_pylint_score
        self.__MAX_COMMIT_TIMES = max_commit_times

    def list_files(self, path):

        """
        遍历工程路径path，如果遇到文件则统计，如果遇到目录则进行递归
        """

        lineCounter = LineCounter(self.__MAX_LINE_NUM)
        # test_data路径
        commit_times_counter = CommitTimesCounter("D:\\test_data.json")

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
                Pylint_Score = 0
                Commit_Times = 0
                dirnames = os.path.split(path)[1].split('_')
                if self.__checkPY(code_path):
                    FaceToTestHandler = CodeFaceToTestCount(cases_path)
                    LineCount = lineCounter.countLines(code_path)
                    if LineCount != self.__MAX_LINE_NUM:
                        if FaceToTestHandler.isFaceToTest(code_path):
                            LineCount = self.__MAX_LINE_NUM
                    # TODO 圈复杂度统计
                    if LineCount != self.__MAX_LINE_NUM:
                        Cyclomatic_Complexity = mccabe_alter.get_module_complexity(code_path, 0)
                        Pylint_Score = PylintScoreCount.get_pylint_score(code_path)
                        Commit_Times = commit_times_counter.getCommitTimes(dirnames[0], dirnames[1])
                    else:
                        Cyclomatic_Complexity = self.__MAX_CYCLOMATIC_COMPLEXITY
                        Pylint_Score = self.__MIN_PYLINT_SCORE
                        Commit_Times = self.__MAX_COMMIT_TIMES
                else:
                    LineCount = self.__MAX_LINE_NUM
                    Cyclomatic_Complexity = self.__MAX_CYCLOMATIC_COMPLEXITY
                    Pylint_Score = self.__MIN_PYLINT_SCORE
                    Commit_Times = self.__MAX_COMMIT_TIMES
                self.__CODE_INFO.append(
                    CodeInfo(dirnames[0], dirnames[1], LineCount, Cyclomatic_Complexity, Pylint_Score, Commit_Times))
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

    if len(sys.argv) != 3:

        # 命令行按照如下格式输入即可运行程序
        # @param: project_path: 包含代码文件的目录，可以是文件夹或者文件
        # @param: target_path: 输出目标，是一个json文件
        # TODO 将CodeInfo的json文件输出到doc里
        print("Usage :  project_path target_path")
    else:
        project_path = sys.argv[1]
        target_path = sys.argv[2]
        handler = CodeHandler(MAX_LINE_NUM, MAX_CYCLOMATIC_COMPLEXITY, MIN_PYLINT_SCORE, MAX_COMMIT_TIMES)
        handler.list_files(project_path)
        handler.printResult(target_path)
