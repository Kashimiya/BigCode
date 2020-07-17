"""
现在简单做了一个根据分数选择题目的类
使用方法：在创建实例后直接get结果即可
"""
import csv
import json
import os


class TestChooser:
    __student = ""
    __smoothTime = []
    __hardTime = []
    # 挑选的分数段，默认为大于98小于100
    __scoreSet = [98, 100]
    # 挑选的提交次数段，默认为大于10小于60
    __commitSet = [10, 60]
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
        self.__student = student
        self.__smoothTime = smoothTime
        self.__hardTime = hardTime
        self.__initTestSet(path)
        self.__chooseTest()

    # 更改挑选的分数段
    # @param: newScoreSet 包含两个数（整数或小数）的数组，最高分数是100
    def setScoreSet(self, newScoreSet):
        self.__scoreSet = newScoreSet

    # 更改挑选的提交次数段
    # @param: newCommitSet 包含两个数（整数或小数）的数组，题均最大提交次数是58.19663034
    def setCommitSet(self, newCommitSet):
        self.__commitSet = newCommitSet

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
                    for i in range(len(self.__smoothTime) - 1, 2):
                        if self.__smoothTime[i] < upload[0]["upload_time"] < self.__smoothTime[i + 1]:
                            self.__smoothTestSet.append(case["case_id"])
                    for i in range(len(self.__hardTime) - 1, 2):
                        if self.__hardTime[i] < upload[0]["upload_time"] < self.__hardTime[i + 1]:
                            self.__hardTestSet.append(case["case_id"])
        file.close()

    # 在initTestSet基础上，挑选出符合分数区间的题
    def __chooseTest(self):
        path = os.path.abspath('..\\..') + '\\doc\\Score.csv'
        file = open(path, 'r')
        reader = csv.reader(file)
        score_lines = list(reader)
        file.close()
        path = os.path.abspath('..\\..') + '\\doc\\CommitTimes.csv'
        file = open(path, 'r')
        reader = csv.reader(file)
        commits_lines = list(reader)
        file.close()
        for score_line in score_lines:
            if score_line[0] in self.__smoothTestSet:
                if self.__scoreSet[0] < float(score_line[2]) < self.__scoreSet[1]:
                    for commits_line in commits_lines:
                        if commits_line[0] == score_line[0]:
                            if self.__commitSet[0] < float(commits_line[1]) < self.__commitSet[1]:
                                self.__smoothRes.append(score_line[0])
            elif score_line[0] in self.__hardTestSet:
                if self.__scoreSet[0] < float(score_line[2]) < self.__scoreSet[1]:
                    for commits_line in commits_lines:
                        if commits_line[0] == score_line[0]:
                            if self.__commitSet[0] < float(commits_line[1]) < self.__commitSet[1]:
                                self.__hardRes.append(score_line[0])

    def getSmoothTest(self):
        return self.__smoothRes

    def getHardTest(self):
        return self.__hardRes
