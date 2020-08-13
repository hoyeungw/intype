import inspect


def sample_func(alpha, beta=0, *args, x, y=1, **kvps):
    pass


name = sample_func.__name__
signature = inspect.signature(sample_func)
print(f'inspect.signature({name}) is {signature} ({type(signature)})')
parameters = signature.parameters
print(f'signature.parameters is {parameters} ({type(parameters)})')
for k, v in parameters.items():
    print(f'[kind] ({v.kind}) {k}，{v} [default] ({v.default}) [type] ({type(k)}，{type(v)})')
