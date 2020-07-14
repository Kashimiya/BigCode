"""
这里面的方法主要完成计算每个题目的均分以及对于均分进行排序
"""

import json
import os


class SearchSameDifficulty:
    __allDate = {}
    __peopleNum = []
    __caseId = []
    __caseAverageGrade = []

    def __init__(self, path):
        # path是json文件路径
        file = open(path, encoding='utf-8')
        self.__allDate = json.load(file)
        self.__caseId = []
        self.__peopleNum = []
        self.__caseAverageGrade = []

    def countGrade(self):
        # 下面都是解析json文件
        for k in self.__allDate:
            student = self.__allDate[k]
            for i in student:
                if i == "cases":
                    cases = student[i]
                    for oneCase in cases:
                        for j in oneCase:
                            if j == "case_id":
                                index = len(self.__caseId)
                                for m in range(0, len(self.__caseId)):
                                    if self.__caseId[m] == oneCase[j]:
                                        index = m
                                        self.__caseAverageGrade[m] = (self.__caseAverageGrade[m] * (
                                            self.__peopleNum[m]) + oneCase["final_score"]) / (self.__peopleNum[m] + 1)
                                        # 每输入一个分数计算平均分
                                        self.__peopleNum[m] += 1
                                if index == len(self.__caseId):
                                    self.__caseId.append(oneCase[j])
                                    self.__peopleNum.append(1)
                                    self.__caseAverageGrade.append(oneCase["final_score"])
        self.__sortByGrade()

    def __sortByGrade(self):
        # 利用排序算法将caseAverageGrade排序，同时caseId和peopleNum也跟着其改变排位
        for i in range(0, len(self.__caseAverageGrade)):
            for j in range(0, i):
                if self.__caseAverageGrade[i] > self.__caseAverageGrade[j]:
                    temp1 = self.__caseAverageGrade[i]
                    temp2 = self.__peopleNum[i]
                    temp3 = self.__caseId[i]
                    for k in range(i, j, -1):
                        self.__caseId[k] = self.__caseId[k - 1]
                        self.__peopleNum[k] = self.__peopleNum[k - 1]
                        self.__caseAverageGrade[k] = self.__caseAverageGrade[k - 1]
                    self.__caseAverageGrade[j] = temp1
                    self.__peopleNum[j] = temp2
                    self.__caseId[j] = temp3
        path = os.path.abspath('..') + '\\doc\\Result'
        doc = open(path, 'a')

        print(self.__caseId, file=doc)
        print(self.__peopleNum, file=doc)
        print(self.__caseAverageGrade, file=doc)
        '''
        #暂时修改成csv格式输出
        for i in range(len(self.__caseId)):
            print(str(self.__caseId[i])+","+str(self.__peopleNum[i])+","+str(self.__caseAverageGrade[i]),file=doc)
=======
        path = os.path.abspath('..') + '\\doc\\Result'
        doc = open(path, 'a')
        print(self.__caseId, file=doc)
        print(self.__peopleNum, file=doc)
        print(self.__caseAverageGrade, file=doc)
>>>>>>> 7de97cf9cf774d29f598bdafd93dd2f8b4547f65
        doc.close()
        '''
