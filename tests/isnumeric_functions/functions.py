from re import compile as re_compile, match as re_match


def is_number_try_except(s):
    """ Returns True is string is a number. """
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_number_regex(s):
    """ Returns True is string is a number. """
    if re_match('^\d+?\.\d+?$', s) is None:
        return s.isdigit()
    return True


comp = re_compile("^\d+?\.\d+?$")


def compiled_regex(s):
    """ Returns True is string is a number. """
    if comp.match(s) is None:
        return s.isdigit()
    return True


def is_number_repl_isdigit(s):
    """ Returns True is string is a number. """
    return s.replace('.', '', 1).isdigit()


def is_number_repl_isnumeric(s):
    """ Returns True is string is a number. """
    return s.replace('.', '', 1).isnumeric()
