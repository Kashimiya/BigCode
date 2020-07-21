"""
使用方法：在创建实例后直接get结果即可
"""
import csv
import json
import os
from GotScoreGetter import GotScoreGetter


class TestChooser:
    __student = ""
    __smoothTime = []
    __hardTime = []
    # 挑选的分数段，默认为大于97小于100
    __scoreSet = [97, 100]
    # 挑选的提交次数段，默认为大于0小于6.5
    __commitSet = [0, 6.5]
    # 挑选的得分段，默认大于等于50小于等于100
    __gotScoreSet = [50, 100]

    __smoothTestSet = []
    __hardTestSet = []
    # 输出结果 调用get函数即可
    __smoothRes = []
    __hardRes = []

    # @param: student 需要进行选择的学生的编号
    # @param: smoothTime 平滑做作业的区间，包含一个或多个起始和截止的时间戳，两两成对
    # @param: hardTime 赶作业的区间，包含一个或多个起始和截止的时间戳，两两成对
    # @param: path 做题结果json文件路径
    def __init__(self, student, smoothTime, hardTime, path):
        # 初始化结果
        self.__smoothRes = []
        self.__hardRes = []
        self.__hardTestSet = []
        self.__smoothTestSet = []

        self.__student = student
        self.__smoothTime = smoothTime
        self.__hardTime = hardTime
        self.__initTestSet(path)
        self.__chooseTest()

    # 挑选出该同学在平常阶段和赶作业阶段做的题目的编号
    def __initTestSet(self, path):
        file = open(path, encoding='utf-8')
        examples = json.load(file)
        for example in examples:
            if example == self.__student:
                student = examples[example]
                cases = student["cases"]
                for case in cases:
                    upload = case["upload_records"]
                    '''for i in range(len(self.__smoothTime) - 1, 2):
                        if self.__smoothTime[i] < upload[0]["upload_time"] < self.__smoothTime[i + 1]:
                            self.__smoothTestSet.append(case["case_id"])'''
                    for i in range(len(self.__smoothTime) // 2):
                        if self.__smoothTime[i * 2] < upload[0]["upload_time"] < self.__smoothTime[i * 2 + 1]:
                            self.__smoothTestSet.append(case["case_id"])
                    '''for i in range(len(self.__hardTime) - 1, 2):
                        if self.__hardTime[i] < upload[0]["upload_time"] < self.__hardTime[i + 1]:
                            self.__hardTestSet.append(case["case_id"])'''
                    for i in range(len(self.__hardTime) // 2):
                        if self.__hardTime[i * 2] < upload[0]["upload_time"] < self.__hardTime[i * 2 + 1]:
                            self.__hardTestSet.append(case["case_id"])
        file.close()

    # 在initTestSet基础上，挑选出符合分数区间的题
    def __chooseTest(self):
        path = os.path.abspath('..\\..') + '\\doc\\Score.csv'
        file = open(path, 'r', encoding='UTF-8')
        reader = csv.reader(file)
        score_lines = list(reader)
        file.close()
        path = os.path.abspath('..\\..') + '\\doc\\CommitTimes.csv'
        file = open(path, 'r')
        reader = csv.reader(file)
        commits_lines = list(reader)
        file.close()
        score_getter = GotScoreGetter("D:\\test_data.json")
        for score_line in score_lines:
            if score_line[0] in self.__smoothTestSet:
                if self.__scoreSet[0] < float(score_line[2]) < self.__scoreSet[1]:
                    for commits_line in commits_lines:
                        if commits_line[0] == score_line[0]:
                            if self.__commitSet[0] < float(commits_line[1]) < self.__commitSet[1]:
                                if self.__gotScoreSet[0] <= score_getter.getScore(self.__student, score_line[0]) <= \
                                        self.__gotScoreSet[1]:
                                    self.__smoothRes.append(score_line[0])
                            break
            elif score_line[0] in self.__hardTestSet:
                if self.__scoreSet[0] < float(score_line[2]) < self.__scoreSet[1]:
                    for commits_line in commits_lines:
                        if commits_line[0] == score_line[0]:
                            if self.__commitSet[0] < float(commits_line[1]) < self.__commitSet[1]:
                                if self.__gotScoreSet[0] <= score_getter.getScore(self.__student, score_line[0]) <= \
                                        self.__gotScoreSet[1]:
                                    self.__hardRes.append(score_line[0])
                            break

    def getSmoothTest(self):
        return self.__smoothRes

    def getHardTest(self):
        return self.__hardRes
