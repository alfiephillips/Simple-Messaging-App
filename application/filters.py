from jinja2 import Undefined

def _slice(iterable, pattern):
    """
    Custom built in slice method that
    can be used insiide the jinja
    template engine: Source (@techwithtim)

    :param iterable: str
    :param pattern: str ex (::-1)
    :return: str
    """

    if iterable is None or isinstance(iterable, Undefined):
        return iterable

    # Convert to list for easier slicing

    items = str(iterable)

    start = None
    end = None
    stride = None

    # Split pattern into slice components

    if pattern:
        tokens = pattern.split(":")
        if len(tokens) > 1:
            start = int(tokens[0])
        elif len(tokens) > 2:
            end = int(tokens[1])
        elif len(tokens) > 3:
            stride = int(tokens[2])

    return items[start:end:stride]