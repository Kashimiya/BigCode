from CaseCountByTime import CaseCountByTime
from SearchSameDifficulty import SearchSameDifficulty
import datetime
import time

# 将到HL老师提醒时的完成情况导出到result
if __name__ == '__main__':
    cct = CaseCountByTime(r'C:\Users\13097\Desktop\BigCode-master\test_data.json')
    cct.__init__(r'C:\Users\13097\Desktop\BigCode-master\test_data.json')
    t = datetime.datetime(2020, 3, 31, 23, 59)
    ddl = time.mktime(t.timetuple())
    cct.countByTime(ddl)
    '''
    for i in range(1,30):
        cct = CaseCountByTime("D:\\test_data.json")
        cct.__init__("D:\\test_data.json")
        t = datetime.datetime(2020, 2, i, 23, 59)
        ddl=time.mktime(t.timetuple())
        cct.countByTime(ddl)
    for i in range(1, 32):
        cct = CaseCountByTime("D:\\test_data.json")
        cct.__init__("D:\\test_data.json")
        t = datetime.datetime(2020, 3, i, 23, 59)
        ddl = time.mktime(t.timetuple())
        cct.countByTime(ddl)'''
    # ssd=SearchSameDifficulty("D:\\test_data.json")
    # ssd.countGrade()
