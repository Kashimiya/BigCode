"""
采用方法：
目前的版本是统计print个数（因为一般用不了那么多print）
"""

import json


class CodeFaceToTestCount:
    __outputs = []

    # 读取用例答案
    def __init__(self, path):
        file = open(path, encoding='utf-8')
        tests = json.load(file)
        for test in tests:
            self.__outputs.append(test['output'])

    def __getText(self, path):
        txt = open(path, "r", encoding='UTF-8').read()
        txt = txt.lower()
        for char in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~\'':
            # 将文本中特殊字符替换为空格
            txt = txt.replace(char, " ")
        return txt

    def __countPrint(self, path):
        Txt = self.__getText(path)
        words = Txt.split()
        counts = 0
        i = 0
        while i < len(words):
            if words[i] == 'print':
                # 统计了print的个数
                counts += 1
            i += 1
        return counts

    def isFaceToTest(self, path):
        if len(self.__outputs) <= 1:
            # 只有一个用例的情况下，就当作他没有面向用例吧
            return False
        check = self.__countPrint(path)
        return len(self.__outputs) <= check
