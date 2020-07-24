import os
import json
import ast
import mccabe_alter
from CodeLineCount import LineCounter
from CodeInfo import CodeInfo
from FaceToTestCount import CodeFaceToTestCount
from Question_average import Question_average

# 最大行数\最大圈复杂度\最大提交次数
MAX_LINE_NUM = 100
MAX_CYCLOMATIC_COMPLEXITY = 40
MAX_COMMIT_TIMES = 40


class CodeHandler:
    __CODE_INFO = []
    __MAX_LINE_NUM = 0
    __MAX_CYCLOMATIC_COMPLEXITY = 0
    __MAX_COMMIT_TIMES = 0
    __res = []

    def __init__(self, max_line_num, max_cyclomatic_complexity, max_commit_times):
        self.__MAX_LINE_NUM = max_line_num
        self.__MAX_CYCLOMATIC_COMPLEXITY = max_cyclomatic_complexity
        self.__MAX_COMMIT_TIMES = max_commit_times

    def list_files(self, path):

        """
        遍历工程路径path，如果遇到文件则统计，如果遇到目录则进行递归
        """

        lineCounter = LineCounter(self.__MAX_LINE_NUM)
        # test_data路径

        filenames = os.listdir(path)
        for f in filenames:
            fpath = os.path.join(path, f)
            if f == 'main.py':
                print("1")
                cases_path = os.path.join(os.path.join(path, '.mooctest'), 'testCases.json')
                code_path = os.path.join(path, f)
                LineCount = 0
                Cyclomatic_Complexity = 0

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

                    else:
                        Cyclomatic_Complexity = self.__MAX_CYCLOMATIC_COMPLEXITY

                else:
                    LineCount = self.__MAX_LINE_NUM
                    Cyclomatic_Complexity = self.__MAX_CYCLOMATIC_COMPLEXITY

                    Commit_Times = self.__MAX_COMMIT_TIMES
                self.__CODE_INFO.append(
                    CodeInfo(dirnames[0], dirnames[1], LineCount, Cyclomatic_Complexity, Commit_Times))
            elif f == '.mooctest':
                # 2020.7.22 zw: debug
                continue
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

    def printResult_average(self, targetPath):

        file = open(targetPath, 'w')
        file.write("{\"1\":[")
        for question in self.__res:
            file.write(json.dumps(question.__dict__))
            file.write(",\n")
        file.truncate()
        file.write("]}")
        file.close()

    def calAverage(self, targetPath):
        file = open(targetPath)
        content = file.read()
        codeinfo_average = json.loads(content)["1"]
        file.close()
        print(codeinfo_average)
        path_score = os.path.abspath('../..') + '\\doc\\Score.csv'
        questions = []
        with open(path_score, encoding='UTF-8') as f:
            for row in f:
                questions.append(str(row.split(",")[0]))
        questions[0] = "2198"
        print(questions)
        for item in questions:
            codeline_average = 0
            cyclomatic_complexity_average = 0
            count = 0
            for answer in codeinfo_average:

                if (answer['case_id'] == item):
                    count += 1
                    codeline_average += answer['code_line']
                    cyclomatic_complexity_average += answer['cyclomatic_complexity']
            if count == 0:
                self.__res.append(Question_average(item, 0.0, 0.0))
                break
            codeline_average = codeline_average / count
            cyclomatic_complexity_average = cyclomatic_complexity_average / count
            self.__res.append(Question_average(item, codeline_average, cyclomatic_complexity_average))
            path = os.path.abspath('../..') + '\\doc\\codeinfo_average.json'
            self.printResult_average(path)


if __name__ == '__main__':
    project_path = "D:\\bigCodeDownloads\\all\\unziped"
    target_path = "D:\\bigCodeDownloads\\2.json"
    handler = CodeHandler(MAX_LINE_NUM, MAX_CYCLOMATIC_COMPLEXITY, MAX_COMMIT_TIMES)
    # handler.list_files(project_path)
    # handler.printResult(target_path)
    handler.calAverage("D:\\bigCodeDownloads\\2.json")
