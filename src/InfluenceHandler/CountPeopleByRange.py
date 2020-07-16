import os

class CountPeopleByRange:
    def countPeopleByRange(self,lower,higher):
        # lower和 higher 代表输入做题数目区间的上限和下限
        path=os.path.abspath('../..')+'\\doc\\Result'
        doc = open(path,'r')
        for i in range(0,121):
            temp=doc.readline()
            temp=temp.strip('\n')
            if len(temp)==0:
                continue
            if i==50:
                # 找到黄老师催促以前的数据
                hlBefore=temp
                hlBefore=hlBefore.split(',')
                hlBefore.remove(hlBefore[0])
                for i in range(0,len(hlBefore)):
                    hlBefore[i]=int (hlBefore[i])
            elif i==56:
                # 找到黄老师催促以后的数据
                hlAfter=temp
                hlAfter=hlAfter.split(',')
                hlAfter.remove(hlAfter[0])
                for i in range(0,len(hlAfter)):
                    hlAfter[i]=int (hlAfter[i])
        count=0
        caseBefore=0
        caseAfter=0
        index=[]
        for i in range(0,len(hlBefore)):
            if hlBefore[i]<=higher and hlBefore[i]>=lower:
                index.append(i)
                caseBefore=caseBefore+hlBefore[i]
                count=count+1
        for j in index:
            caseAfter+=hlAfter[j]

        path=os.path.abspath('../..')+'\\doc\\CountPeopleByRangeResult'
        writeDoc=open(path,'a')
        caseBeforeAverage=(caseBefore/count)/10
        caseAfterAverage=((caseAfter-caseBefore)/count)/3
        if(caseBeforeAverage==0):
            growthRate=9999999999
        else:
            growthRate=caseAfterAverage/caseBeforeAverage-1
        # 将区间，人数，前后平均做题数目，前后平均每天做题增长率打印到文件里面
        print("["+str(lower)+','+str(higher)+"],"+str(count),end=",",file=writeDoc)
        print(caseBeforeAverage,end=",",file=writeDoc)
        print(caseAfterAverage,end=",",file=writeDoc)
        print(growthRate,file=writeDoc)

