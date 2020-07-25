import os
import json
from Question_average import Question_average

# 最大行数\最大圈复杂度
MAX_LINE_NUM = 100
MAX_CYCLOMATIC_COMPLEXITY = 40


class AverageHandler:
    __res = []

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

                if answer['case_id'] == item:
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
    handler = AverageHandler()
    handler.calAverage("D:\\bigCodeDownloads\\2.json")
