'''
原代码地址https://blog.csdn.net/qq_37503890/article/details/89406681
采用方法：
1.记录该题所有的答案（output）
2.检测代码中是否存在print(答案)的现象
3.只有print了所有的答案才算面向用例
'''

import json

class CodeFaceToTestCount:

    __outputs = []

    def __init__(self, path):
        file = open(path, encoding='utf-8')
        tests = json.load(file)
        self.__outputs = tests['output']

    def __getText(self, path):
        txt = open(path, "r").read()
        txt = txt.lower()
        for char in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~\'':
            txt = txt.replace(char, " ")  # 将文本中特殊字符替换为空格
        return txt

    def __countPrint(self, path):
        Txt = self.__getText(path)
        words = Txt.split()
        counts = 0
        i = 0
        while (i < len(words)):
            if words[i] == 'print':
                i += 1
                if words[i] in self.__outputs:
                    counts += 1
            i += 1
        return counts

    def isFaceToTest(self, path):
        return len(self.__outputs) <= self.__countPrint(path)