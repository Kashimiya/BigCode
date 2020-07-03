'''
这里面的方法主要完成计算每个题目的均分以及对于均分进行排序
'''

import json

class SearchSameDifficulty:

    allDate={}
    peopleNum=[]
    caseId=[]
    caseAverageGrade=[]

    def __init__(self,path):
        global allDate,caseId,peopleNum,caseAverageGrade
        file = open(path, encoding='utf-8')
        allDate=json.load(file)
        caseId=[]
        peopleNum=[]
        caseAverageGrade=[]

    def countGrade(self):
        global allDate,caseId,peopleNum,caseAverageGrade
        #下面都是解析json文件
        for k in allDate:
            student=allDate[k]
            for i in student:
                if i=="cases":
                    cases=student[i]
                    for oneCase in cases:
                        for j in oneCase:
                            if j=="case_id":
                                index=len(caseId)
                                for m in range(0,len(caseId)):
                                    if caseId[m]==oneCase[j]:
                                        index=m
                                        caseAverageGrade[m]=(caseAverageGrade[m]*(peopleNum[m])+oneCase["final_score"])/(peopleNum[m]+1)
                                        #每输入一个分数计算平均分
                                        peopleNum[m]+=1
                                if index==len(caseId):
                                    caseId.append(oneCase[j])
                                    peopleNum.append(1)
                                    caseAverageGrade.append(oneCase["final_score"])
        print(caseId)
        print(peopleNum)
        print(caseAverageGrade)
        self.sortByGrade()
    def sortByGrade(self):
        global allDate,caseId,peopleNum,caseAverageGrade
        #利用排序算法将caseAverageGrade排序，同时caseId和peopleNum也跟着其改变排位
        for i in range(0,len(caseAverageGrade)):
            for j in range(0,i):
                if caseAverageGrade[i]>caseAverageGrade[j]:
                    temp1=caseAverageGrade[i]
                    temp2=peopleNum[i]
                    temp3=caseId[i]
                    for k in range(i,j,-1):
                        caseId[k]=caseId[k-1]
                        peopleNum[k]=peopleNum[k-1]
                        caseAverageGrade[k]=caseAverageGrade[k-1]
                    caseAverageGrade[j]=temp1
                    peopleNum[j]=temp2
                    caseId[j]=temp3
        print(caseId)
        print(peopleNum)
        print(caseAverageGrade)