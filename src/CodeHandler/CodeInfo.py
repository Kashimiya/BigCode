class CodeInfo:

    FilePath = ""
    CodeLine = 0
    Cyclomatic_Complexity = 0

    def __init__(self, FilePath, CodeLine, Cyclomatic_Complexity):
        self.FilePath = FilePath
        self.CodeLine = CodeLine
        self.Cyclomatic_Complexity = Cyclomatic_Complexity

    # 按照json的格式输出
    def printCodeInfo(self):
        print("{")
        print("FilePath :\'" + self.FilePath + "\',")
        print("CodeRow :" + self.CodeLine + ",")
        print("Cyclomatic_Complexity :" + self.Cyclomatic_Complexity)
        print("},")
