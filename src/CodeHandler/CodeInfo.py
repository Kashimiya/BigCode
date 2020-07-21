class CodeInfo:
    FilePath = ""
    CodeLine = 0
    cyclomatic_complexity = 0
    pylint_score = 0
    commit_times = 0

    def __init__(self, FilePath, CodeLine, cyclomatic_complexity, pylint_score, commit_times):
        self.FilePath = FilePath
        self.CodeLine = CodeLine
        self.cyclomatic_complexity = cyclomatic_complexity
        self.pylint_score = pylint_score
        self.commit_times = commit_times
