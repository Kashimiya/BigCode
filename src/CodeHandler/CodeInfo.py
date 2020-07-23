class CodeInfo:
    student_id = ""
    case_id = ""
    code_line = 0
    cyclomatic_complexity = 0

    def __init__(self, student_id, case_id, CodeLine, cyclomatic_complexity):
        self.student_id = student_id
        self.case_id = case_id
        self.code_line = CodeLine
        self.cyclomatic_complexity = cyclomatic_complexity
