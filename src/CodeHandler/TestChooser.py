"""
现在简单做了一个根据分数选择题目的类
使用方法，在创建实例后直接get结果即可
"""
import csv
import json


class TestChooser:
    __student = ""
    __smoothTime = []
    __hardTime = []
    # 挑选的分数段，默认为大于98小于100
    __scoreSet = [98, 100]
    __smoothTestSet = []
    __hardTestSet = []
    # 输出结果 调用get函数即可
    __smoothRes = []
    __hardRes = []

    # @param: student 需要进行选择的学生的编号
    # @param: smoothTime 平滑做作业的区间，包含一个或多个起始和截止的时间戳,两两成对
    # @param: hardTime 赶作业的时间，包含一个或多个起始和截止的时间戳，两两成对
    # @param: path 做题结果json文件路径
    def __init__(self, student, smoothTime, hardTime, path):
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
                    for i in range(len(self.__smoothTime) - 1, 2):
                        if self.__smoothTime[i] < upload[0]["upload_time"] < self.__smoothTime[i + 1]:
                            self.__smoothTestSet.append(case["case_id"])
                    for i in range(len(self.__hardTime) - 1, 2):
                        if self.__hardTime[i] < upload[0]["upload_time"] < self.__hardTime[i + 1]:
                            self.__hardTestSet.append(case["case_id"])
        file.close()

    def __chooseTest(self):
        with open("../doc/Score.csv") as file:
            reader = csv.reader(file)
            lines = list(reader)
            for line in lines:
                if line[0] in self.__smoothTestSet:
                    if self.__scoreSet[0] < float(line[2]) < self.__scoreSet[1]:
                        self.__smoothRes.append(line[0])
                elif line[0] in self.__hardTestSet:
                    if self.__scoreSet[0] < float(line[2]) < self.__scoreSet[1]:
                        self.__hardRes.append(line[0])

    def getSmoothTest(self):
        return self.__smoothRes

    def getHardTest(self):
        return self.__hardRes
