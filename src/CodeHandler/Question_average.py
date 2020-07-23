class Question_average:
    case_id = ""
    CodeLine_average = 0
    cyclomatic_complexity_average = 0

    def __init__(self, case_id, CodeLine_average, cyclomatic_complexity_average):
        self.case_id = case_id
        self.CodeLine_average = CodeLine_average
        self.cyclomatic_complexity_average = cyclomatic_complexity_average
