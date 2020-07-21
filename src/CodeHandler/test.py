# 筛选的题目代号输出到doc\ChoosenQuestions.json中
import time
from TestChooser import TestChooser
import os

data = [
    ["60686", ["2020-02-14", "2020-03-29"], ["2020-03-29", "2020-03-31"]],
    ["60782", ["2020-02-14", "2020-03-17"], ["2020-03-17", "2020-03-31"]],
    ["60586", ["2020-02-14", "2020-03-28"], ["2020-03-28", "2020-03-31"]],
    ["60688", ["2020-02-14", "2020-03-27"], ["2020-03-27", "2020-03-31"]],
    ["60768", ["2020-02-14", "2020-03-24"], ["2020-03-24", "2020-03-31"]],
    ["61519", ["2020-02-14", "2020-03-30"], ["2020-03-30", "2020-03-31"]],
    ["60590", ["2020-02-14", "2020-03-29"], ["2020-03-29", "2020-03-31"]],
    ["60710", ["2020-02-14", "2020-03-30"], ["2020-03-30", "2020-03-31"]],
    ["60673", ["2020-02-14", "2020-03-23"], ["2020-03-23", "2020-03-31"]],
    ["60712", ["2020-02-14", "2020-03-29"], ["2020-03-29", "2020-03-31"]],
    ["60797", ["2020-02-14", "2020-03-29"], ["2020-03-29", "2020-03-31"]],
    ["59137", ["2020-02-14", "2020-03-28"], ["2020-03-28", "2020-03-31"]],
    ["60611", ["2020-02-14", "2020-03-22"], ["2020-03-22", "2020-03-31"]],
    ["60643", ["2020-02-14", "2020-03-29"], ["2020-03-29", "2020-03-31"]],
    ["60739", ["2020-02-14", "2020-03-27"], ["2020-03-27", "2020-03-31"]],
    ["60825", ["2020-02-14", "2020-03-22"], ["2020-03-22", "2020-03-31"]],
]


def fun1(m, d):
    t = (2020, m, d, 23, 59, 0, 0, 0, 0)
    sec = time.mktime(t)
    return sec


if __name__ == '__main__':

    filepath = "D:\\test_data.json"
    for record in data:
        for i in range(len(record[1])):
            month = int((record[1][i].split("-")[1]))
            day = int(record[1][i].split("-")[2])
            t = (2020, month, day, 23, 59, 0, 0, 0, 0)
            sec = int(fun1(month, day)) * 1000
            record[1][i] = sec
        for i in range(len(record[2])):
            month = int((record[2][i].split("-")[1]))
            day = int(record[2][i].split("-")[2])
            t = (2020, month, day, 23, 59, 0, 0, 0, 0)
            sec = int(fun1(month, day)) * 1000
            record[2][i] = sec
    json_text = ""
    json_text += "{"
    for record in data:
        tc = TestChooser(record[0], record[1], record[2], filepath)
        s = tc.getSmoothTest()
        h = tc.getHardTest()
        tc.setCommitSet([0,100])
        print(s, h)
        json_text += "\"" + record[0] + "\":{"
        json_text += "\"hardset\":" + str(h) + ",\n"
        json_text += "\"smoothset\":" + str(s) + "\n"
        json_text += "},\n"
    json_text = json_text[:-2]
    json_text += "}"
    json_text = json_text.replace("\'", "\"")
    path = os.path.abspath('../..') + '\\doc\\ChoosenQuestions.json'
    file = open(path, 'a', encoding='UTF-8')
    file.write(json_text)
