import json


class GotScoreGetter:
    __examples = {}

    def __init__(self, path):
        file = open(path, encoding='utf-8')
        self.__examples = json.load(file)
        file.close()

    # 获得某个学生某道题的最终得分
    # @param: student_id
    # @param: case_id
    def getScore(self, student_id, case_id):
        cases = self.__examples[student_id]['cases']
        for case in cases:
            if case['case_id'] == case_id:
                return case['final_score']
