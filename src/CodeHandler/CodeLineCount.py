class LineCounter:
    # 最大行数
    __MAX_LINE_NUM = 0

    def __init__(self, maxLineNum):
        self.__MAX_LINE_NUM = maxLineNum

    def countLines(self, FilePath):

        LineCount = 0

        with open(FilePath, 'rb') as f:
            last_data = '\n'
            while True:
                data = f.read(0x400000)
                if not data:
                    break
                LineCount += data.count(b'\n')
                last_data = data
            if last_data[-1:] != b'\n':
                LineCount += 1

        return LineCount
