def introspection_info(obj):
    type_of_object = type(obj)

    attributes = dir(obj)

    methods = [method for method in dir(obj) if callable(getattr(obj, method))]

    module = getattr(obj, '__module__', None)

    additional_info = {
        "str": lambda s: f"'{s}'",
        "int": lambda i: str(i),
        "float": lambda f: str(f),
        "complex": lambda c: str(c),
        "list": lambda l: f"[{','.join(map(str, l))}]",
        "tuple": lambda t: f"({','.join(map(str, t))})",
        "dict": lambda d: f"{{{','.join(': '.join((repr(k), repr(v))) for k, v in d.items())}}}"}

    try:
        additional_info[type(obj).__name__](obj)
    except KeyError:
        pass

    return {
        "type": type_of_object.__name__,
        "attributes": attributes,
        "methods": methods,
        "module": module,
        **additional_info}


number_info = introspection_info(42)
print(number_info)