# from test.assets.typen_testables.basics import basics
# from test.assets.typen_testables.numerics import numerics
# from test.assets.typen_testables.strings import strings
# from test.assets.typen_testables.vectors import vectors
# from test.typen.isnumeric_functions.functions import is_number_repl_isdigit
from intype import is_numeric

candidates = {
    "unicode_1": "1",  # unicode
    "1.0": "1.0",  #
    " 1.0": " 1.0",
    " -3.5": " -3.5",
    b"1": b"1",  # byte
    "A": "A",
    "IV": "IV",  # 罗马数字
    "四": "四",  # 汉字
}


# candidates2 = {
#     **basics,
#     **numerics,
#     **strings,
#     **vectors,
# }


# def is_numeric(some):
#     if isinstance(some, float) or isinstance(some, int):
#         return True
#     if isinstance(some, str):
#         return is_number_repl_isdigit(some)
#     return False


def parse_float(some):
    try:
        return float(some)
    except TypeError:
        return None
    except ValueError:
        return None


def test():
    for (k, v) in candidates.items():
        judge = is_numeric(v)
        print(f'[{k}] ({v})', judge, parse_float(v))


test()
