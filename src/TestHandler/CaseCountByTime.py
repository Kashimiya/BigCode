import time
import json
import os

from SearchSameDifficulty import SearchSameDifficulty


class CaseCountByTime:
    __allDate = {}
    __userId = []
    __caseCount = []

    def __init__(self, path):
        file = open(path, encoding='utf-8')
        self.__allDate = json.load(file)
        self.__caseId = []
        self.__peopleNum = []
        self.__caseAverageGrade = []
        self.__caseCount=[]

    def countByTime(self, deadLine):
        # 给的是deadLine是float类型的时间戳
        deadLine = deadLine * 1000
        for k in self.__allDate:
            # 下面是解析json文件
            student = self.__allDate[k]
            for i in student:
                if i == "user_id":
                    self.__userId.append(student[i])
                    self.__caseCount.append(0)
                if i == "cases":
                    cases = student[i]
                    for oneCase in cases:
                        for j in oneCase:
                            if j == "upload_records":
                                upload_records = oneCase[j]
                                for oneRecord in upload_records:
                                    for m in oneRecord:
                                        if m == "score":
                                            score = oneRecord[m]
                                        if m == "upload_time":
                                            upload_time = oneRecord[m]
                                    if score == 100 and upload_time < deadLine:
                                        self.__caseCount[len(self.__caseCount) - 1] += 1
                                        break
 #在一次提交记录中的时间在deadLine之前以及已经拿到了满分是这个同学的完成题目加一并停止遍历题目
        path=os.path.abspath('..')+'\\doc\\Result'
        doc=open(path,'a')
        print(self.__caseCount,file=doc)
        print(self.__userId,file=doc)
        '''
        #暂用csv格式输出
        deadLine=deadLine/1000
        timeArray=time.localtime(deadLine)
        date = time.strftime("%Y-%m-%d %H:%M:%S",timeArray)
        print(date,end=",",file=doc)
        for i in range(len(self.__caseCount)):
            if(i!=len(self.__caseCount)-1):
                print(self.__caseCount[i],end=",",file=doc)
            else:
                print(self.__caseCount[i],end="",file=doc)
        print("\n",file=doc)
        doc.close()
        '''
