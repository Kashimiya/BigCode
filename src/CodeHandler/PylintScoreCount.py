from pylint.lint import Run


class PylintScoreCount:
    __code_path = ""

    def __init__(self, path):
        self.__code_path = path

    def set_path(self, new_path):
        self.__code_path = new_path

    def get_score(self):
        res = Run([self.__code_path], do_exit=False)
        return res.linter.stats['global_note']
