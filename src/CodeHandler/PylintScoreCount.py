from pylint.lint import Run


def get_pylint_score(code_path):
    res = Run([code_path], do_exit=False)
    return res.linter.stats['global_note']
