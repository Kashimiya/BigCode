import json
import os
import pandas as pd


class CommitTimesCounter:
    __examples = {}
    __caseId = []
    __caseAvgCommitTimes = []
    __peopleNum = []

    # @param: path 做题结果json的路径
    def __init__(self, path):
        file = open(path, encoding='utf-8')
        self.__examples = json.load(file)
        file.close()

    # 获得学生某道题的提交次数
    # @param: student 学生的编号
    # @param: test 题目编号
    def getCommitTimes(self, student, test):
        cases = self.__examples[student]['cases']
        for case in cases:
            if case['case_id'] == test:
                return len(case['upload_records'])

    # 将所有题目的平均提交次数输出到文件
    def printAvgCommitTimes(self):
        for example in self.__examples:
            example = self.__examples[example]
            cases = example["cases"]
            for case in cases:
                index = len(self.__caseId)
                commitTimes = len(case["upload_records"])
                if commitTimes != 0:
                    for i in range(len(self.__caseId)):
                        if self.__caseId[i] == case["case_id"]:
                            index = i
                            self.__peopleNum[i] += 1
                            self.__caseAvgCommitTimes[i] = (self.__caseAvgCommitTimes[i] * self.__peopleNum[
                                i] + commitTimes) / self.__peopleNum[i]
                    if index == len(self.__caseId):
                        self.__caseId.append(case["case_id"])
                        self.__peopleNum.append(1)
                        self.__caseAvgCommitTimes.append(commitTimes)
        path = os.path.abspath('..\\..') + '\\doc\\CommitTimes.csv'
        doc = open(path, 'a')
        for i in range(len(self.__caseId)):
            print(str(self.__caseId[i]) + ',' + str(self.__caseAvgCommitTimes[i]), file=doc)


if __name__ == '__main__':
    # ctc = CommitTimesCounter("D:\\test_data.json")
    # ctc.printAvgCommitTimes()
    # 用pandas对csv排序
    path = os.path.abspath('..\\..') + '\\doc\\CommitTimes.csv'
    file = pd.read_csv(path)
    data = file.sort_values(by="CommitTimes", ascending=True)
    data.to_csv("new.csv", mode='a+', index=False)
