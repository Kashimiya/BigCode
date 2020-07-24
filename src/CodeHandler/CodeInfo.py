class CodeInfo:
    student_id = ""
    case_id = ""
    question_name = ""
    code_line = 0
    cyclomatic_complexity = 0
    time_category = 0

    def __init__(self, student_id, case_id, question_name, CodeLine, cyclomatic_complexity, time_category):
        self.student_id = student_id
        self.case_id = case_id
        self.question_name = question_name
        self.code_line = CodeLine
        self.cyclomatic_complexity = cyclomatic_complexity
        self.time_category = time_category
