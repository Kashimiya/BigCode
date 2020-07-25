import os
import json
import ast
import mccabe_alter
import time
import CodeLineCount
import ResultHandler.draw_result as output
from CodeInfo import CodeInfo
from FaceToTestCount import CodeFaceToTestCount
from ResultHandler.pca_dealer import PcaDealer
from util.DownloadCode import DownloadCode
from TimeZoneHandler import TimeZoneHandler

# 最大行数\最大圈复杂度
MAX_LINE_NUM = 100
MAX_CYCLOMATIC_COMPLEXITY = 40


class CodeHandler:
    __CODE_INFO = []
    __MAX_LINE_NUM = 0
    __MAX_CYCLOMATIC_COMPLEXITY = 0

    def __init__(self, max_line_num, max_cyclomatic_complexity):
        self.__MAX_LINE_NUM = max_line_num
        self.__MAX_CYCLOMATIC_COMPLEXITY = max_cyclomatic_complexity

    def list_files(self, path, uid):

        """
        遍历工程路径path，如果遇到文件则统计，如果遇到目录则进行递归
        """
        codeinfo_average_path = os.path.abspath('../..') + '\\doc\\codeinfo_average.json'
        codeinfo_file = open(codeinfo_average_path)
        codeinfo_average = json.loads(codeinfo_file.read())['1']

        filenames = os.listdir(path)

        for f in filenames:
            fpath = os.path.join(path, f)
            if f == 'main.py':
                cases_path = os.path.join(os.path.join(path, '.mooctest'), 'testCases.json')
                code_path = os.path.join(path, f)
                LineCount = 0
                Cyclomatic_Complexity = 0
                dirnames = os.path.split(path)[1].split('_')
                if dirnames[0] != str(uid):
                    continue
                name = dirnames[2]
                timestamp = int(str(dirnames[3]).split('.')[0])
                timeArray = time.localtime(timestamp // 1000)  # 秒数
                StyledTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                time_category = int(StyledTime.split(' ')[1].split(':')[0])
                if self.__checkPY(code_path):
                    FaceToTestHandler = CodeFaceToTestCount(cases_path)
                    if FaceToTestHandler.isFaceToTest(code_path):
                        LineCount = self.__MAX_LINE_NUM
                        Cyclomatic_Complexity = self.__MAX_CYCLOMATIC_COMPLEXITY
                    else:
                        LineCount = CodeLineCount.countLines(code_path)
                        Cyclomatic_Complexity = mccabe_alter.get_module_complexity(code_path, 0)
                else:
                    LineCount = self.__MAX_LINE_NUM
                    Cyclomatic_Complexity = self.__MAX_CYCLOMATIC_COMPLEXITY
                for question in codeinfo_average:
                    # 和平均数的比值
                    if question['case_id'] == dirnames[1]:
                        LineCount = LineCount / question['CodeLine_average']
                        Cyclomatic_Complexity = Cyclomatic_Complexity / question['cyclomatic_complexity_average']
                        break
                self.__CODE_INFO.append(
                    CodeInfo(dirnames[0], dirnames[1], name, LineCount, Cyclomatic_Complexity, time_category))
            elif f == '.mooctest':
                continue
            elif os.path.isdir(fpath):
                self.list_files(fpath, uid)

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
        file.write("{\"1\":[\n")
        for i in range(len(self.__CODE_INFO)):
            file.write(json.dumps(self.__CODE_INFO[i].__dict__))
            if i != len(self.__CODE_INFO) - 1:
                file.write(",\n")
        file.write("]}\n")
        file.close()


if __name__ == '__main__':
    # download part
    uid = int(input())
    dlcode = DownloadCode(uid)
    dlcode.download()

    # this part
    project_path = "D:\\bigCodeDownloads\\unziped"
    target_path = path = os.path.abspath('../..') + '\\doc\\codeinfo.json'
    handler = CodeHandler(MAX_LINE_NUM, MAX_CYCLOMATIC_COMPLEXITY)
    handler.list_files(project_path, uid)
    handler.printResult(target_path)

    # pca part
    pca_dealer = PcaDealer()
    matrix = pca_dealer.pca()
    order = pca_dealer.get_code_order()
    Path = os.path.abspath('..\\..') + '\\doc\\after_pca.csv'
    res = ""
    for i in range(len(order)):
        res += str(order[i]) + ',' + str(matrix[i][0]) + "\n"
    doc = open(Path, 'w')
    doc.write(res)
    doc.close()

    # time zone
    tzh = TimeZoneHandler()
    tzh.TimeZonePrint()

    # print result
    output.draw_result()
