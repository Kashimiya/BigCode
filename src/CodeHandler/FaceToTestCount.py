"""
原代码地址https://blog.csdn.net/qq_37503890/article/details/89406681
采用方法：
1.记录该题所有的答案（output）
2.检测代码中是否存在print(答案)的现象
3.只有print了所有的答案才算面向用例
4.(7月1日改)上面的方法理论上可以实现，而且应该准确率较高，但是我还没有想出来实现的方法，目前的版本是统计print个数（因为一般用不了那么多print）
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
                # 现在只是简单统计了print的个数
                counts += 1
            i += 1
        return counts

    def isFaceToTest(self, path):
        if len(self.__outputs) <= 1:
            # 只有一个用例的情况下，就当作他没有面向用例吧
            return False
        return len(self.__outputs) <= self.__countPrint(path)
